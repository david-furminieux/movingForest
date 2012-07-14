grammar MFQL;
options {
  language=Python;
}

@header {

from taj.expr import NullConstant, Integer, Float, String, Summ, Product, \
    Function, Array, Map
from taj.logic import Conjunction, Disjunction, Comparaison, Negation, IsNull, \
    IsKey, Boolean
from taj.parser.base import SyntaxError
from taj.parser.stmt import SelectStatement, Rename, SimpleRelation, \
    TableCreationStatement, StreamCreationStatement, InsertStatement, \
    UpdateStatement, DropRequest, AlterRequest, AssignmentStatement, Stream, \
    SimpleStream, AmountWindow, TimeWindow, ComposedRelation, WindowedStream, \
    DeleteStatement, RenameRelation
from taj.path import Path, AttributeAccess, IdxAccess

def escapeString(str):
    str = str.replace('\\n', '\n')
    return str

def createSinglePath(str):
    result = Path()
    result.append(AttributeAccess(str))
    return result

}

@members {
#def displayRecognitionError(self, tokenNames, e):
#  print tokenNames
#  print e

def emitErrorMessage(self, msg):
  raise SyntaxError(msg)
}

/* ****************************************************************************
 * Statements
 */
 
stmts returns [ list result ]
  : { result = [] }
    (s=stmt ';' { result.append(s) })+
  ;

stmt returns [ Statement result ]
  : s=createStmt           { result = s }
  | s=selectStmt           { result = s }
  | s=insertStmt           { result = s }
  | s=updateStmt           { result = s }
  | s=deleteStmt           { result = s }
  | s=globalAssignmentStmt { result = s }
  ;

createStmt returns [CreateStatement result]
  : CREATE
    ( TABLE n=name d=tableDef
      { result = TableCreationStatement(n, d) }
    | ( INPUT  { type = StreamCreationStatement.INPUT  }
      | OUTPUT { type = StreamCreationStatement.OUTPUT }
      ) STREAM n=name d=streamDef
      { result = StreamCreationStatement(n, d, type) }
    )
  ;

selectStmt returns [SelectStatement result]
  : SELECT
    { result = SelectStatement() }
    (DISTINCT { result.setDistinct(True) } )? 
    ( l=attrSel                 { stream = Stream.NONE     } 
    | ISTREAM '(' l=attrSel ')' { stream = Stream.INSERT   }
    | DSTREAM '(' l=attrSel ')' { stream = Stream.DELETE   }
    | RSTREAM '(' l=attrSel ')' { stream = Stream.RELATION }
    )
    { result.setProjections(l) }
    { result.setStreamingOp(stream) }
    FROM r=relation { result.setSource(r) }
    (WHERE r=whereRestriction { result.setSelection(r) })?
//    (GROUP BY pathList)?
//    (HAVING predicate)?
  ;

attrSel returns [list result]
  : STAR                 { result = []   }
  | list=renamedAttrList { result = list }
  ;
    
insertStmt returns [InsertStatement result]
  : INSERT INTO
    r=simpleRelation
    s=selectStmt
    { result = InsertStatement(); result.setTarget(r) }
    { result.setSource(s) }
  ;
    
updateStmt returns [UpdateStatement result]
  : UPDATE rel=simpleRelation
    { orders = [] } 
    (
      SET  l=modifOrders  { orders.extend(l) }  
    | DROP l=dropOrders   { orders.extend(l) }
    )+
    (WHERE res=whereRestriction)?
    { result = UpdateStatement()    }
    { result.setTarget(rel)         }
    { result.setAlterations(orders) }
    { result.setSelection(res)      }
  ;

deleteStmt returns [DeleteStatement result]
  : DELETE FROM
    rel=simpleRelOrStr
    (WHERE res=whereRestriction)?
    { result = DeleteStatement() }
    { result.setTarget(rel)      }
    { result.setSelection(res)   }
  ;

globalAssignmentStmt returns [AssignmentStatement result]
  : SET n=name '=' c=constant
    { result = AssignmentStatement() }
    { result.setName(n)              }
    { result.setValue(c)             }
  ;

modifOrders returns [list result]
  : { result = [] }
    o=modifOrder { result.append(o) }
    ( ',' o=modifOrder { result.append(o) } )*
  ;

