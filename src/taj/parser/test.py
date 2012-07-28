
from taj.expr import Expression, Integer, Float, NullConstant, String, Summ, \
    Product, Function
from taj.logic import Conjunction, Disjunction, Comparaison, Boolean, IsNull
from taj.parser.stmt import SelectStatement, SimpleRelation, Rename, \
    StreamCreationStatement, TableCreationStatement, UpdateStatement, \
    InsertStatement
from taj.parser.visitor import CompositeVisitor, IsKeyValidator
from taj.path import IdxAccess, Path
import antlr3
import unittest
from MFQLLexer import MFQLLexer
from MFQLParser import MFQLParser, SyntaxError


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def parse(self, rule, inputStr):
        char_stream = antlr3.ANTLRStringStream(inputStr)
        lexer = MFQLLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = MFQLParser(tokens)
        
        rule = getattr(parser, rule)
        result = rule()
        parser.eof()
        
        validator = CompositeVisitor()
        validator.addComponent(IsKeyValidator())

        if isinstance(result, list):
            for elem in result:
                elem.walk(validator)
        else:
            result.walk(validator)
        
        return result

    def testConstants(self):
        intVal = self.parse('constant', '-1')
        self.assertTrue(isinstance(intVal, Integer))
        self.assertTrue(intVal.getValue() == -1)
        
        floatVal = self.parse('constant', '1.2')
        self.assertTrue(isinstance(floatVal, Float))
        # yes I know about floatVal comparaison
        self.assertTrue(floatVal.getValue() == 1.2)
        
        boolVal = self.parse('constant', 'TRUE')
        self.assertTrue(isinstance(boolVal, Boolean))
        self.assertTrue(boolVal.getValue())
        
        string = self.parse('constant', "'BLA\"'")
        self.assertTrue(isinstance(string, String))
        self.assertTrue(string.getValue() == 'BLA"')

        string = self.parse('constant', '"BLA\'"')
        self.assertTrue(isinstance(string, String))
        self.assertTrue(string.getValue() == "BLA'")
        
        string = self.parse('constant', "'a\\nb'")
        self.assertTrue('\n' in string.getValue())
        
        null = self.parse('constant', 'NULL')
        self.assertTrue(isinstance(null, NullConstant))
        self.assertTrue(null.getValue() is None)
    
    def testBasicExpressions(self):
        
        expr = self.parse('expr', '`a%b`')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Path))
        self.assertTrue(len(expr.getMembers())==1)
        self.assertTrue(expr.getMembers()[0].getAttributeName() == 'a%b')

        expr = self.parse('expr', 'a+2')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Summ))
        self.assertTrue(len(expr.getMembers())==2)
        
        expr = self.parse('expr', '1-2')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Summ))
        self.assertTrue(len(expr.getMembers())==2)
        
        expr = self.parse('expr', '1%2')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Product))
        self.assertTrue(len(expr.getMembers())==2)
        
        expr = self.parse('expr', '1*2/3')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Product))
        self.assertTrue(len(expr.getMembers())==3)
        
        expr = self.parse('expr', '1-3*5')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Summ))
        members = expr.getMembers()
        self.assertTrue(isinstance(members[0][1], Integer))
        self.assertTrue(isinstance(members[1][1], Product))
        self.assertTrue(len(members[1][1].getMembers())==2)

        expr = self.parse('expr', '(1-3)*5')
        self.assertTrue(expr is not None)
        self.assertTrue(isinstance(expr, Product))
        members = expr.getMembers()
        self.assertTrue(isinstance(members[0][1], Summ))
        self.assertTrue(isinstance(members[1][1], Integer))
        self.assertTrue(len(members[0][1].getMembers())==2)
        
        expr = self.parse('predicate', '(1+2)+3 = 1')
        self.assertTrue(isinstance(expr, Comparaison))
        self.assertTrue(isinstance(expr.getLValue(),Summ))
        (_, expr) = expr.getLValue().getMembers()[0]
        self.assertTrue(isinstance(expr, Summ))
    
    def testFunctions(self):

        expr = self.parse('expr', 'f(1+2)')
        self.assertTrue(isinstance(expr, Function))
        args = expr.getArguments()
        self.assertTrue(isinstance(args, list))
        self.assertTrue(len(args)==1)
        self.assertTrue(isinstance(args[0], Summ))
        
        expr = self.parse('expr', 'f(1+2, 2)')
        self.assertTrue(isinstance(expr, Function))
        args = expr.getArguments()
        self.assertTrue(isinstance(args, list))
        self.assertTrue(len(args)==2)
        self.assertTrue(isinstance(args[0], Summ))
        self.assertTrue(isinstance(args[1], Integer))
        
    def testLogic(self):
        
        expr = self.parse('predicate', 'a.b IS NULL')
        self.assertTrue(isinstance(expr, IsNull))
        #print expr.getExpression()
        
        expr = self.parse('predicate', 'a IS KEY')
        
        expr = self.parse('predicate', '1=2')
        #print expr

        expr = self.parse('predicate', '(1=2)')
        #print expr

        expr = self.parse('predicate', '1>2 AND 1=2')
        #print expr

        expr = self.parse('predicate', 'NOT 1>2 OR 1=2 AND a=b')
        #print expr

        expr = self.parse('predicate', '(1+2)=3 OR 1=2 AND a=b')
        #print expr

        exc = False
        try:
            self.parse('predicate', 'a+1 IS KEY')
        except SyntaxError:
            exc = True
        self.assertTrue(exc, 'expr may not be used as isKey predicate')

    def testPaths(self):
        path = self.parse('path', '.')
        self.assertTrue(path is not None)
        self.assertTrue(len(path.getMembers())==0)
        
        path = self.parse('path', 'store')
        self.assertTrue(path is not None)
        members = path.getMembers()
        self.assertTrue(len(members)==1)
        self.assertTrue(members[0].getAttributeName()=='store')
        
        path = self.parse('path', '.store')
        self.assertTrue(path is not None)
        members = path.getMembers()
        self.assertTrue(len(members)==1)
        self.assertTrue(members[0].getAttributeName()=='store')
        
        path = self.parse('path', 'store.book')
        self.assertTrue(path is not None)
        members = path.getMembers()
        self.assertTrue(len(members)==2)
        self.assertTrue(map(lambda x: x.getAttributeName(), members) == [u'store', u'book'])

        self.assertTrue(self.parse('path', '.store.book') is not None)

        path = self.parse('path', 'store.book[2]')
        self.assertTrue(path is not None)
        members = path.getMembers()
        self.assertTrue(len(members)==3)
        self.assertTrue(isinstance(members[2], IdxAccess))
        self.assertTrue(members[2].getIndex()==2)
        
        path = self.parse('path', '.[2]')
        self.assertTrue(path is not None)
        members = path.getMembers()
        self.assertTrue(len(members)==1)
        self.assertTrue(isinstance(members[0], IdxAccess))
        self.assertTrue(members[0].getIndex()==2)
        
        self.assertTrue(self.parse('path', 'store.book[-1]') is not None)
        self.assertTrue(self.parse('path', 'store.book[2].title') is not None)
        
        exc = False
        try:
            self.parse('path', '.store.book[*].author')
        except SyntaxError:
            exc = True
        self.assertTrue(exc, 'selector is not a path')
        
        exc = False
        try:
            self.parse('path', '')
        except SyntaxError:
            exc = True
        self.assertTrue(exc, 'empty path is not valid')
        
        exc = False
        try:
            self.parse('path', '[1]')
        except SyntaxError:
            exc = True
        self.assertTrue(exc, 'not valid')
        
    def testBasicPattern(self):
        pat = self.parse('expr', 'null')
        self.assertTrue(isinstance(pat, NullConstant))
        
        pat = self.parse('expr', '1')
        self.assertTrue(isinstance(pat, Integer))
        self.assertTrue(pat.getValue()==1)
        
        pat = self.parse('expr', '1.3')
        self.assertTrue(isinstance(pat, Float))
        self.assertTrue(pat.getValue() == 1.3)

        pat = self.parse('expr', '"hello"')
        self.assertTrue(isinstance(pat, String))
        self.assertTrue(pat.getValue() == 'hello')

        # logic is not allowed in patterns for now
        #self.assertTrue(self.parse('pattern', 'true') is not None)
        self.assertTrue(self.parse('expr', '[]') is not None)
        self.assertTrue(self.parse('expr', '{}') is not None)