dropOrders returns [list result]
  : { result = [] }
    p=path { result.append(DropRequest(p)) }
    ( ',' p=path { result.append(DropRequest(p)) } )*
  ;
      
modifOrder returns [AlterRequest result]
  : p=path '=' e=expr { result = AlterRequest(p, e) }
  ;

streamDef returns [dict result]
  : '(' s=optionStruct ')' { result = s }
  ;
    
tableDef returns [Integer result]
  : AS s=selectStmt { result = s }
  ;

whereRestriction returns [Predicate result]
  : p=predicate { result = p }
  ;

renamedAttrList returns [list result]
  :  { result = []; count=1 }
     e=expr { newName = None }
     (AS p=path { newName = p })?
     { if newName is None: newName = createSinglePath('var1') }
     { result.append(Rename(e, newName)) }
     (
       ',' e=expr { newName = None; count += 1 }
       (AS p=path { newName = p })?
       { if newName is None: newName = createSinglePath('var' + str(count)) }
       { result.append(Rename(e, newName)) }
     )*
  ;
    
optionStruct returns [dict result]
  : { result = dict() }
    o=option { (key, value) = o; result[key] = value }
    (',' o=option { (key, value) = o; result[key] = value })*
  ;

option returns [tuple result]
  : n=name '='
    ( c=constantStruct       { result = (n, c) }
    | '(' s=optionStruct ')' { result = (n, s) }
    )
  ;

/* ****************************************************************************
 * Relations and Joins
 */

relation returns [Relation result]
  : { result = ComposedRelation(); many = False }
    r1=simpleRelOrStr { result.cross(r1) }
    ( ',' r=simpleRelOrStr { result.cross(r); many = True }
//    | (LEFT|RIGHT) (OUTER)? JOIN r=simpleRelOrStr ON '(' expr ')'
    )*
    { if not many: result = r1 }
  ;
  
simpleRelOrStr returns [Relation result]
  : ( r=simpleRelation { result = r }
    | s=simpleStream   { result = s }
    )
    ( AS p=path { result = RenameRelation(result, p) } )?
  ;

simpleRelation returns [Relation result]
  : n=name { result = SimpleRelation(n) }
  ;

simpleStream returns [Relation result]
  : n=name { result = WindowedStream(SimpleStream(n)) }
    '[' w=windowSpecification ']' { result.setWindow(w) }
  ;

/* ****************************************************************************
 * Windows
 */
windowSpecification returns [Window result]
  : { partition = None }
    (PARTITION BY { partition = [] }
      p=path { partition.append(p) }
      (',' path { partition.append(p) } )*
    )?
    ( UNBOUNDED                      { result = AmountWindow(-1)   }
    | NOW                            { result = TimeWindow(0)       }
    | RANGE i=integer scale=timeUnit { result = TimeWindow(i*scale) }
    | ROWS i=integer                 { result = AmountWindow(i)     }
    )
    { if partition is not None: result.setPartition(partition) }
  ;

timeUnit returns [TimeUnit result]
  : SECONDS { result = 1    }
  | MINUTES { result = 60   }
  | HOURS   { result = 3600 }
  ;

/* ****************************************************************************
 * Basic stuff
 */

//predOrExpr returns [Expression result]
//  : e=expr      { result = e }
//  | p=predicate { result = p }
//  ;

eof
  : EOF
  ;

integer returns [int result]
  : { invert = False }
    (MINUS { invert = True })?
    NUM
    {
      result = int($NUM.text)
      if invert: result = -result
    }
  ;

boolean returns[ bool result ]
  : TRUE  { result = True }
  | FALSE { result = False }
  ;

string returns [string result]
  : STR  { result = escapeString($STR.text[1:-1])  }
  | DSTR { result = escapeString($DSTR.text[1:-1]) }
  ;

constantStruct returns [ object result ]
  : c=constant { result = c }
  | '{' { result = dict() }
    ( n=string ':' s=constantStruct { result[n] = s } )?
    ( ','  n=string ':' s=constantStruct { result[n] = s } )*
    '}'
  | '[' { result = list() }
    ( e=constantStruct { result.append(e) } )?
    ( ',' e=constantStruct { result.append(e) } )*
    ']'
  ;

nonLogicConstant returns [ Constant result]
  : i=cInt      { result = i                }
  | NULL        { result = NullConstant()   }
  | f=cFloat    { result = f                }
  | s=cString   { result = s                }
  ;

logicConstant returns [ Constant result ]
  : b=cBoolean         { result = b }
  ;

constant returns [ Constant result ]
  : b=logicConstant    { result = b }
  | c=nonLogicConstant { result = c }
  ;

cBoolean returns [ Constant result ]
  : v=boolean  { result = Boolean(v) }
  ;
    
cInt returns [ Integer result ]
  : i=integer { result = Integer(i) }
  ;

cFloat returns [ Float result ]
  : MINUS? FLOAT { result = Float(float($FLOAT.text)) }
  ;

cString returns [ String result ]
  : s=string { result = String(s) }
  ;

/* ****************************************************************************
 * Expressions
 */

expr returns [ Expression result ]
  : f1=factor
    { result = Summ(); result.add(f1); many = False }
    ( PLUS  f2=factor { result.add(f2); many = True }
    | MINUS f2=factor { result.sub(f2); many = True }
    )*
    { if not many: result = f1 }
  ;

exprList returns [ list result ]
  : { result = [] }
    (e=expr { result.append(e) } )?
    ( ',' e=expr { result.append(e) })*
  ;

factor returns [ Expression result ]
  : t1=term
    { result = Product(); result.multiply(t1); many = False }
    ( STAR    t2=term    { result.multiply(t2); many = True }
    | SLASH   t2=term    { result.divide(t2);   many = True }
    | PERCENT t2=term    { result.modulo(t2);   many = True }
    )*
    { if not many: result = t1 }
  ;

term returns [ Expression result ]
  : p=pattern                            { result = p }
//  c=nonLogicConstant                   { result = c }
//  | p=path                               { result = p }
//  | (path)=> p=path                      { result = p }
//  | s=selector                           { result = s }
  | f=functionName '(' args=exprList ')'
    { result = Function(f); result.setArguments(args) }
  | '(' e=expr ')'                       { result = e }
  ; 

functionName returns [String result]
  : s=anum { result = s }
  ;

name returns [String result]
  : s=anum { result = s }
  ;
 
/* ****************************************************************************
 * paths, patterns and selectors
 */

path returns [ Path result ]
  : DOT { result = Path() }
    (
      '[' i=integer ']' { result.append(IdxAccess(i)) }
      ( p=pathPart {result.append(p)})*
    ) ?
  | DOT? n=name { result = Path(); result.append(AttributeAccess(n)) }
    ( p=pathPart {result.append(p)})*
  ;

pathPart returns [String result]
  : DOT n=name { result = AttributeAccess(n) }
  | '[' i=integer ']' { result = IdxAccess(i) }
  ;
      
pattern returns [Pattern result]
  : c=nonLogicConstant { result = c }
  | s=selector         { result = s }
  | '[' { result = Array() } (p=pattern { result.add(p) })?
    ( ',' p=pattern { result.add(p) } )*
    ']'
  | '{' { result = Map() } (name1=string ':' p=pattern { result.put(name1, p) })?
    ( ',' name2=string ':' p=pattern { result.put(name2, p) })*
    '}' 
  ;

// selector are not implemented yet
selector returns [Path result]
  : p=path { result = p }
  ; 

//selector returns [Selector result]
//  : DOT { result = Selector() }
//  | { deep = False }
//    (DOTDOT { deep = True } | DOT)?
//    n=name
//    { result = Selector(); }
//    { if not deep: result.append(AttributeAccess(n)) }
//    { if deep: result.append(DeepAttributeAccess(n)) }
//    ( p=selectorPart {result.append(p)})*
//  | { result = Selector() }
//    DOT i=selectorIdx { result.append(i) }
//    ( p=selectorPart {result.append(p)})*
//  | AT { result = Selector(); result.setRelative(True) }
//    ( p=selectorPart {result.append(p)})+
//  ;