#    def testSelectors(self):
#        
#        self.assertTrue(self.parse('selector', '.') is not None)
#        self.assertTrue(self.parse('selector', 'store') is not None)
#        self.assertTrue(self.parse('selector', '.store') is not None)
#        self.assertTrue(self.parse('selector', '..store') is not None)
#        self.assertTrue(self.parse('selector', 'store.book') is not None)
#        self.assertTrue(self.parse('selector', '.store.book') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[2]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[store.bla]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[-1]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[1:3]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[:3]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[1:3:2]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[2].title') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[*].author') is not None)
#        self.assertTrue(self.parse('selector', '.[..author IS KEY]') is not None)
#        self.assertTrue(self.parse('selector', '.store.*') is not None)
#        self.assertTrue(self.parse('selector', '.store[..price is key]') is not None)
#        self.assertTrue(self.parse('selector', '.[@..book[2] is null]') is not None)
#        self.assertTrue(self.parse('selector', '.book[0,3]') is not None)
#        self.assertTrue(self.parse('selector', '.[..book[@.isbn] is key]') is not None)
#        self.assertTrue(self.parse('selector', '.book[@.price<10]') is not None)
#        
#        self.assertTrue(self.parse('selector', '.store.book[ @.price>10 and @.price<20]') is not None)
#        self.assertTrue(self.parse('selector', '.store.book[ @.price<10, @.price>20]') is not None)
#
#        self.assertTrue(self.parse('selector', '.store.book[.length<10]') is not None)

    def testBasicOperation(self):
        
        result = self.parse('stmts', 'SELECT * FROM bla;')
        self.assertTrue(result is not None)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(isinstance(result[0], SelectStatement))

    def testBasicSelect(self):
        
        result = self.parse('stmts', '''
          SELECT * FROM bla;
        ''')
        self.assertTrue(result is not None);
        
        stmt = result[0]
        self.assertTrue(isinstance(stmt, SelectStatement))
        
        src = stmt.getSource()
        self.assertTrue(isinstance(src, SimpleRelation))
        self.assertTrue(src.getName() == 'bla')
        
        projs = stmt.getProjections()
        self.assertTrue(isinstance(projs, list))
        self.assertTrue(len(projs) == 0)
    
    def testRenaming(self):
        result = self.parse('stmts', 'SELECT a AS b, b AS c, c AS d FROM bla;')
        stmt = result[0]
        self.assertTrue(isinstance(stmt, SelectStatement))

        projs = stmt.getProjections()
        self.assertTrue((projs is not None) and isinstance(projs, list))
        
        for proj in projs:
            self.assertTrue((proj is not None) and isinstance(proj, Rename))
            newName = proj.getNewName()
            self.assertTrue((newName is not None) and isinstance(newName, Path))
            expr    = proj.getExpression()
            self.assertTrue((expr is not None) and isinstance(expr, Expression))
            self.assertTrue(isinstance(expr, Path))
    
    def testExpression(self):
        
        result = self.parse('stmts', """
          SELECT
            *
          FROM t
          WHERE
              'BLA'='BLUP' OR 1<>2
            AND
              FUNC(1)><8
          ;
        """)
        self.assertTrue(result is not None);
        stmt = result[0]
        pred = stmt.getSelection()
        
        self.assertTrue(isinstance(pred, Conjunction))
        members = pred.getMembers()
        self.assertTrue(isinstance(members[0], Disjunction))
        self.assertTrue(isinstance(members[1], Comparaison))
        
        members = members[0].getMembers()
        self.assertTrue(isinstance(members[0], Comparaison))
        self.assertTrue(isinstance(members[1], Comparaison))
        

    def testCreateInputStream(self):
    
        result = self.parse('stmts', ''' 
          CREATE INPUT STREAM stdin (
            file         = '/dev/stdin',
            adapter      = 'CSV',
            synchronized = FALSE,
            schema       = (
              a = 'INT',
              b = 'INT'
            )
          );''')
        self.assertTrue(result is not None)
        stmt = result[0]
        self.assertTrue(isinstance(stmt, StreamCreationStatement))
        self.assertTrue(stmt.getType()==StreamCreationStatement.INPUT)
        
        for key in ['file', 'adapter', 'synchronized', 'schema']:
            self.assertTrue(stmt.getOptions().has_key(key))
        
    def testCreateOutputStream(self):
        result = self.parse('stmts', ''' 
          CREATE OUTPUT STREAM stdout (
            file         = '/dev/stdout',
            adapter      = 'CSV',
            synchronized = FALSE  
          );
        ''')
        self.assertTrue(result is not None)
        stmt = result[0]
        self.assertTrue(isinstance(stmt, StreamCreationStatement))
        self.assertTrue(stmt.getType()==StreamCreationStatement.OUTPUT)
    
    def testBasicCreateTable(self):
        result = self.parse('stmts', ''' 
          CREATE TABLE buffer AS SELECT * FROM stdin;''')
        self.assertTrue(result is not None)
        stmt = result[0]
        self.assertTrue(isinstance(stmt, TableCreationStatement))

    def testBasicUpdate(self):
        result = self.parse('stmts', 'UPDATE buffer SET a = 1 WHERE b = 2;');
        self.assertTrue(result is not None)
        stmt = result[0]
        self.assertTrue(isinstance(stmt, UpdateStatement))