//selectorPart returns [SelectorPart result]
//  : (DOTDOT { deep=True } |DOT { deep=False })
//    (n=name | STAR { n=None })
//    { if n is not None and deep:     result = DeepAttributeAccess(n) }
//    { if n is not None and not deep: result = AttributeAccess(n) }
//    { if n is None and deep:         result = WideDeepAttributeAccess() }
//    { if n is None and not deep:     result = WideAttributeAccess() }
//    
//  | idx = selectorIdx { result = idx }
//  ;

//selectorIdx returns [SelectorPart result]
//  :'['
//    ( STAR                                { result = WideAttributeAccess() }
//    | (predicate) => p=predicate
//      { result = ConditionalAccess(); result.add(p) }
//      ( ',' p=predicate { result.add(p) } )*
//    | { rel = False }
//      (AT { rel = True })?
//      p=path
//      {  result = PathAccess(p); result.setRelative(rel) }
//    | ':' i2=integer                      { result = RangeAccess(None, i2)   }
//    | i1=integer                          { result = IdxAccess(i1)           }
//      ( ':' i2=integer (':' i3=integer )? { result = RangeAccess(i1, i2, i3) }
//      | { idxs=[i1] } ( ',' i=integer { idxs.append(i) } )+
//                                          { result = EnumAccess(idxs)        }
//      ) ?
//    )
//    ']'
//  ;

/* ****************************************************************************
 * Logic
 */
 
predicate returns [ Predicate result ]
  : { result = Conjunction(); many = False }
    f1=lfactor
    { result.add(f1) }
    ( AND f=lfactor { result.add(f); many = True })*
    { if not many: result = f1 }
  ;

lfactor returns [ Predicate result ]
  : { result = Disjunction(); many = False }
    t1=lterm
    { result.add(t1) }
    ( OR t=lterm { result.add(t); many = True })*
    { if not many: result = t1 }
  ;
  
lterm returns [ Predicate result ]
  : { negated = False }
    ( NOT { negated=True })?
    ( ('(' predicate) => '(' p=predicate ')' { val = p } 
    | val=logicConstant
    | e1=expr
        ( op=comparaisonOp e2=expr { val = Comparaison(op, e1, e2) }
        | IS NULL                  { val = IsNull(e1)              }
        | IS KEY                   { val = IsKey(e1)               }
        ) 
    )
    { if negated: val = Negation(val) }
    { result = val } 
  ;

comparaisonOp returns [ int result ]
  : '<'  { result = Comparaison.LESS          }
  | '<=' { result = Comparaison.LESS_EQUAL    }
  | '='  { result = Comparaison.EQUAL         }
  | '==' { result = Comparaison.EQUAL         }
  | '<>' { result = Comparaison.UNEQUAL       }
  | '!=' { result = Comparaison.UNEQUAL       }
  | '>=' { result = Comparaison.GREATER_EQUAL }
  | '>'  { result = Comparaison.GREATER       }
  | '><' { result = Comparaison.SIMILAR       }
  ;

/* ****************************************************************************
 * TERMINALS
 */

anum returns [string result]
 : ANUM
   { result = $ANUM.text }
   { if result[0] == '`': result = result[1:-1] }
 ;
 
 
AND:       ('A'|'a')('N'|'n')('D'|'d');
AS:        ('A'|'a')('S'|'s');
BY:        ('B'|'b')('Y'|'y');
CREATE:    ('C'|'c')('R'|'r')('E'|'e')('A'|'a')('T'|'t')('E'|'e');
DELETE:    ('D'|'d')('E'|'e')('L'|'l')('E'|'e')('T'|'t')('E'|'e');
DISTINCT:  ('D'|'d')('I'|'i')('S'|'s')('T'|'t')('I'|'i')('N'|'n')('C'|'c')('T'|'t'); 
DROP:      ('D'|'d')('R'|'r')('O'|'o')('P'|'p');
DSTREAM:   ('D'|'d')('S'|'s')('T'|'t')('R'|'r')('E'|'e')('A'|'a')('M'|'m');
FALSE:     ('F'|'f')('A'|'a')('L'|'l')('S'|'s')('E'|'e');
FROM:      ('F'|'f')('R'|'r')('O'|'o')('M'|'m');
GROUP:     ('G'|'g')('R'|'r')('O'|'o')('U'|'u')('P'|'p');
HAVING:    ('H'|'h')('A'|'a')('V'|'v')('I'|'i')('N'|'n')('G'|'g');
HOURS:     ('H'|'h')('O'|'o')('U'|'u')('R'|'r')('S'|'s');
INPUT:     ('I'|'i')('N'|'n')('P'|'p')('U'|'u')('T'|'t');
INSERT:    ('I'|'i')('N'|'n')('S'|'s')('E'|'e')('R'|'r')('T'|'t');
INTO:      ('I'|'i')('N'|'n')('T'|'t')('O'|'o');
IS:        ('I'|'i')('S'|'s');
ISTREAM:   ('I'|'i')('S'|'s')('T'|'t')('R'|'r')('E'|'e')('A'|'a')('M'|'m');
JOIN:      ('J'|'j')('O'|'o')('I'|'i')('N'|'n');
KEY:       ('K'|'k')('E'|'e')('Y'|'y');
LEFT:      ('L'|'l')('E'|'e')('F'|'f')('T'|'t');
MINUTES:   ('M'|'m')('I'|'i')('N'|'n')('U'|'u')('T'|'t')('E'|'e')('S'|'s');
NOT:       ('N'|'n')('O'|'o')('T'|'t');
NOW:       ('N'|'n')('O'|'o')('W'|'w');    
NULL:      ('N'|'n')('U'|'u')('L'|'l')('L'|'l');
ON:        ('O'|'o')('N'|'n');
OR:        ('O'|'o')('R'|'r');
OUTER:     ('O'|'o')('U'|'u')('T'|'t')('E'|'e')('R'|'r');
OUTPUT:    ('O'|'o')('U'|'u')('T'|'t')('P'|'p')('U'|'u')('T'|'t');
PARTITION: ('P'|'p')('A'|'a')('R'|'r')('T'|'t')('I'|'i')('T'|'t')('I'|'i')('O'|'o')('N'|'n');
RANGE:     ('R'|'r')('A'|'a')('N'|'n')('G'|'g')('E'|'e');
RIGHT:     ('R'|'r')('I'|'i')('G'|'g')('H'|'h')('T'|'t');
RSTREAM:   ('R'|'r')('S'|'s')('T'|'t')('R'|'r')('E'|'e')('A'|'a')('M'|'m');
ROWS:      ('R'|'r')('O'|'o')('W'|'w')('S'|'s');
SECONDS:   ('S'|'s')('E'|'e')('C'|'c')('O'|'o')('N'|'n')('D'|'d')('S'|'s');
SELECT:    ('S'|'s')('E'|'e')('L'|'l')('E'|'e')('C'|'c')('T'|'t');
SET:       ('S'|'s')('E'|'e')('T'|'t');
STREAM:    ('S'|'s')('T'|'t')('R'|'r')('E'|'e')('A'|'a')('M'|'m');
TABLE:     ('T'|'t')('A'|'a')('B'|'b')('L'|'l')('E'|'e');
TRUE:      ('T'|'t')('R'|'r')('U'|'u')('E'|'e');
UNBOUNDED: ('U'|'u')('N'|'n')('B'|'b')('O'|'o')('U'|'u')('N'|'n')('D'|'d')('E'|'e')('D'|'d');
UPDATE:    ('U'|'u')('P'|'p')('D'|'d')('A'|'a')('T'|'t')('E'|'e');
WHERE:     ('W'|'w')('H'|'h')('E'|'e')('R'|'r')('E'|'e');

MINUS:   '-';
PLUS:    '+';
STAR:    '*';
SLASH:   '/';
DOT:     '.';
DOTDOT:  '..';
AT:      '@';
PERCENT: '%';

COMMENTS: '#' .* '\n' { $channel=HIDDEN; }; 
WS: (' ' | '\t' |'\n' |'\r' )+ { $channel=HIDDEN; }; // ignore whitespace
FLOAT: ('0'..'9')+ '.' ('0'..'9')*;
NUM: ('0'..'9')+;
ANUM
  : ('_'|'a'..'z'|'A'..'Z'|'0'..'9')+
  | '`' ( '\\' . | ~('\\'|'\`') )* '`'
  ;

STR:  '\'' ( '\\' . | ~('\\'|'\'') )* '\'';
DSTR: '"' ( '\\' . | ~('\\'|'"') )* '"';