#    def testUpdateDrop(self):
#        result = self.parse('stmts', 'UPDATE buffer SET a = 1 DROP c WHERE b = 2;')

    def testBasicInsert(self):
        result = self.parse('stmts', 'INSERT INTO stdout SELECT * FROM buff;')
        self.assertTrue(result is not None)
        stmt = result[0]
        self.assertTrue(isinstance(stmt, InsertStatement))
    
    def testPatterns(self):
        result = self.parse('stmts', 'SELECT [] AS ., {"a":1} AS .[0] FROM buff;')
        self.assertTrue(result is not None)
        stmt = result[0]
        print "SELECT %s" % stmt
    
    def testWindow(self):
        result = self.parse('stmts', '''
          SELECT
            RSTREAM(*)
          FROM PosSpeedStr [NOW];
        ''')
        self.assertTrue(result is not None)
    
    def testJoin(self):
        
#        result = self.parse('stmts', '''
#          SELECT
#            *
#          FROM
#            table1 AS t1,
#            stream1[ROWS 10] AS t1.bla,
#            stream2[NOW] AS blup;
#        ''')
        pass
    
#    def testGroupBy(self):
#        result = self.parse('stmts', '''
#          SELECT SUM(a) FROM table1 GROUP BY b; 
#        ''')

if __name__ == "__main__":
    unittest.main()
