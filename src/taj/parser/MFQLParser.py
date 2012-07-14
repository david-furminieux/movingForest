# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 MFQL.g 2011-04-01 00:04:05

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         

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




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__68=68
T__69=69
T__66=66
WHERE=15
T__67=67
T__64=64
STAR=16
T__65=65
T__62=62
T__63=63
ISTREAM=11
DSTR=38
INPUT=6
TABLE=5
UPDATE=19
SECONDS=30
NOW=27
DOTDOT=58
FLOAT=40
NOT=47
AND=45
EOF=-1
AT=59
STR=37
AS=23
CREATE=4
SLASH=42
COMMENTS=60
INSERT=17
IS=48
PARTITION=24
LEFT=54
PLUS=41
DOT=44
STREAM=8
SELECT=9
INTO=18
ANUM=50
OUTER=56
BY=25
PERCENT=43
KEY=49
NULL=39
RSTREAM=13
ON=55
RANGE=28
RIGHT=57
SET=20
HAVING=52
DELETE=22
MINUS=33
TRUE=35
JOIN=53
NUM=34
DSTREAM=12
MINUTES=31
GROUP=51
WS=61
T__71=71
T__72=72
T__70=70
DROP=21
OR=46
ROWS=29
T__76=76
FROM=14
FALSE=36
UNBOUNDED=26
T__75=75
T__74=74
DISTINCT=10
T__73=73
OUTPUT=7
HOURS=32
T__79=79
T__78=78
T__77=77

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "CREATE", "TABLE", "INPUT", "OUTPUT", "STREAM", "SELECT", "DISTINCT", 
    "ISTREAM", "DSTREAM", "RSTREAM", "FROM", "WHERE", "STAR", "INSERT", 
    "INTO", "UPDATE", "SET", "DROP", "DELETE", "AS", "PARTITION", "BY", 
    "UNBOUNDED", "NOW", "RANGE", "ROWS", "SECONDS", "MINUTES", "HOURS", 
    "MINUS", "NUM", "TRUE", "FALSE", "STR", "DSTR", "NULL", "FLOAT", "PLUS", 
    "SLASH", "PERCENT", "DOT", "AND", "OR", "NOT", "IS", "KEY", "ANUM", 
    "GROUP", "HAVING", "JOIN", "LEFT", "ON", "OUTER", "RIGHT", "DOTDOT", 
    "AT", "COMMENTS", "WS", "';'", "'('", "')'", "'='", "','", "'['", "']'", 
    "'{'", "':'", "'}'", "'<'", "'<='", "'=='", "'<>'", "'!='", "'>='", 
    "'>'", "'><'"
]




class MFQLParser(Parser):
    grammarFileName = "MFQL.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(MFQLParser, self).__init__(input, state, *args, **kwargs)

        self.dfa57 = self.DFA57(
            self, 57,
            eot = self.DFA57_eot,
            eof = self.DFA57_eof,
            min = self.DFA57_min,
            max = self.DFA57_max,
            accept = self.DFA57_accept,
            special = self.DFA57_special,
            transition = self.DFA57_transition
            )






                


        

              
    #def displayRecognitionError(self, tokenNames, e):
    #  print tokenNames
    #  print e

    def emitErrorMessage(self, msg):
      raise SyntaxError(msg)



    # $ANTLR start "stmts"
    # MFQL.g:38:1: stmts returns [ list result ] : (s= stmt ';' )+ ;
    def stmts(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:39:3: ( (s= stmt ';' )+ )
                # MFQL.g:39:5: (s= stmt ';' )+
                pass 
                if self._state.backtracking == 0:
                    result = [] 

                # MFQL.g:40:5: (s= stmt ';' )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CREATE or LA1_0 == SELECT or LA1_0 == INSERT or (UPDATE <= LA1_0 <= SET) or LA1_0 == DELETE) :
                        alt1 = 1


                    if alt1 == 1:
                        # MFQL.g:40:6: s= stmt ';'
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_stmts52)
                        s = self.stmt()

                        self._state.following.pop()
                        self.match(self.input, 62, self.FOLLOW_62_in_stmts54)
                        if self._state.backtracking == 0:
                            result.append(s) 



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "stmts"


    # $ANTLR start "stmt"
    # MFQL.g:43:1: stmt returns [ Statement result ] : (s= createStmt | s= selectStmt | s= insertStmt | s= updateStmt | s= deleteStmt | s= globalAssignmentStmt );
    def stmt(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:44:3: (s= createStmt | s= selectStmt | s= insertStmt | s= updateStmt | s= deleteStmt | s= globalAssignmentStmt )
                alt2 = 6
                LA2 = self.input.LA(1)
                if LA2 == CREATE:
                    alt2 = 1
                elif LA2 == SELECT:
                    alt2 = 2
                elif LA2 == INSERT:
                    alt2 = 3
                elif LA2 == UPDATE:
                    alt2 = 4
                elif LA2 == DELETE:
                    alt2 = 5
                elif LA2 == SET:
                    alt2 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # MFQL.g:44:5: s= createStmt
                    pass 
                    self._state.following.append(self.FOLLOW_createStmt_in_stmt77)
                    s = self.createStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt2 == 2:
                    # MFQL.g:45:5: s= selectStmt
                    pass 
                    self._state.following.append(self.FOLLOW_selectStmt_in_stmt97)
                    s = self.selectStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt2 == 3:
                    # MFQL.g:46:5: s= insertStmt
                    pass 
                    self._state.following.append(self.FOLLOW_insertStmt_in_stmt117)
                    s = self.insertStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt2 == 4:
                    # MFQL.g:47:5: s= updateStmt
                    pass 
                    self._state.following.append(self.FOLLOW_updateStmt_in_stmt137)
                    s = self.updateStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt2 == 5:
                    # MFQL.g:48:5: s= deleteStmt
                    pass 
                    self._state.following.append(self.FOLLOW_deleteStmt_in_stmt157)
                    s = self.deleteStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt2 == 6:
                    # MFQL.g:49:5: s= globalAssignmentStmt
                    pass 
                    self._state.following.append(self.FOLLOW_globalAssignmentStmt_in_stmt177)
                    s = self.globalAssignmentStmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "stmt"


    # $ANTLR start "createStmt"
    # MFQL.g:52:1: createStmt returns [CreateStatement result] : CREATE ( TABLE n= name d= tableDef | ( INPUT | OUTPUT ) STREAM n= name d= streamDef ) ;
    def createStmt(self, ):

        result = None

        n = None

        d = None


        try:
            try:
                # MFQL.g:53:3: ( CREATE ( TABLE n= name d= tableDef | ( INPUT | OUTPUT ) STREAM n= name d= streamDef ) )
                # MFQL.g:53:5: CREATE ( TABLE n= name d= tableDef | ( INPUT | OUTPUT ) STREAM n= name d= streamDef )
                pass 
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_createStmt196)
                # MFQL.g:54:5: ( TABLE n= name d= tableDef | ( INPUT | OUTPUT ) STREAM n= name d= streamDef )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TABLE) :
                    alt4 = 1
                elif ((INPUT <= LA4_0 <= OUTPUT)) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # MFQL.g:54:7: TABLE n= name d= tableDef
                    pass 
                    self.match(self.input, TABLE, self.FOLLOW_TABLE_in_createStmt204)
                    self._state.following.append(self.FOLLOW_name_in_createStmt208)
                    n = self.name()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_tableDef_in_createStmt212)
                    d = self.tableDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = TableCreationStatement(n, d) 



                elif alt4 == 2:
                    # MFQL.g:56:7: ( INPUT | OUTPUT ) STREAM n= name d= streamDef
                    pass 
                    # MFQL.g:56:7: ( INPUT | OUTPUT )
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == INPUT) :
                        alt3 = 1
                    elif (LA3_0 == OUTPUT) :
                        alt3 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 3, 0, self.input)

                        raise nvae

                    if alt3 == 1:
                        # MFQL.g:56:9: INPUT
                        pass 
                        self.match(self.input, INPUT, self.FOLLOW_INPUT_in_createStmt230)
                        if self._state.backtracking == 0:
                            type = StreamCreationStatement.INPUT  



                    elif alt3 == 2:
                        # MFQL.g:57:9: OUTPUT
                        pass 
                        self.match(self.input, OUTPUT, self.FOLLOW_OUTPUT_in_createStmt243)
                        if self._state.backtracking == 0:
                            type = StreamCreationStatement.OUTPUT 




                    self.match(self.input, STREAM, self.FOLLOW_STREAM_in_createStmt255)
                    self._state.following.append(self.FOLLOW_name_in_createStmt259)
                    n = self.name()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_streamDef_in_createStmt263)
                    d = self.streamDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = StreamCreationStatement(n, d, type) 








            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "createStmt"


    # $ANTLR start "selectStmt"
    # MFQL.g:63:1: selectStmt returns [SelectStatement result] : SELECT ( DISTINCT )? (l= attrSel | ISTREAM '(' l= attrSel ')' | DSTREAM '(' l= attrSel ')' | RSTREAM '(' l= attrSel ')' ) FROM r= relation ( WHERE r= whereRestriction )? ;
    def selectStmt(self, ):

        result = None

        l = None

        r = None


        try:
            try:
                # MFQL.g:64:3: ( SELECT ( DISTINCT )? (l= attrSel | ISTREAM '(' l= attrSel ')' | DSTREAM '(' l= attrSel ')' | RSTREAM '(' l= attrSel ')' ) FROM r= relation ( WHERE r= whereRestriction )? )
                # MFQL.g:64:5: SELECT ( DISTINCT )? (l= attrSel | ISTREAM '(' l= attrSel ')' | DSTREAM '(' l= attrSel ')' | RSTREAM '(' l= attrSel ')' ) FROM r= relation ( WHERE r= whereRestriction )?
                pass 
                self.match(self.input, SELECT, self.FOLLOW_SELECT_in_selectStmt294)
                if self._state.backtracking == 0:
                    result = SelectStatement() 

                # MFQL.g:66:5: ( DISTINCT )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == DISTINCT) :
                    alt5 = 1
                if alt5 == 1:
                    # MFQL.g:66:6: DISTINCT
                    pass 
                    self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_selectStmt307)
                    if self._state.backtracking == 0:
                        result.setDistinct(True) 




                # MFQL.g:67:5: (l= attrSel | ISTREAM '(' l= attrSel ')' | DSTREAM '(' l= attrSel ')' | RSTREAM '(' l= attrSel ')' )
                alt6 = 4
                LA6 = self.input.LA(1)
                if LA6 == STAR or LA6 == MINUS or LA6 == NUM or LA6 == STR or LA6 == DSTR or LA6 == NULL or LA6 == FLOAT or LA6 == DOT or LA6 == ANUM or LA6 == 63 or LA6 == 67 or LA6 == 69:
                    alt6 = 1
                elif LA6 == ISTREAM:
                    alt6 = 2
                elif LA6 == DSTREAM:
                    alt6 = 3
                elif LA6 == RSTREAM:
                    alt6 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # MFQL.g:67:7: l= attrSel
                    pass 
                    self._state.following.append(self.FOLLOW_attrSel_in_selectStmt323)
                    l = self.attrSel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream = Stream.NONE     



                elif alt6 == 2:
                    # MFQL.g:68:7: ISTREAM '(' l= attrSel ')'
                    pass 
                    self.match(self.input, ISTREAM, self.FOLLOW_ISTREAM_in_selectStmt350)
                    self.match(self.input, 63, self.FOLLOW_63_in_selectStmt352)
                    self._state.following.append(self.FOLLOW_attrSel_in_selectStmt356)
                    l = self.attrSel()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_selectStmt358)
                    if self._state.backtracking == 0:
                        stream = Stream.INSERT   



                elif alt6 == 3:
                    # MFQL.g:69:7: DSTREAM '(' l= attrSel ')'
                    pass 
                    self.match(self.input, DSTREAM, self.FOLLOW_DSTREAM_in_selectStmt368)
                    self.match(self.input, 63, self.FOLLOW_63_in_selectStmt370)
                    self._state.following.append(self.FOLLOW_attrSel_in_selectStmt374)
                    l = self.attrSel()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_selectStmt376)
                    if self._state.backtracking == 0:
                        stream = Stream.DELETE   



                elif alt6 == 4:
                    # MFQL.g:70:7: RSTREAM '(' l= attrSel ')'
                    pass 
                    self.match(self.input, RSTREAM, self.FOLLOW_RSTREAM_in_selectStmt386)
                    self.match(self.input, 63, self.FOLLOW_63_in_selectStmt388)
                    self._state.following.append(self.FOLLOW_attrSel_in_selectStmt392)
                    l = self.attrSel()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_selectStmt394)
                    if self._state.backtracking == 0:
                        stream = Stream.RELATION 




                if self._state.backtracking == 0:
                    result.setProjections(l) 

                if self._state.backtracking == 0:
                    result.setStreamingOp(stream) 

                self.match(self.input, FROM, self.FOLLOW_FROM_in_selectStmt420)
                self._state.following.append(self.FOLLOW_relation_in_selectStmt424)
                r = self.relation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.setSource(r) 

                # MFQL.g:75:5: ( WHERE r= whereRestriction )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == WHERE) :
                    alt7 = 1
                if alt7 == 1:
                    # MFQL.g:75:6: WHERE r= whereRestriction
                    pass 
                    self.match(self.input, WHERE, self.FOLLOW_WHERE_in_selectStmt433)
                    self._state.following.append(self.FOLLOW_whereRestriction_in_selectStmt437)
                    r = self.whereRestriction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result.setSelection(r) 








            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "selectStmt"


    # $ANTLR start "attrSel"
    # MFQL.g:80:1: attrSel returns [list result] : ( STAR | list= renamedAttrList );
    def attrSel(self, ):

        result = None

        list = None


        try:
            try:
                # MFQL.g:81:3: ( STAR | list= renamedAttrList )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == STAR) :
                    alt8 = 1
                elif ((MINUS <= LA8_0 <= NUM) or (STR <= LA8_0 <= FLOAT) or LA8_0 == DOT or LA8_0 == ANUM or LA8_0 == 63 or LA8_0 == 67 or LA8_0 == 69) :
                    alt8 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # MFQL.g:81:5: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_attrSel460)
                    if self._state.backtracking == 0:
                        result = []   



                elif alt8 == 2:
                    # MFQL.g:82:5: list= renamedAttrList
                    pass 
                    self._state.following.append(self.FOLLOW_renamedAttrList_in_attrSel486)
                    list = self.renamedAttrList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = list 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "attrSel"


    # $ANTLR start "insertStmt"
    # MFQL.g:85:1: insertStmt returns [InsertStatement result] : INSERT INTO r= simpleRelation s= selectStmt ;
    def insertStmt(self, ):

        result = None

        r = None

        s = None


        try:
            try:
                # MFQL.g:86:3: ( INSERT INTO r= simpleRelation s= selectStmt )
                # MFQL.g:86:5: INSERT INTO r= simpleRelation s= selectStmt
                pass 
                self.match(self.input, INSERT, self.FOLLOW_INSERT_in_insertStmt509)
                self.match(self.input, INTO, self.FOLLOW_INTO_in_insertStmt511)
                self._state.following.append(self.FOLLOW_simpleRelation_in_insertStmt519)
                r = self.simpleRelation()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_selectStmt_in_insertStmt527)
                s = self.selectStmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = InsertStatement(); result.setTarget(r) 

                if self._state.backtracking == 0:
                    result.setSource(s) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "insertStmt"


    # $ANTLR start "updateStmt"
    # MFQL.g:93:1: updateStmt returns [UpdateStatement result] : UPDATE rel= simpleRelation ( SET l= modifOrders | DROP l= dropOrders )+ ( WHERE res= whereRestriction )? ;
    def updateStmt(self, ):

        result = None

        rel = None

        l = None

        res = None


        try:
            try:
                # MFQL.g:94:3: ( UPDATE rel= simpleRelation ( SET l= modifOrders | DROP l= dropOrders )+ ( WHERE res= whereRestriction )? )
                # MFQL.g:94:5: UPDATE rel= simpleRelation ( SET l= modifOrders | DROP l= dropOrders )+ ( WHERE res= whereRestriction )?
                pass 
                self.match(self.input, UPDATE, self.FOLLOW_UPDATE_in_updateStmt560)
                self._state.following.append(self.FOLLOW_simpleRelation_in_updateStmt564)
                rel = self.simpleRelation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    orders = [] 

                # MFQL.g:96:5: ( SET l= modifOrders | DROP l= dropOrders )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == SET) :
                        alt9 = 1
                    elif (LA9_0 == DROP) :
                        alt9 = 2


                    if alt9 == 1:
                        # MFQL.g:97:7: SET l= modifOrders
                        pass 
                        self.match(self.input, SET, self.FOLLOW_SET_in_updateStmt585)
                        self._state.following.append(self.FOLLOW_modifOrders_in_updateStmt590)
                        l = self.modifOrders()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            orders.extend(l) 



                    elif alt9 == 2:
                        # MFQL.g:98:7: DROP l= dropOrders
                        pass 
                        self.match(self.input, DROP, self.FOLLOW_DROP_in_updateStmt603)
                        self._state.following.append(self.FOLLOW_dropOrders_in_updateStmt607)
                        l = self.dropOrders()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            orders.extend(l) 



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                # MFQL.g:100:5: ( WHERE res= whereRestriction )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == WHERE) :
                    alt10 = 1
                if alt10 == 1:
                    # MFQL.g:100:6: WHERE res= whereRestriction
                    pass 
                    self.match(self.input, WHERE, self.FOLLOW_WHERE_in_updateStmt625)
                    self._state.following.append(self.FOLLOW_whereRestriction_in_updateStmt629)
                    res = self.whereRestriction()

                    self._state.following.pop()



                if self._state.backtracking == 0:
                    result = UpdateStatement()    

                if self._state.backtracking == 0:
                    result.setTarget(rel)         

                if self._state.backtracking == 0:
                    result.setAlterations(orders) 

                if self._state.backtracking == 0:
                    result.setSelection(res)      





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "updateStmt"


    # $ANTLR start "deleteStmt"
    # MFQL.g:107:1: deleteStmt returns [DeleteStatement result] : DELETE FROM rel= simpleRelOrStr ( WHERE res= whereRestriction )? ;
    def deleteStmt(self, ):

        result = None

        rel = None

        res = None


        try:
            try:
                # MFQL.g:108:3: ( DELETE FROM rel= simpleRelOrStr ( WHERE res= whereRestriction )? )
                # MFQL.g:108:5: DELETE FROM rel= simpleRelOrStr ( WHERE res= whereRestriction )?
                pass 
                self.match(self.input, DELETE, self.FOLLOW_DELETE_in_deleteStmt672)
                self.match(self.input, FROM, self.FOLLOW_FROM_in_deleteStmt674)
                self._state.following.append(self.FOLLOW_simpleRelOrStr_in_deleteStmt682)
                rel = self.simpleRelOrStr()

                self._state.following.pop()
                # MFQL.g:110:5: ( WHERE res= whereRestriction )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == WHERE) :
                    alt11 = 1
                if alt11 == 1:
                    # MFQL.g:110:6: WHERE res= whereRestriction
                    pass 
                    self.match(self.input, WHERE, self.FOLLOW_WHERE_in_deleteStmt689)
                    self._state.following.append(self.FOLLOW_whereRestriction_in_deleteStmt693)
                    res = self.whereRestriction()

                    self._state.following.pop()



                if self._state.backtracking == 0:
                    result = DeleteStatement() 

                if self._state.backtracking == 0:
                    result.setTarget(rel)      

                if self._state.backtracking == 0:
                    result.setSelection(res)   





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "deleteStmt"


    # $ANTLR start "globalAssignmentStmt"
    # MFQL.g:116:1: globalAssignmentStmt returns [AssignmentStatement result] : SET n= name '=' c= constant ;
    def globalAssignmentStmt(self, ):

        result = None

        n = None

        c = None


        try:
            try:
                # MFQL.g:117:3: ( SET n= name '=' c= constant )
                # MFQL.g:117:5: SET n= name '=' c= constant
                pass 
                self.match(self.input, SET, self.FOLLOW_SET_in_globalAssignmentStmt730)
                self._state.following.append(self.FOLLOW_name_in_globalAssignmentStmt734)
                n = self.name()

                self._state.following.pop()
                self.match(self.input, 65, self.FOLLOW_65_in_globalAssignmentStmt736)
                self._state.following.append(self.FOLLOW_constant_in_globalAssignmentStmt740)
                c = self.constant()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = AssignmentStatement() 

                if self._state.backtracking == 0:
                    result.setName(n)              

                if self._state.backtracking == 0:
                    result.setValue(c)             





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "globalAssignmentStmt"


    # $ANTLR start "modifOrders"
    # MFQL.g:123:1: modifOrders returns [list result] : o= modifOrder ( ',' o= modifOrder )* ;
    def modifOrders(self, ):

        result = None

        o = None


        try:
            try:
                # MFQL.g:124:3: (o= modifOrder ( ',' o= modifOrder )* )
                # MFQL.g:124:5: o= modifOrder ( ',' o= modifOrder )*
                pass 
                if self._state.backtracking == 0:
                    result = [] 

                self._state.following.append(self.FOLLOW_modifOrder_in_modifOrders783)
                o = self.modifOrder()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.append(o) 

                # MFQL.g:126:5: ( ',' o= modifOrder )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 66) :
                        alt12 = 1


                    if alt12 == 1:
                        # MFQL.g:126:7: ',' o= modifOrder
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_modifOrders793)
                        self._state.following.append(self.FOLLOW_modifOrder_in_modifOrders797)
                        o = self.modifOrder()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.append(o) 



                    else:
                        break #loop12




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "modifOrders"


    # $ANTLR start "dropOrders"
    # MFQL.g:129:1: dropOrders returns [list result] : p= path ( ',' p= path )* ;
    def dropOrders(self, ):

        result = None

        p = None


        try:
            try:
                # MFQL.g:130:3: (p= path ( ',' p= path )* )
                # MFQL.g:130:5: p= path ( ',' p= path )*
                pass 
                if self._state.backtracking == 0:
                    result = [] 

                self._state.following.append(self.FOLLOW_path_in_dropOrders827)
                p = self.path()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.append(DropRequest(p)) 

                # MFQL.g:132:5: ( ',' p= path )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 66) :
                        alt13 = 1


                    if alt13 == 1:
                        # MFQL.g:132:7: ',' p= path
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_dropOrders837)
                        self._state.following.append(self.FOLLOW_path_in_dropOrders841)
                        p = self.path()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.append(DropRequest(p)) 



                    else:
                        break #loop13




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "dropOrders"


    # $ANTLR start "modifOrder"
    # MFQL.g:135:1: modifOrder returns [AlterRequest result] : p= path '=' e= expr ;
    def modifOrder(self, ):

        result = None

        p = None

        e = None


        try:
            try:
                # MFQL.g:136:3: (p= path '=' e= expr )
                # MFQL.g:136:5: p= path '=' e= expr
                pass 
                self._state.following.append(self.FOLLOW_path_in_modifOrder871)
                p = self.path()

                self._state.following.pop()
                self.match(self.input, 65, self.FOLLOW_65_in_modifOrder873)
                self._state.following.append(self.FOLLOW_expr_in_modifOrder877)
                e = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = AlterRequest(p, e) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "modifOrder"


    # $ANTLR start "streamDef"
    # MFQL.g:139:1: streamDef returns [dict result] : '(' s= optionStruct ')' ;
    def streamDef(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:140:3: ( '(' s= optionStruct ')' )
                # MFQL.g:140:5: '(' s= optionStruct ')'
                pass 
                self.match(self.input, 63, self.FOLLOW_63_in_streamDef896)
                self._state.following.append(self.FOLLOW_optionStruct_in_streamDef900)
                s = self.optionStruct()

                self._state.following.pop()
                self.match(self.input, 64, self.FOLLOW_64_in_streamDef902)
                if self._state.backtracking == 0:
                    result = s 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "streamDef"


    # $ANTLR start "tableDef"
    # MFQL.g:143:1: tableDef returns [Integer result] : AS s= selectStmt ;
    def tableDef(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:144:3: ( AS s= selectStmt )
                # MFQL.g:144:5: AS s= selectStmt
                pass 
                self.match(self.input, AS, self.FOLLOW_AS_in_tableDef925)
                self._state.following.append(self.FOLLOW_selectStmt_in_tableDef929)
                s = self.selectStmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = s 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "tableDef"


    # $ANTLR start "whereRestriction"
    # MFQL.g:147:1: whereRestriction returns [Predicate result] : p= predicate ;
    def whereRestriction(self, ):

        result = None

        p = None


        try:
            try:
                # MFQL.g:148:3: (p= predicate )
                # MFQL.g:148:5: p= predicate
                pass 
                self._state.following.append(self.FOLLOW_predicate_in_whereRestriction950)
                p = self.predicate()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = p 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "whereRestriction"


    # $ANTLR start "renamedAttrList"
    # MFQL.g:151:1: renamedAttrList returns [list result] : e= expr ( AS p= path )? ( ',' e= expr ( AS p= path )? )* ;
    def renamedAttrList(self, ):

        result = None

        e = None

        p = None


        try:
            try:
                # MFQL.g:152:3: (e= expr ( AS p= path )? ( ',' e= expr ( AS p= path )? )* )
                # MFQL.g:152:6: e= expr ( AS p= path )? ( ',' e= expr ( AS p= path )? )*
                pass 
                if self._state.backtracking == 0:
                    result = []; count=1 

                self._state.following.append(self.FOLLOW_expr_in_renamedAttrList979)
                e = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    newName = None 

                # MFQL.g:154:6: ( AS p= path )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == AS) :
                    alt14 = 1
                if alt14 == 1:
                    # MFQL.g:154:7: AS p= path
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_renamedAttrList989)
                    self._state.following.append(self.FOLLOW_path_in_renamedAttrList993)
                    p = self.path()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        newName = p 




                if self._state.backtracking == 0:
                    if newName is None: newName = createSinglePath('var1') 

                if self._state.backtracking == 0:
                    result.append(Rename(e, newName)) 

                # MFQL.g:157:6: ( ',' e= expr ( AS p= path )? )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 66) :
                        alt16 = 1


                    if alt16 == 1:
                        # MFQL.g:158:8: ',' e= expr ( AS p= path )?
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_renamedAttrList1027)
                        self._state.following.append(self.FOLLOW_expr_in_renamedAttrList1031)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            newName = None; count += 1 

                        # MFQL.g:159:8: ( AS p= path )?
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == AS) :
                            alt15 = 1
                        if alt15 == 1:
                            # MFQL.g:159:9: AS p= path
                            pass 
                            self.match(self.input, AS, self.FOLLOW_AS_in_renamedAttrList1043)
                            self._state.following.append(self.FOLLOW_path_in_renamedAttrList1047)
                            p = self.path()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                newName = p 




                        if self._state.backtracking == 0:
                            if newName is None: newName = createSinglePath('var' + str(count)) 

                        if self._state.backtracking == 0:
                            result.append(Rename(e, newName)) 



                    else:
                        break #loop16




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "renamedAttrList"


    # $ANTLR start "optionStruct"
    # MFQL.g:165:1: optionStruct returns [dict result] : o= option ( ',' o= option )* ;
    def optionStruct(self, ):

        result = None

        o = None


        try:
            try:
                # MFQL.g:166:3: (o= option ( ',' o= option )* )
                # MFQL.g:166:5: o= option ( ',' o= option )*
                pass 
                if self._state.backtracking == 0:
                    result = dict() 

                self._state.following.append(self.FOLLOW_option_in_optionStruct1106)
                o = self.option()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    (key, value) = o; result[key] = value 

                # MFQL.g:168:5: ( ',' o= option )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == 66) :
                        alt17 = 1


                    if alt17 == 1:
                        # MFQL.g:168:6: ',' o= option
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_optionStruct1115)
                        self._state.following.append(self.FOLLOW_option_in_optionStruct1119)
                        o = self.option()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            (key, value) = o; result[key] = value 



                    else:
                        break #loop17




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "optionStruct"


    # $ANTLR start "option"
    # MFQL.g:171:1: option returns [tuple result] : n= name '=' (c= constantStruct | '(' s= optionStruct ')' ) ;
    def option(self, ):

        result = None

        n = None

        c = None

        s = None


        try:
            try:
                # MFQL.g:172:3: (n= name '=' (c= constantStruct | '(' s= optionStruct ')' ) )
                # MFQL.g:172:5: n= name '=' (c= constantStruct | '(' s= optionStruct ')' )
                pass 
                self._state.following.append(self.FOLLOW_name_in_option1142)
                n = self.name()

                self._state.following.pop()
                self.match(self.input, 65, self.FOLLOW_65_in_option1144)
                # MFQL.g:173:5: (c= constantStruct | '(' s= optionStruct ')' )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((MINUS <= LA18_0 <= FLOAT) or LA18_0 == 67 or LA18_0 == 69) :
                    alt18 = 1
                elif (LA18_0 == 63) :
                    alt18 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # MFQL.g:173:7: c= constantStruct
                    pass 
                    self._state.following.append(self.FOLLOW_constantStruct_in_option1154)
                    c = self.constantStruct()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = (n, c) 



                elif alt18 == 2:
                    # MFQL.g:174:7: '(' s= optionStruct ')'
                    pass 
                    self.match(self.input, 63, self.FOLLOW_63_in_option1170)
                    self._state.following.append(self.FOLLOW_optionStruct_in_option1174)
                    s = self.optionStruct()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_option1176)
                    if self._state.backtracking == 0:
                        result = (n, s) 








            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "option"


    # $ANTLR start "relation"
    # MFQL.g:182:1: relation returns [Relation result] : r1= simpleRelOrStr ( ',' r= simpleRelOrStr )* ;
    def relation(self, ):

        result = None

        r1 = None

        r = None


        try:
            try:
                # MFQL.g:183:3: (r1= simpleRelOrStr ( ',' r= simpleRelOrStr )* )
                # MFQL.g:183:5: r1= simpleRelOrStr ( ',' r= simpleRelOrStr )*
                pass 
                if self._state.backtracking == 0:
                    result = ComposedRelation(); many = False 

                self._state.following.append(self.FOLLOW_simpleRelOrStr_in_relation1212)
                r1 = self.simpleRelOrStr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.cross(r1) 

                # MFQL.g:185:5: ( ',' r= simpleRelOrStr )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 66) :
                        alt19 = 1


                    if alt19 == 1:
                        # MFQL.g:185:7: ',' r= simpleRelOrStr
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_relation1222)
                        self._state.following.append(self.FOLLOW_simpleRelOrStr_in_relation1226)
                        r = self.simpleRelOrStr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.cross(r); many = True 



                    else:
                        break #loop19
                if self._state.backtracking == 0:
                    if not many: result = r1 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "relation"


    # $ANTLR start "simpleRelOrStr"
    # MFQL.g:191:1: simpleRelOrStr returns [Relation result] : (r= simpleRelation | s= simpleStream ) ( AS p= path )? ;
    def simpleRelOrStr(self, ):

        result = None

        r = None

        s = None

        p = None


        try:
            try:
                # MFQL.g:192:3: ( (r= simpleRelation | s= simpleStream ) ( AS p= path )? )
                # MFQL.g:192:5: (r= simpleRelation | s= simpleStream ) ( AS p= path )?
                pass 
                # MFQL.g:192:5: (r= simpleRelation | s= simpleStream )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ANUM) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 67) :
                        alt20 = 2
                    elif (LA20_1 == WHERE or LA20_1 == AS or LA20_1 == 62 or LA20_1 == 66) :
                        alt20 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # MFQL.g:192:7: r= simpleRelation
                    pass 
                    self._state.following.append(self.FOLLOW_simpleRelation_in_simpleRelOrStr1265)
                    r = self.simpleRelation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = r 



                elif alt20 == 2:
                    # MFQL.g:193:7: s= simpleStream
                    pass 
                    self._state.following.append(self.FOLLOW_simpleStream_in_simpleRelOrStr1277)
                    s = self.simpleStream()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 




                # MFQL.g:195:5: ( AS p= path )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == AS) :
                    alt21 = 1
                if alt21 == 1:
                    # MFQL.g:195:7: AS p= path
                    pass 
                    self.match(self.input, AS, self.FOLLOW_AS_in_simpleRelOrStr1295)
                    self._state.following.append(self.FOLLOW_path_in_simpleRelOrStr1299)
                    p = self.path()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = RenameRelation(result, p) 








            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "simpleRelOrStr"


    # $ANTLR start "simpleRelation"
    # MFQL.g:198:1: simpleRelation returns [Relation result] : n= name ;
    def simpleRelation(self, ):

        result = None

        n = None


        try:
            try:
                # MFQL.g:199:3: (n= name )
                # MFQL.g:199:5: n= name
                pass 
                self._state.following.append(self.FOLLOW_name_in_simpleRelation1323)
                n = self.name()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = SimpleRelation(n) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "simpleRelation"


    # $ANTLR start "simpleStream"
    # MFQL.g:202:1: simpleStream returns [Relation result] : n= name '[' w= windowSpecification ']' ;
    def simpleStream(self, ):

        result = None

        n = None

        w = None


        try:
            try:
                # MFQL.g:203:3: (n= name '[' w= windowSpecification ']' )
                # MFQL.g:203:5: n= name '[' w= windowSpecification ']'
                pass 
                self._state.following.append(self.FOLLOW_name_in_simpleStream1344)
                n = self.name()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = WindowedStream(SimpleStream(n)) 

                self.match(self.input, 67, self.FOLLOW_67_in_simpleStream1352)
                self._state.following.append(self.FOLLOW_windowSpecification_in_simpleStream1356)
                w = self.windowSpecification()

                self._state.following.pop()
                self.match(self.input, 68, self.FOLLOW_68_in_simpleStream1358)
                if self._state.backtracking == 0:
                    result.setWindow(w) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "simpleStream"


    # $ANTLR start "windowSpecification"
    # MFQL.g:210:1: windowSpecification returns [Window result] : ( PARTITION BY p= path ( ',' path )* )? ( UNBOUNDED | NOW | RANGE i= integer scale= timeUnit | ROWS i= integer ) ;
    def windowSpecification(self, ):

        result = None

        p = None

        i = None

        scale = None


        try:
            try:
                # MFQL.g:211:3: ( ( PARTITION BY p= path ( ',' path )* )? ( UNBOUNDED | NOW | RANGE i= integer scale= timeUnit | ROWS i= integer ) )
                # MFQL.g:211:5: ( PARTITION BY p= path ( ',' path )* )? ( UNBOUNDED | NOW | RANGE i= integer scale= timeUnit | ROWS i= integer )
                pass 
                if self._state.backtracking == 0:
                    partition = None 

                # MFQL.g:212:5: ( PARTITION BY p= path ( ',' path )* )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == PARTITION) :
                    alt23 = 1
                if alt23 == 1:
                    # MFQL.g:212:6: PARTITION BY p= path ( ',' path )*
                    pass 
                    self.match(self.input, PARTITION, self.FOLLOW_PARTITION_in_windowSpecification1386)
                    self.match(self.input, BY, self.FOLLOW_BY_in_windowSpecification1388)
                    if self._state.backtracking == 0:
                        partition = [] 

                    self._state.following.append(self.FOLLOW_path_in_windowSpecification1400)
                    p = self.path()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        partition.append(p) 

                    # MFQL.g:214:7: ( ',' path )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == 66) :
                            alt22 = 1


                        if alt22 == 1:
                            # MFQL.g:214:8: ',' path
                            pass 
                            self.match(self.input, 66, self.FOLLOW_66_in_windowSpecification1411)
                            self._state.following.append(self.FOLLOW_path_in_windowSpecification1413)
                            self.path()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                partition.append(p) 



                        else:
                            break #loop22



                # MFQL.g:216:5: ( UNBOUNDED | NOW | RANGE i= integer scale= timeUnit | ROWS i= integer )
                alt24 = 4
                LA24 = self.input.LA(1)
                if LA24 == UNBOUNDED:
                    alt24 = 1
                elif LA24 == NOW:
                    alt24 = 2
                elif LA24 == RANGE:
                    alt24 = 3
                elif LA24 == ROWS:
                    alt24 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # MFQL.g:216:7: UNBOUNDED
                    pass 
                    self.match(self.input, UNBOUNDED, self.FOLLOW_UNBOUNDED_in_windowSpecification1433)
                    if self._state.backtracking == 0:
                        result = AmountWindow(-1)   



                elif alt24 == 2:
                    # MFQL.g:217:7: NOW
                    pass 
                    self.match(self.input, NOW, self.FOLLOW_NOW_in_windowSpecification1464)
                    if self._state.backtracking == 0:
                        result = TimeWindow(0)       



                elif alt24 == 3:
                    # MFQL.g:218:7: RANGE i= integer scale= timeUnit
                    pass 
                    self.match(self.input, RANGE, self.FOLLOW_RANGE_in_windowSpecification1501)
                    self._state.following.append(self.FOLLOW_integer_in_windowSpecification1505)
                    i = self.integer()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_timeUnit_in_windowSpecification1509)
                    scale = self.timeUnit()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = TimeWindow(i*scale) 



                elif alt24 == 4:
                    # MFQL.g:219:7: ROWS i= integer
                    pass 
                    self.match(self.input, ROWS, self.FOLLOW_ROWS_in_windowSpecification1519)
                    self._state.following.append(self.FOLLOW_integer_in_windowSpecification1523)
                    i = self.integer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = AmountWindow(i)     




                if self._state.backtracking == 0:
                    if partition is not None: result.setPartition(partition) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "windowSpecification"


    # $ANTLR start "timeUnit"
    # MFQL.g:224:1: timeUnit returns [TimeUnit result] : ( SECONDS | MINUTES | HOURS );
    def timeUnit(self, ):

        result = None

        try:
            try:
                # MFQL.g:225:3: ( SECONDS | MINUTES | HOURS )
                alt25 = 3
                LA25 = self.input.LA(1)
                if LA25 == SECONDS:
                    alt25 = 1
                elif LA25 == MINUTES:
                    alt25 = 2
                elif LA25 == HOURS:
                    alt25 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # MFQL.g:225:5: SECONDS
                    pass 
                    self.match(self.input, SECONDS, self.FOLLOW_SECONDS_in_timeUnit1570)
                    if self._state.backtracking == 0:
                        result = 1    



                elif alt25 == 2:
                    # MFQL.g:226:5: MINUTES
                    pass 
                    self.match(self.input, MINUTES, self.FOLLOW_MINUTES_in_timeUnit1578)
                    if self._state.backtracking == 0:
                        result = 60   



                elif alt25 == 3:
                    # MFQL.g:227:5: HOURS
                    pass 
                    self.match(self.input, HOURS, self.FOLLOW_HOURS_in_timeUnit1586)
                    if self._state.backtracking == 0:
                        result = 3600 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "timeUnit"


    # $ANTLR start "eof"
    # MFQL.g:239:1: eof : EOF ;
    def eof(self, ):

        try:
            try:
                # MFQL.g:240:3: ( EOF )
                # MFQL.g:240:5: EOF
                pass 
                self.match(self.input, EOF, self.FOLLOW_EOF_in_eof1611)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "eof"


    # $ANTLR start "integer"
    # MFQL.g:243:1: integer returns [int result] : ( MINUS )? NUM ;
    def integer(self, ):

        result = None

        NUM1 = None

        try:
            try:
                # MFQL.g:244:3: ( ( MINUS )? NUM )
                # MFQL.g:244:5: ( MINUS )? NUM
                pass 
                if self._state.backtracking == 0:
                    invert = False 

                # MFQL.g:245:5: ( MINUS )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == MINUS) :
                    alt26 = 1
                if alt26 == 1:
                    # MFQL.g:245:6: MINUS
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_integer1635)
                    if self._state.backtracking == 0:
                        invert = True 




                NUM1=self.match(self.input, NUM, self.FOLLOW_NUM_in_integer1645)
                if self._state.backtracking == 0:
                         
                    result = int(NUM1.text)
                    if invert: result = -result
                        





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "integer"


    # $ANTLR start "boolean"
    # MFQL.g:253:1: boolean returns [ bool result ] : ( TRUE | FALSE );
    def boolean(self, ):

        result = None

        try:
            try:
                # MFQL.g:254:3: ( TRUE | FALSE )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == TRUE) :
                    alt27 = 1
                elif (LA27_0 == FALSE) :
                    alt27 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # MFQL.g:254:5: TRUE
                    pass 
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_boolean1667)
                    if self._state.backtracking == 0:
                        result = True 



                elif alt27 == 2:
                    # MFQL.g:255:5: FALSE
                    pass 
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_boolean1676)
                    if self._state.backtracking == 0:
                        result = False 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "boolean"


    # $ANTLR start "string"
    # MFQL.g:258:1: string returns [string result] : ( STR | DSTR );
    def string(self, ):

        result = None

        STR2 = None
        DSTR3 = None

        try:
            try:
                # MFQL.g:259:3: ( STR | DSTR )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == STR) :
                    alt28 = 1
                elif (LA28_0 == DSTR) :
                    alt28 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # MFQL.g:259:5: STR
                    pass 
                    STR2=self.match(self.input, STR, self.FOLLOW_STR_in_string1695)
                    if self._state.backtracking == 0:
                        result = escapeString(STR2.text[1:-1])  



                elif alt28 == 2:
                    # MFQL.g:260:5: DSTR
                    pass 
                    DSTR3=self.match(self.input, DSTR, self.FOLLOW_DSTR_in_string1704)
                    if self._state.backtracking == 0:
                        result = escapeString(DSTR3.text[1:-1]) 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "string"


    # $ANTLR start "constantStruct"
    # MFQL.g:263:1: constantStruct returns [ object result ] : (c= constant | '{' (n= string ':' s= constantStruct )? ( ',' n= string ':' s= constantStruct )* '}' | '[' (e= constantStruct )? ( ',' e= constantStruct )* ']' );
    def constantStruct(self, ):

        result = None

        c = None

        n = None

        s = None

        e = None


        try:
            try:
                # MFQL.g:264:3: (c= constant | '{' (n= string ':' s= constantStruct )? ( ',' n= string ':' s= constantStruct )* '}' | '[' (e= constantStruct )? ( ',' e= constantStruct )* ']' )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 == MINUS or LA33 == NUM or LA33 == TRUE or LA33 == FALSE or LA33 == STR or LA33 == DSTR or LA33 == NULL or LA33 == FLOAT:
                    alt33 = 1
                elif LA33 == 69:
                    alt33 = 2
                elif LA33 == 67:
                    alt33 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # MFQL.g:264:5: c= constant
                    pass 
                    self._state.following.append(self.FOLLOW_constant_in_constantStruct1725)
                    c = self.constant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = c 



                elif alt33 == 2:
                    # MFQL.g:265:5: '{' (n= string ':' s= constantStruct )? ( ',' n= string ':' s= constantStruct )* '}'
                    pass 
                    self.match(self.input, 69, self.FOLLOW_69_in_constantStruct1733)
                    if self._state.backtracking == 0:
                        result = dict() 

                    # MFQL.g:266:5: (n= string ':' s= constantStruct )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if ((STR <= LA29_0 <= DSTR)) :
                        alt29 = 1
                    if alt29 == 1:
                        # MFQL.g:266:7: n= string ':' s= constantStruct
                        pass 
                        self._state.following.append(self.FOLLOW_string_in_constantStruct1745)
                        n = self.string()

                        self._state.following.pop()
                        self.match(self.input, 70, self.FOLLOW_70_in_constantStruct1747)
                        self._state.following.append(self.FOLLOW_constantStruct_in_constantStruct1751)
                        s = self.constantStruct()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result[n] = s 




                    # MFQL.g:267:5: ( ',' n= string ':' s= constantStruct )*
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == 66) :
                            alt30 = 1


                        if alt30 == 1:
                            # MFQL.g:267:7: ',' n= string ':' s= constantStruct
                            pass 
                            self.match(self.input, 66, self.FOLLOW_66_in_constantStruct1764)
                            self._state.following.append(self.FOLLOW_string_in_constantStruct1769)
                            n = self.string()

                            self._state.following.pop()
                            self.match(self.input, 70, self.FOLLOW_70_in_constantStruct1771)
                            self._state.following.append(self.FOLLOW_constantStruct_in_constantStruct1775)
                            s = self.constantStruct()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                result[n] = s 



                        else:
                            break #loop30
                    self.match(self.input, 71, self.FOLLOW_71_in_constantStruct1786)


                elif alt33 == 3:
                    # MFQL.g:269:5: '[' (e= constantStruct )? ( ',' e= constantStruct )* ']'
                    pass 
                    self.match(self.input, 67, self.FOLLOW_67_in_constantStruct1792)
                    if self._state.backtracking == 0:
                        result = list() 

                    # MFQL.g:270:5: (e= constantStruct )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if ((MINUS <= LA31_0 <= FLOAT) or LA31_0 == 67 or LA31_0 == 69) :
                        alt31 = 1
                    if alt31 == 1:
                        # MFQL.g:270:7: e= constantStruct
                        pass 
                        self._state.following.append(self.FOLLOW_constantStruct_in_constantStruct1804)
                        e = self.constantStruct()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.append(e) 




                    # MFQL.g:271:5: ( ',' e= constantStruct )*
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == 66) :
                            alt32 = 1


                        if alt32 == 1:
                            # MFQL.g:271:7: ',' e= constantStruct
                            pass 
                            self.match(self.input, 66, self.FOLLOW_66_in_constantStruct1817)
                            self._state.following.append(self.FOLLOW_constantStruct_in_constantStruct1821)
                            e = self.constantStruct()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                result.append(e) 



                        else:
                            break #loop32
                    self.match(self.input, 68, self.FOLLOW_68_in_constantStruct1832)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "constantStruct"


    # $ANTLR start "nonLogicConstant"
    # MFQL.g:275:1: nonLogicConstant returns [ Constant result] : (i= cInt | NULL | f= cFloat | s= cString );
    def nonLogicConstant(self, ):

        result = None

        i = None

        f = None

        s = None


        try:
            try:
                # MFQL.g:276:3: (i= cInt | NULL | f= cFloat | s= cString )
                alt34 = 4
                LA34 = self.input.LA(1)
                if LA34 == MINUS:
                    LA34_1 = self.input.LA(2)

                    if (LA34_1 == FLOAT) :
                        alt34 = 3
                    elif (LA34_1 == NUM) :
                        alt34 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 34, 1, self.input)

                        raise nvae

                elif LA34 == NUM:
                    alt34 = 1
                elif LA34 == NULL:
                    alt34 = 2
                elif LA34 == FLOAT:
                    alt34 = 3
                elif LA34 == STR or LA34 == DSTR:
                    alt34 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # MFQL.g:276:5: i= cInt
                    pass 
                    self._state.following.append(self.FOLLOW_cInt_in_nonLogicConstant1851)
                    i = self.cInt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = i                



                elif alt34 == 2:
                    # MFQL.g:277:5: NULL
                    pass 
                    self.match(self.input, NULL, self.FOLLOW_NULL_in_nonLogicConstant1864)
                    if self._state.backtracking == 0:
                        result = NullConstant()   



                elif alt34 == 3:
                    # MFQL.g:278:5: f= cFloat
                    pass 
                    self._state.following.append(self.FOLLOW_cFloat_in_nonLogicConstant1881)
                    f = self.cFloat()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = f                



                elif alt34 == 4:
                    # MFQL.g:279:5: s= cString
                    pass 
                    self._state.following.append(self.FOLLOW_cString_in_nonLogicConstant1894)
                    s = self.cString()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s                




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "nonLogicConstant"


    # $ANTLR start "logicConstant"
    # MFQL.g:282:1: logicConstant returns [ Constant result ] : b= cBoolean ;
    def logicConstant(self, ):

        result = None

        b = None


        try:
            try:
                # MFQL.g:283:3: (b= cBoolean )
                # MFQL.g:283:5: b= cBoolean
                pass 
                self._state.following.append(self.FOLLOW_cBoolean_in_logicConstant1917)
                b = self.cBoolean()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = b 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "logicConstant"


    # $ANTLR start "constant"
    # MFQL.g:286:1: constant returns [ Constant result ] : (b= logicConstant | c= nonLogicConstant );
    def constant(self, ):

        result = None

        b = None

        c = None


        try:
            try:
                # MFQL.g:287:3: (b= logicConstant | c= nonLogicConstant )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if ((TRUE <= LA35_0 <= FALSE)) :
                    alt35 = 1
                elif ((MINUS <= LA35_0 <= NUM) or (STR <= LA35_0 <= FLOAT)) :
                    alt35 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # MFQL.g:287:5: b= logicConstant
                    pass 
                    self._state.following.append(self.FOLLOW_logicConstant_in_constant1946)
                    b = self.logicConstant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = b 



                elif alt35 == 2:
                    # MFQL.g:288:5: c= nonLogicConstant
                    pass 
                    self._state.following.append(self.FOLLOW_nonLogicConstant_in_constant1959)
                    c = self.nonLogicConstant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = c 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "constant"


    # $ANTLR start "cBoolean"
    # MFQL.g:291:1: cBoolean returns [ Constant result ] : v= boolean ;
    def cBoolean(self, ):

        result = None

        v = None


        try:
            try:
                # MFQL.g:292:3: (v= boolean )
                # MFQL.g:292:5: v= boolean
                pass 
                self._state.following.append(self.FOLLOW_boolean_in_cBoolean1980)
                v = self.boolean()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = Boolean(v) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "cBoolean"


    # $ANTLR start "cInt"
    # MFQL.g:295:1: cInt returns [ Integer result ] : i= integer ;
    def cInt(self, ):

        result = None

        i = None


        try:
            try:
                # MFQL.g:296:3: (i= integer )
                # MFQL.g:296:5: i= integer
                pass 
                self._state.following.append(self.FOLLOW_integer_in_cInt2006)
                i = self.integer()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = Integer(i) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "cInt"


    # $ANTLR start "cFloat"
    # MFQL.g:299:1: cFloat returns [ Float result ] : ( MINUS )? FLOAT ;
    def cFloat(self, ):

        result = None

        FLOAT4 = None

        try:
            try:
                # MFQL.g:300:3: ( ( MINUS )? FLOAT )
                # MFQL.g:300:5: ( MINUS )? FLOAT
                pass 
                # MFQL.g:300:5: ( MINUS )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == MINUS) :
                    alt36 = 1
                if alt36 == 1:
                    # MFQL.g:300:5: MINUS
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_cFloat2025)



                FLOAT4=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_cFloat2028)
                if self._state.backtracking == 0:
                    result = Float(float(FLOAT4.text)) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "cFloat"


    # $ANTLR start "cString"
    # MFQL.g:303:1: cString returns [ String result ] : s= string ;
    def cString(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:304:3: (s= string )
                # MFQL.g:304:5: s= string
                pass 
                self._state.following.append(self.FOLLOW_string_in_cString2049)
                s = self.string()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = String(s) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "cString"


    # $ANTLR start "expr"
    # MFQL.g:311:1: expr returns [ Expression result ] : f1= factor ( PLUS f2= factor | MINUS f2= factor )* ;
    def expr(self, ):

        result = None

        f1 = None

        f2 = None


        try:
            try:
                # MFQL.g:312:3: (f1= factor ( PLUS f2= factor | MINUS f2= factor )* )
                # MFQL.g:312:5: f1= factor ( PLUS f2= factor | MINUS f2= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_expr2073)
                f1 = self.factor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = Summ(); result.add(f1); many = False 

                # MFQL.g:314:5: ( PLUS f2= factor | MINUS f2= factor )*
                while True: #loop37
                    alt37 = 3
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == PLUS) :
                        alt37 = 1
                    elif (LA37_0 == MINUS) :
                        alt37 = 2


                    if alt37 == 1:
                        # MFQL.g:314:7: PLUS f2= factor
                        pass 
                        self.match(self.input, PLUS, self.FOLLOW_PLUS_in_expr2087)
                        self._state.following.append(self.FOLLOW_factor_in_expr2092)
                        f2 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.add(f2); many = True 



                    elif alt37 == 2:
                        # MFQL.g:315:7: MINUS f2= factor
                        pass 
                        self.match(self.input, MINUS, self.FOLLOW_MINUS_in_expr2102)
                        self._state.following.append(self.FOLLOW_factor_in_expr2106)
                        f2 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.sub(f2); many = True 



                    else:
                        break #loop37
                if self._state.backtracking == 0:
                    if not many: result = f1 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "expr"


    # $ANTLR start "exprList"
    # MFQL.g:320:1: exprList returns [ list result ] : (e= expr )? ( ',' e= expr )* ;
    def exprList(self, ):

        result = None

        e = None


        try:
            try:
                # MFQL.g:321:3: ( (e= expr )? ( ',' e= expr )* )
                # MFQL.g:321:5: (e= expr )? ( ',' e= expr )*
                pass 
                if self._state.backtracking == 0:
                    result = [] 

                # MFQL.g:322:5: (e= expr )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if ((MINUS <= LA38_0 <= NUM) or (STR <= LA38_0 <= FLOAT) or LA38_0 == DOT or LA38_0 == ANUM or LA38_0 == 63 or LA38_0 == 67 or LA38_0 == 69) :
                    alt38 = 1
                if alt38 == 1:
                    # MFQL.g:322:6: e= expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_exprList2147)
                    e = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result.append(e) 




                # MFQL.g:323:5: ( ',' e= expr )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == 66) :
                        alt39 = 1


                    if alt39 == 1:
                        # MFQL.g:323:7: ',' e= expr
                        pass 
                        self.match(self.input, 66, self.FOLLOW_66_in_exprList2160)
                        self._state.following.append(self.FOLLOW_expr_in_exprList2164)
                        e = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.append(e) 



                    else:
                        break #loop39




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "exprList"


    # $ANTLR start "factor"
    # MFQL.g:326:1: factor returns [ Expression result ] : t1= term ( STAR t2= term | SLASH t2= term | PERCENT t2= term )* ;
    def factor(self, ):

        result = None

        t1 = None

        t2 = None


        try:
            try:
                # MFQL.g:327:3: (t1= term ( STAR t2= term | SLASH t2= term | PERCENT t2= term )* )
                # MFQL.g:327:5: t1= term ( STAR t2= term | SLASH t2= term | PERCENT t2= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_factor2187)
                t1 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = Product(); result.multiply(t1); many = False 

                # MFQL.g:329:5: ( STAR t2= term | SLASH t2= term | PERCENT t2= term )*
                while True: #loop40
                    alt40 = 4
                    LA40 = self.input.LA(1)
                    if LA40 == STAR:
                        alt40 = 1
                    elif LA40 == SLASH:
                        alt40 = 2
                    elif LA40 == PERCENT:
                        alt40 = 3

                    if alt40 == 1:
                        # MFQL.g:329:7: STAR t2= term
                        pass 
                        self.match(self.input, STAR, self.FOLLOW_STAR_in_factor2201)
                        self._state.following.append(self.FOLLOW_term_in_factor2208)
                        t2 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.multiply(t2); many = True 



                    elif alt40 == 2:
                        # MFQL.g:330:7: SLASH t2= term
                        pass 
                        self.match(self.input, SLASH, self.FOLLOW_SLASH_in_factor2221)
                        self._state.following.append(self.FOLLOW_term_in_factor2227)
                        t2 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.divide(t2);   many = True 



                    elif alt40 == 3:
                        # MFQL.g:331:7: PERCENT t2= term
                        pass 
                        self.match(self.input, PERCENT, self.FOLLOW_PERCENT_in_factor2240)
                        self._state.following.append(self.FOLLOW_term_in_factor2244)
                        t2 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.modulo(t2);   many = True 



                    else:
                        break #loop40
                if self._state.backtracking == 0:
                    if not many: result = t1 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "factor"


    # $ANTLR start "term"
    # MFQL.g:336:1: term returns [ Expression result ] : (p= pattern | f= functionName '(' args= exprList ')' | '(' e= expr ')' );
    def term(self, ):

        result = None

        p = None

        f = None

        args = None

        e = None


        try:
            try:
                # MFQL.g:337:3: (p= pattern | f= functionName '(' args= exprList ')' | '(' e= expr ')' )
                alt41 = 3
                LA41 = self.input.LA(1)
                if LA41 == MINUS or LA41 == NUM or LA41 == STR or LA41 == DSTR or LA41 == NULL or LA41 == FLOAT or LA41 == DOT or LA41 == 67 or LA41 == 69:
                    alt41 = 1
                elif LA41 == ANUM:
                    LA41_2 = self.input.LA(2)

                    if (LA41_2 == 63) :
                        alt41 = 2
                    elif (LA41_2 == EOF or (FROM <= LA41_2 <= STAR) or (SET <= LA41_2 <= DROP) or LA41_2 == AS or LA41_2 == MINUS or (PLUS <= LA41_2 <= OR) or LA41_2 == IS or LA41_2 == 62 or (64 <= LA41_2 <= 67) or (72 <= LA41_2 <= 79)) :
                        alt41 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 41, 2, self.input)

                        raise nvae

                elif LA41 == 63:
                    alt41 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # MFQL.g:337:5: p= pattern
                    pass 
                    self._state.following.append(self.FOLLOW_pattern_in_term2281)
                    p = self.pattern()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = p 



                elif alt41 == 2:
                    # MFQL.g:342:5: f= functionName '(' args= exprList ')'
                    pass 
                    self._state.following.append(self.FOLLOW_functionName_in_term2322)
                    f = self.functionName()

                    self._state.following.pop()
                    self.match(self.input, 63, self.FOLLOW_63_in_term2324)
                    self._state.following.append(self.FOLLOW_exprList_in_term2328)
                    args = self.exprList()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_term2330)
                    if self._state.backtracking == 0:
                        result = Function(f); result.setArguments(args) 



                elif alt41 == 3:
                    # MFQL.g:344:5: '(' e= expr ')'
                    pass 
                    self.match(self.input, 63, self.FOLLOW_63_in_term2342)
                    self._state.following.append(self.FOLLOW_expr_in_term2346)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_term2348)
                    if self._state.backtracking == 0:
                        result = e 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "term"


    # $ANTLR start "functionName"
    # MFQL.g:347:1: functionName returns [String result] : s= anum ;
    def functionName(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:348:3: (s= anum )
                # MFQL.g:348:5: s= anum
                pass 
                self._state.following.append(self.FOLLOW_anum_in_functionName2392)
                s = self.anum()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = s 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "functionName"


    # $ANTLR start "name"
    # MFQL.g:351:1: name returns [String result] : s= anum ;
    def name(self, ):

        result = None

        s = None


        try:
            try:
                # MFQL.g:352:3: (s= anum )
                # MFQL.g:352:5: s= anum
                pass 
                self._state.following.append(self.FOLLOW_anum_in_name2413)
                s = self.anum()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = s 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "name"


    # $ANTLR start "path"
    # MFQL.g:359:1: path returns [ Path result ] : ( DOT ( '[' i= integer ']' (p= pathPart )* )? | ( DOT )? n= name (p= pathPart )* );
    def path(self, ):

        result = None

        i = None

        p = None

        n = None


        try:
            try:
                # MFQL.g:360:3: ( DOT ( '[' i= integer ']' (p= pathPart )* )? | ( DOT )? n= name (p= pathPart )* )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == DOT) :
                    LA46_1 = self.input.LA(2)

                    if (LA46_1 == ANUM) :
                        alt46 = 2
                    elif (LA46_1 == EOF or (FROM <= LA46_1 <= STAR) or (SET <= LA46_1 <= DROP) or LA46_1 == AS or (UNBOUNDED <= LA46_1 <= ROWS) or LA46_1 == MINUS or (PLUS <= LA46_1 <= PERCENT) or (AND <= LA46_1 <= OR) or LA46_1 == IS or LA46_1 == 62 or (64 <= LA46_1 <= 68) or (71 <= LA46_1 <= 79)) :
                        alt46 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 46, 1, self.input)

                        raise nvae

                elif (LA46_0 == ANUM) :
                    alt46 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # MFQL.g:360:5: DOT ( '[' i= integer ']' (p= pathPart )* )?
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_path2436)
                    if self._state.backtracking == 0:
                        result = Path() 

                    # MFQL.g:361:5: ( '[' i= integer ']' (p= pathPart )* )?
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == 67) :
                        alt43 = 1
                    if alt43 == 1:
                        # MFQL.g:362:7: '[' i= integer ']' (p= pathPart )*
                        pass 
                        self.match(self.input, 67, self.FOLLOW_67_in_path2452)
                        self._state.following.append(self.FOLLOW_integer_in_path2456)
                        i = self.integer()

                        self._state.following.pop()
                        self.match(self.input, 68, self.FOLLOW_68_in_path2458)
                        if self._state.backtracking == 0:
                            result.append(IdxAccess(i)) 

                        # MFQL.g:363:7: (p= pathPart )*
                        while True: #loop42
                            alt42 = 2
                            LA42_0 = self.input.LA(1)

                            if (LA42_0 == DOT or LA42_0 == 67) :
                                alt42 = 1


                            if alt42 == 1:
                                # MFQL.g:363:9: p= pathPart
                                pass 
                                self._state.following.append(self.FOLLOW_pathPart_in_path2472)
                                p = self.pathPart()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    result.append(p)



                            else:
                                break #loop42





                elif alt46 == 2:
                    # MFQL.g:365:5: ( DOT )? n= name (p= pathPart )*
                    pass 
                    # MFQL.g:365:5: ( DOT )?
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == DOT) :
                        alt44 = 1
                    if alt44 == 1:
                        # MFQL.g:365:5: DOT
                        pass 
                        self.match(self.input, DOT, self.FOLLOW_DOT_in_path2490)



                    self._state.following.append(self.FOLLOW_name_in_path2495)
                    n = self.name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = Path(); result.append(AttributeAccess(n)) 

                    # MFQL.g:366:5: (p= pathPart )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == DOT or LA45_0 == 67) :
                            alt45 = 1


                        if alt45 == 1:
                            # MFQL.g:366:7: p= pathPart
                            pass 
                            self._state.following.append(self.FOLLOW_pathPart_in_path2507)
                            p = self.pathPart()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                result.append(p)



                        else:
                            break #loop45



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "path"


    # $ANTLR start "pathPart"
    # MFQL.g:369:1: pathPart returns [String result] : ( DOT n= name | '[' i= integer ']' );
    def pathPart(self, ):

        result = None

        n = None

        i = None


        try:
            try:
                # MFQL.g:370:3: ( DOT n= name | '[' i= integer ']' )
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == DOT) :
                    alt47 = 1
                elif (LA47_0 == 67) :
                    alt47 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # MFQL.g:370:5: DOT n= name
                    pass 
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_pathPart2528)
                    self._state.following.append(self.FOLLOW_name_in_pathPart2532)
                    n = self.name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = AttributeAccess(n) 



                elif alt47 == 2:
                    # MFQL.g:371:5: '[' i= integer ']'
                    pass 
                    self.match(self.input, 67, self.FOLLOW_67_in_pathPart2540)
                    self._state.following.append(self.FOLLOW_integer_in_pathPart2544)
                    i = self.integer()

                    self._state.following.pop()
                    self.match(self.input, 68, self.FOLLOW_68_in_pathPart2546)
                    if self._state.backtracking == 0:
                        result = IdxAccess(i) 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "pathPart"


    # $ANTLR start "pattern"
    # MFQL.g:374:1: pattern returns [Pattern result] : (c= nonLogicConstant | s= selector | '[' (p= pattern )? ( ',' p= pattern )* ']' | '{' (name1= string ':' p= pattern )? ( ',' name2= string ':' p= pattern )* '}' );
    def pattern(self, ):

        result = None

        c = None

        s = None

        p = None

        name1 = None

        name2 = None


        try:
            try:
                # MFQL.g:375:3: (c= nonLogicConstant | s= selector | '[' (p= pattern )? ( ',' p= pattern )* ']' | '{' (name1= string ':' p= pattern )? ( ',' name2= string ':' p= pattern )* '}' )
                alt52 = 4
                LA52 = self.input.LA(1)
                if LA52 == MINUS or LA52 == NUM or LA52 == STR or LA52 == DSTR or LA52 == NULL or LA52 == FLOAT:
                    alt52 = 1
                elif LA52 == DOT or LA52 == ANUM:
                    alt52 = 2
                elif LA52 == 67:
                    alt52 = 3
                elif LA52 == 69:
                    alt52 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # MFQL.g:375:5: c= nonLogicConstant
                    pass 
                    self._state.following.append(self.FOLLOW_nonLogicConstant_in_pattern2573)
                    c = self.nonLogicConstant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = c 



                elif alt52 == 2:
                    # MFQL.g:376:5: s= selector
                    pass 
                    self._state.following.append(self.FOLLOW_selector_in_pattern2583)
                    s = self.selector()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        result = s 



                elif alt52 == 3:
                    # MFQL.g:377:5: '[' (p= pattern )? ( ',' p= pattern )* ']'
                    pass 
                    self.match(self.input, 67, self.FOLLOW_67_in_pattern2599)
                    if self._state.backtracking == 0:
                        result = Array() 

                    # MFQL.g:377:30: (p= pattern )?
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((MINUS <= LA48_0 <= NUM) or (STR <= LA48_0 <= FLOAT) or LA48_0 == DOT or LA48_0 == ANUM or LA48_0 == 67 or LA48_0 == 69) :
                        alt48 = 1
                    if alt48 == 1:
                        # MFQL.g:377:31: p= pattern
                        pass 
                        self._state.following.append(self.FOLLOW_pattern_in_pattern2606)
                        p = self.pattern()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.add(p) 




                    # MFQL.g:378:5: ( ',' p= pattern )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == 66) :
                            alt49 = 1


                        if alt49 == 1:
                            # MFQL.g:378:7: ',' p= pattern
                            pass 
                            self.match(self.input, 66, self.FOLLOW_66_in_pattern2618)
                            self._state.following.append(self.FOLLOW_pattern_in_pattern2622)
                            p = self.pattern()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                result.add(p) 



                        else:
                            break #loop49
                    self.match(self.input, 68, self.FOLLOW_68_in_pattern2633)


                elif alt52 == 4:
                    # MFQL.g:380:5: '{' (name1= string ':' p= pattern )? ( ',' name2= string ':' p= pattern )* '}'
                    pass 
                    self.match(self.input, 69, self.FOLLOW_69_in_pattern2639)
                    if self._state.backtracking == 0:
                        result = Map() 

                    # MFQL.g:380:28: (name1= string ':' p= pattern )?
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if ((STR <= LA50_0 <= DSTR)) :
                        alt50 = 1
                    if alt50 == 1:
                        # MFQL.g:380:29: name1= string ':' p= pattern
                        pass 
                        self._state.following.append(self.FOLLOW_string_in_pattern2646)
                        name1 = self.string()

                        self._state.following.pop()
                        self.match(self.input, 70, self.FOLLOW_70_in_pattern2648)
                        self._state.following.append(self.FOLLOW_pattern_in_pattern2652)
                        p = self.pattern()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.put(name1, p) 




                    # MFQL.g:381:5: ( ',' name2= string ':' p= pattern )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == 66) :
                            alt51 = 1


                        if alt51 == 1:
                            # MFQL.g:381:7: ',' name2= string ':' p= pattern
                            pass 
                            self.match(self.input, 66, self.FOLLOW_66_in_pattern2664)
                            self._state.following.append(self.FOLLOW_string_in_pattern2668)
                            name2 = self.string()

                            self._state.following.pop()
                            self.match(self.input, 70, self.FOLLOW_70_in_pattern2670)
                            self._state.following.append(self.FOLLOW_pattern_in_pattern2674)
                            p = self.pattern()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                result.put(name2, p) 



                        else:
                            break #loop51
                    self.match(self.input, 71, self.FOLLOW_71_in_pattern2684)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "pattern"


    # $ANTLR start "selector"
    # MFQL.g:386:1: selector returns [Path result] : p= path ;
    def selector(self, ):

        result = None

        p = None


        try:
            try:
                # MFQL.g:387:3: (p= path )
                # MFQL.g:387:5: p= path
                pass 
                self._state.following.append(self.FOLLOW_path_in_selector2705)
                p = self.path()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result = p 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "selector"


    # $ANTLR start "predicate"
    # MFQL.g:441:1: predicate returns [ Predicate result ] : f1= lfactor ( AND f= lfactor )* ;
    def predicate(self, ):

        result = None

        f1 = None

        f = None


        try:
            try:
                # MFQL.g:442:3: (f1= lfactor ( AND f= lfactor )* )
                # MFQL.g:442:5: f1= lfactor ( AND f= lfactor )*
                pass 
                if self._state.backtracking == 0:
                    result = Conjunction(); many = False 

                self._state.following.append(self.FOLLOW_lfactor_in_predicate2784)
                f1 = self.lfactor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.add(f1) 

                # MFQL.g:445:5: ( AND f= lfactor )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == AND) :
                        alt53 = 1


                    if alt53 == 1:
                        # MFQL.g:445:7: AND f= lfactor
                        pass 
                        self.match(self.input, AND, self.FOLLOW_AND_in_predicate2798)
                        self._state.following.append(self.FOLLOW_lfactor_in_predicate2802)
                        f = self.lfactor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.add(f); many = True 



                    else:
                        break #loop53
                if self._state.backtracking == 0:
                    if not many: result = f1 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "predicate"


    # $ANTLR start "lfactor"
    # MFQL.g:449:1: lfactor returns [ Predicate result ] : t1= lterm ( OR t= lterm )* ;
    def lfactor(self, ):

        result = None

        t1 = None

        t = None


        try:
            try:
                # MFQL.g:450:3: (t1= lterm ( OR t= lterm )* )
                # MFQL.g:450:5: t1= lterm ( OR t= lterm )*
                pass 
                if self._state.backtracking == 0:
                    result = Disjunction(); many = False 

                self._state.following.append(self.FOLLOW_lterm_in_lfactor2837)
                t1 = self.lterm()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    result.add(t1) 

                # MFQL.g:453:5: ( OR t= lterm )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == OR) :
                        alt54 = 1


                    if alt54 == 1:
                        # MFQL.g:453:7: OR t= lterm
                        pass 
                        self.match(self.input, OR, self.FOLLOW_OR_in_lfactor2851)
                        self._state.following.append(self.FOLLOW_lterm_in_lfactor2855)
                        t = self.lterm()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            result.add(t); many = True 



                    else:
                        break #loop54
                if self._state.backtracking == 0:
                    if not many: result = t1 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "lfactor"


    # $ANTLR start "lterm"
    # MFQL.g:457:1: lterm returns [ Predicate result ] : ( NOT )? ( ( '(' predicate )=> '(' p= predicate ')' | val= logicConstant | e1= expr (op= comparaisonOp e2= expr | IS NULL | IS KEY ) ) ;
    def lterm(self, ):

        result = None

        p = None

        val = None

        e1 = None

        op = None

        e2 = None


        try:
            try:
                # MFQL.g:458:3: ( ( NOT )? ( ( '(' predicate )=> '(' p= predicate ')' | val= logicConstant | e1= expr (op= comparaisonOp e2= expr | IS NULL | IS KEY ) ) )
                # MFQL.g:458:5: ( NOT )? ( ( '(' predicate )=> '(' p= predicate ')' | val= logicConstant | e1= expr (op= comparaisonOp e2= expr | IS NULL | IS KEY ) )
                pass 
                if self._state.backtracking == 0:
                    negated = False 

                # MFQL.g:459:5: ( NOT )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == NOT) :
                    alt55 = 1
                if alt55 == 1:
                    # MFQL.g:459:7: NOT
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_lterm2892)
                    if self._state.backtracking == 0:
                        negated=True 




                # MFQL.g:460:5: ( ( '(' predicate )=> '(' p= predicate ')' | val= logicConstant | e1= expr (op= comparaisonOp e2= expr | IS NULL | IS KEY ) )
                alt57 = 3
                alt57 = self.dfa57.predict(self.input)
                if alt57 == 1:
                    # MFQL.g:460:7: ( '(' predicate )=> '(' p= predicate ')'
                    pass 
                    self.match(self.input, 63, self.FOLLOW_63_in_lterm2912)
                    self._state.following.append(self.FOLLOW_predicate_in_lterm2916)
                    p = self.predicate()

                    self._state.following.pop()
                    self.match(self.input, 64, self.FOLLOW_64_in_lterm2918)
                    if self._state.backtracking == 0:
                        val = p 



                elif alt57 == 2:
                    # MFQL.g:461:7: val= logicConstant
                    pass 
                    self._state.following.append(self.FOLLOW_logicConstant_in_lterm2931)
                    val = self.logicConstant()

                    self._state.following.pop()


                elif alt57 == 3:
                    # MFQL.g:462:7: e1= expr (op= comparaisonOp e2= expr | IS NULL | IS KEY )
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_lterm2941)
                    e1 = self.expr()

                    self._state.following.pop()
                    # MFQL.g:463:9: (op= comparaisonOp e2= expr | IS NULL | IS KEY )
                    alt56 = 3
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == 65 or (72 <= LA56_0 <= 79)) :
                        alt56 = 1
                    elif (LA56_0 == IS) :
                        LA56_2 = self.input.LA(2)

                        if (LA56_2 == NULL) :
                            alt56 = 2
                        elif (LA56_2 == KEY) :
                            alt56 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 56, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 56, 0, self.input)

                        raise nvae

                    if alt56 == 1:
                        # MFQL.g:463:11: op= comparaisonOp e2= expr
                        pass 
                        self._state.following.append(self.FOLLOW_comparaisonOp_in_lterm2955)
                        op = self.comparaisonOp()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_expr_in_lterm2959)
                        e2 = self.expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            val = Comparaison(op, e1, e2) 



                    elif alt56 == 2:
                        # MFQL.g:464:11: IS NULL
                        pass 
                        self.match(self.input, IS, self.FOLLOW_IS_in_lterm2973)
                        self.match(self.input, NULL, self.FOLLOW_NULL_in_lterm2975)
                        if self._state.backtracking == 0:
                            val = IsNull(e1)              



                    elif alt56 == 3:
                        # MFQL.g:465:11: IS KEY
                        pass 
                        self.match(self.input, IS, self.FOLLOW_IS_in_lterm3006)
                        self.match(self.input, KEY, self.FOLLOW_KEY_in_lterm3008)
                        if self._state.backtracking == 0:
                            val = IsKey(e1)               







                if self._state.backtracking == 0:
                    if negated: val = Negation(val) 

                if self._state.backtracking == 0:
                    result = val 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "lterm"


    # $ANTLR start "comparaisonOp"
    # MFQL.g:472:1: comparaisonOp returns [ int result ] : ( '<' | '<=' | '=' | '==' | '<>' | '!=' | '>=' | '>' | '><' );
    def comparaisonOp(self, ):

        result = None

        try:
            try:
                # MFQL.g:473:3: ( '<' | '<=' | '=' | '==' | '<>' | '!=' | '>=' | '>' | '><' )
                alt58 = 9
                LA58 = self.input.LA(1)
                if LA58 == 72:
                    alt58 = 1
                elif LA58 == 73:
                    alt58 = 2
                elif LA58 == 65:
                    alt58 = 3
                elif LA58 == 74:
                    alt58 = 4
                elif LA58 == 75:
                    alt58 = 5
                elif LA58 == 76:
                    alt58 = 6
                elif LA58 == 77:
                    alt58 = 7
                elif LA58 == 78:
                    alt58 = 8
                elif LA58 == 79:
                    alt58 = 9
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # MFQL.g:473:5: '<'
                    pass 
                    self.match(self.input, 72, self.FOLLOW_72_in_comparaisonOp3075)
                    if self._state.backtracking == 0:
                        result = Comparaison.LESS          



                elif alt58 == 2:
                    # MFQL.g:474:5: '<='
                    pass 
                    self.match(self.input, 73, self.FOLLOW_73_in_comparaisonOp3084)
                    if self._state.backtracking == 0:
                        result = Comparaison.LESS_EQUAL    



                elif alt58 == 3:
                    # MFQL.g:475:5: '='
                    pass 
                    self.match(self.input, 65, self.FOLLOW_65_in_comparaisonOp3092)
                    if self._state.backtracking == 0:
                        result = Comparaison.EQUAL         



                elif alt58 == 4:
                    # MFQL.g:476:5: '=='
                    pass 
                    self.match(self.input, 74, self.FOLLOW_74_in_comparaisonOp3101)
                    if self._state.backtracking == 0:
                        result = Comparaison.EQUAL         



                elif alt58 == 5:
                    # MFQL.g:477:5: '<>'
                    pass 
                    self.match(self.input, 75, self.FOLLOW_75_in_comparaisonOp3109)
                    if self._state.backtracking == 0:
                        result = Comparaison.UNEQUAL       



                elif alt58 == 6:
                    # MFQL.g:478:5: '!='
                    pass 
                    self.match(self.input, 76, self.FOLLOW_76_in_comparaisonOp3117)
                    if self._state.backtracking == 0:
                        result = Comparaison.UNEQUAL       



                elif alt58 == 7:
                    # MFQL.g:479:5: '>='
                    pass 
                    self.match(self.input, 77, self.FOLLOW_77_in_comparaisonOp3125)
                    if self._state.backtracking == 0:
                        result = Comparaison.GREATER_EQUAL 



                elif alt58 == 8:
                    # MFQL.g:480:5: '>'
                    pass 
                    self.match(self.input, 78, self.FOLLOW_78_in_comparaisonOp3133)
                    if self._state.backtracking == 0:
                        result = Comparaison.GREATER       



                elif alt58 == 9:
                    # MFQL.g:481:5: '><'
                    pass 
                    self.match(self.input, 79, self.FOLLOW_79_in_comparaisonOp3142)
                    if self._state.backtracking == 0:
                        result = Comparaison.SIMILAR       




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "comparaisonOp"


    # $ANTLR start "anum"
    # MFQL.g:488:1: anum returns [string result] : ANUM ;
    def anum(self, ):

        result = None

        ANUM5 = None

        try:
            try:
                # MFQL.g:489:2: ( ANUM )
                # MFQL.g:489:4: ANUM
                pass 
                ANUM5=self.match(self.input, ANUM, self.FOLLOW_ANUM_in_anum3163)
                if self._state.backtracking == 0:
                    result = ANUM5.text 

                if self._state.backtracking == 0:
                    if result[0] == '`': result = result[1:-1] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "anum"

    # $ANTLR start "synpred1_MFQL"
    def synpred1_MFQL_fragment(self, ):
        # MFQL.g:460:7: ( '(' predicate )
        # MFQL.g:460:8: '(' predicate
        pass 
        self.match(self.input, 63, self.FOLLOW_63_in_synpred1_MFQL2905)
        self._state.following.append(self.FOLLOW_predicate_in_synpred1_MFQL2907)
        self.predicate()

        self._state.following.pop()


    # $ANTLR end "synpred1_MFQL"




    # Delegated rules

    def synpred1_MFQL(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_MFQL_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #57

    DFA57_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA57_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA57_min = DFA.unpack(
        u"\1\41\1\0\15\uffff"
        )

    DFA57_max = DFA.unpack(
        u"\1\105\1\0\15\uffff"
        )

    DFA57_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\3\11\uffff\1\1"
        )

    DFA57_special = DFA.unpack(
        u"\1\uffff\1\0\15\uffff"
        )

            
    DFA57_transition = [
        DFA.unpack(u"\2\4\2\2\4\4\3\uffff\1\4\5\uffff\1\4\14\uffff\1\1\3"
        u"\uffff\1\4\1\uffff\1\4"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #57

    class DFA57(DFA):
        pass


        def specialStateTransition(self, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self_ = self
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA57_1 = input.LA(1)

                 
                index57_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_MFQL()):
                    s = 14

                elif (True):
                    s = 4

                 
                input.seek(index57_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 57, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_stmt_in_stmts52 = frozenset([62])
    FOLLOW_62_in_stmts54 = frozenset([1, 4, 9, 17, 19, 20, 22])
    FOLLOW_createStmt_in_stmt77 = frozenset([1])
    FOLLOW_selectStmt_in_stmt97 = frozenset([1])
    FOLLOW_insertStmt_in_stmt117 = frozenset([1])
    FOLLOW_updateStmt_in_stmt137 = frozenset([1])
    FOLLOW_deleteStmt_in_stmt157 = frozenset([1])
    FOLLOW_globalAssignmentStmt_in_stmt177 = frozenset([1])
    FOLLOW_CREATE_in_createStmt196 = frozenset([5, 6, 7])
    FOLLOW_TABLE_in_createStmt204 = frozenset([50])
    FOLLOW_name_in_createStmt208 = frozenset([23])
    FOLLOW_tableDef_in_createStmt212 = frozenset([1])
    FOLLOW_INPUT_in_createStmt230 = frozenset([8])
    FOLLOW_OUTPUT_in_createStmt243 = frozenset([8])
    FOLLOW_STREAM_in_createStmt255 = frozenset([50])
    FOLLOW_name_in_createStmt259 = frozenset([63])
    FOLLOW_streamDef_in_createStmt263 = frozenset([1])
    FOLLOW_SELECT_in_selectStmt294 = frozenset([10, 11, 12, 13, 16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_DISTINCT_in_selectStmt307 = frozenset([11, 12, 13, 16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_attrSel_in_selectStmt323 = frozenset([14])
    FOLLOW_ISTREAM_in_selectStmt350 = frozenset([63])
    FOLLOW_63_in_selectStmt352 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_attrSel_in_selectStmt356 = frozenset([64])
    FOLLOW_64_in_selectStmt358 = frozenset([14])
    FOLLOW_DSTREAM_in_selectStmt368 = frozenset([63])
    FOLLOW_63_in_selectStmt370 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_attrSel_in_selectStmt374 = frozenset([64])
    FOLLOW_64_in_selectStmt376 = frozenset([14])
    FOLLOW_RSTREAM_in_selectStmt386 = frozenset([63])
    FOLLOW_63_in_selectStmt388 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_attrSel_in_selectStmt392 = frozenset([64])
    FOLLOW_64_in_selectStmt394 = frozenset([14])
    FOLLOW_FROM_in_selectStmt420 = frozenset([50])
    FOLLOW_relation_in_selectStmt424 = frozenset([1, 15])
    FOLLOW_WHERE_in_selectStmt433 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_whereRestriction_in_selectStmt437 = frozenset([1])
    FOLLOW_STAR_in_attrSel460 = frozenset([1])
    FOLLOW_renamedAttrList_in_attrSel486 = frozenset([1])
    FOLLOW_INSERT_in_insertStmt509 = frozenset([18])
    FOLLOW_INTO_in_insertStmt511 = frozenset([50])
    FOLLOW_simpleRelation_in_insertStmt519 = frozenset([9])
    FOLLOW_selectStmt_in_insertStmt527 = frozenset([1])
    FOLLOW_UPDATE_in_updateStmt560 = frozenset([50])
    FOLLOW_simpleRelation_in_updateStmt564 = frozenset([20, 21])
    FOLLOW_SET_in_updateStmt585 = frozenset([44, 50])
    FOLLOW_modifOrders_in_updateStmt590 = frozenset([1, 15, 20, 21])
    FOLLOW_DROP_in_updateStmt603 = frozenset([44, 50])
    FOLLOW_dropOrders_in_updateStmt607 = frozenset([1, 15, 20, 21])
    FOLLOW_WHERE_in_updateStmt625 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_whereRestriction_in_updateStmt629 = frozenset([1])
    FOLLOW_DELETE_in_deleteStmt672 = frozenset([14])
    FOLLOW_FROM_in_deleteStmt674 = frozenset([50])
    FOLLOW_simpleRelOrStr_in_deleteStmt682 = frozenset([1, 15])
    FOLLOW_WHERE_in_deleteStmt689 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_whereRestriction_in_deleteStmt693 = frozenset([1])
    FOLLOW_SET_in_globalAssignmentStmt730 = frozenset([50])
    FOLLOW_name_in_globalAssignmentStmt734 = frozenset([65])
    FOLLOW_65_in_globalAssignmentStmt736 = frozenset([33, 34, 35, 36, 37, 38, 39, 40])
    FOLLOW_constant_in_globalAssignmentStmt740 = frozenset([1])
    FOLLOW_modifOrder_in_modifOrders783 = frozenset([1, 66])
    FOLLOW_66_in_modifOrders793 = frozenset([44, 50])
    FOLLOW_modifOrder_in_modifOrders797 = frozenset([1, 66])
    FOLLOW_path_in_dropOrders827 = frozenset([1, 66])
    FOLLOW_66_in_dropOrders837 = frozenset([44, 50])
    FOLLOW_path_in_dropOrders841 = frozenset([1, 66])
    FOLLOW_path_in_modifOrder871 = frozenset([65])
    FOLLOW_65_in_modifOrder873 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_expr_in_modifOrder877 = frozenset([1])
    FOLLOW_63_in_streamDef896 = frozenset([50])
    FOLLOW_optionStruct_in_streamDef900 = frozenset([64])
    FOLLOW_64_in_streamDef902 = frozenset([1])
    FOLLOW_AS_in_tableDef925 = frozenset([9])
    FOLLOW_selectStmt_in_tableDef929 = frozenset([1])
    FOLLOW_predicate_in_whereRestriction950 = frozenset([1])
    FOLLOW_expr_in_renamedAttrList979 = frozenset([1, 23, 66])
    FOLLOW_AS_in_renamedAttrList989 = frozenset([44, 50])
    FOLLOW_path_in_renamedAttrList993 = frozenset([1, 66])
    FOLLOW_66_in_renamedAttrList1027 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_expr_in_renamedAttrList1031 = frozenset([1, 23, 66])
    FOLLOW_AS_in_renamedAttrList1043 = frozenset([44, 50])
    FOLLOW_path_in_renamedAttrList1047 = frozenset([1, 66])
    FOLLOW_option_in_optionStruct1106 = frozenset([1, 66])
    FOLLOW_66_in_optionStruct1115 = frozenset([50])
    FOLLOW_option_in_optionStruct1119 = frozenset([1, 66])
    FOLLOW_name_in_option1142 = frozenset([65])
    FOLLOW_65_in_option1144 = frozenset([33, 34, 35, 36, 37, 38, 39, 40, 63, 67, 69])
    FOLLOW_constantStruct_in_option1154 = frozenset([1])
    FOLLOW_63_in_option1170 = frozenset([50])
    FOLLOW_optionStruct_in_option1174 = frozenset([64])
    FOLLOW_64_in_option1176 = frozenset([1])
    FOLLOW_simpleRelOrStr_in_relation1212 = frozenset([1, 66])
    FOLLOW_66_in_relation1222 = frozenset([50])
    FOLLOW_simpleRelOrStr_in_relation1226 = frozenset([1, 66])
    FOLLOW_simpleRelation_in_simpleRelOrStr1265 = frozenset([1, 23])
    FOLLOW_simpleStream_in_simpleRelOrStr1277 = frozenset([1, 23])
    FOLLOW_AS_in_simpleRelOrStr1295 = frozenset([44, 50])
    FOLLOW_path_in_simpleRelOrStr1299 = frozenset([1])
    FOLLOW_name_in_simpleRelation1323 = frozenset([1])
    FOLLOW_name_in_simpleStream1344 = frozenset([67])
    FOLLOW_67_in_simpleStream1352 = frozenset([24, 26, 27, 28, 29])
    FOLLOW_windowSpecification_in_simpleStream1356 = frozenset([68])
    FOLLOW_68_in_simpleStream1358 = frozenset([1])
    FOLLOW_PARTITION_in_windowSpecification1386 = frozenset([25])
    FOLLOW_BY_in_windowSpecification1388 = frozenset([44, 50])
    FOLLOW_path_in_windowSpecification1400 = frozenset([26, 27, 28, 29, 66])
    FOLLOW_66_in_windowSpecification1411 = frozenset([44, 50])
    FOLLOW_path_in_windowSpecification1413 = frozenset([26, 27, 28, 29, 66])
    FOLLOW_UNBOUNDED_in_windowSpecification1433 = frozenset([1])
    FOLLOW_NOW_in_windowSpecification1464 = frozenset([1])
    FOLLOW_RANGE_in_windowSpecification1501 = frozenset([33, 34])
    FOLLOW_integer_in_windowSpecification1505 = frozenset([30, 31, 32])
    FOLLOW_timeUnit_in_windowSpecification1509 = frozenset([1])
    FOLLOW_ROWS_in_windowSpecification1519 = frozenset([33, 34])
    FOLLOW_integer_in_windowSpecification1523 = frozenset([1])
    FOLLOW_SECONDS_in_timeUnit1570 = frozenset([1])
    FOLLOW_MINUTES_in_timeUnit1578 = frozenset([1])
    FOLLOW_HOURS_in_timeUnit1586 = frozenset([1])
    FOLLOW_EOF_in_eof1611 = frozenset([1])
    FOLLOW_MINUS_in_integer1635 = frozenset([34])
    FOLLOW_NUM_in_integer1645 = frozenset([1])
    FOLLOW_TRUE_in_boolean1667 = frozenset([1])
    FOLLOW_FALSE_in_boolean1676 = frozenset([1])
    FOLLOW_STR_in_string1695 = frozenset([1])
    FOLLOW_DSTR_in_string1704 = frozenset([1])
    FOLLOW_constant_in_constantStruct1725 = frozenset([1])
    FOLLOW_69_in_constantStruct1733 = frozenset([33, 34, 37, 38, 39, 40, 66, 71])
    FOLLOW_string_in_constantStruct1745 = frozenset([70])
    FOLLOW_70_in_constantStruct1747 = frozenset([33, 34, 35, 36, 37, 38, 39, 40, 67, 69])
    FOLLOW_constantStruct_in_constantStruct1751 = frozenset([66, 71])
    FOLLOW_66_in_constantStruct1764 = frozenset([33, 34, 37, 38, 39, 40])
    FOLLOW_string_in_constantStruct1769 = frozenset([70])
    FOLLOW_70_in_constantStruct1771 = frozenset([33, 34, 35, 36, 37, 38, 39, 40, 67, 69])
    FOLLOW_constantStruct_in_constantStruct1775 = frozenset([66, 71])
    FOLLOW_71_in_constantStruct1786 = frozenset([1])
    FOLLOW_67_in_constantStruct1792 = frozenset([33, 34, 35, 36, 37, 38, 39, 40, 66, 67, 68, 69])
    FOLLOW_constantStruct_in_constantStruct1804 = frozenset([66, 68])
    FOLLOW_66_in_constantStruct1817 = frozenset([33, 34, 35, 36, 37, 38, 39, 40, 67, 69])
    FOLLOW_constantStruct_in_constantStruct1821 = frozenset([66, 68])
    FOLLOW_68_in_constantStruct1832 = frozenset([1])
    FOLLOW_cInt_in_nonLogicConstant1851 = frozenset([1])
    FOLLOW_NULL_in_nonLogicConstant1864 = frozenset([1])
    FOLLOW_cFloat_in_nonLogicConstant1881 = frozenset([1])
    FOLLOW_cString_in_nonLogicConstant1894 = frozenset([1])
    FOLLOW_cBoolean_in_logicConstant1917 = frozenset([1])
    FOLLOW_logicConstant_in_constant1946 = frozenset([1])
    FOLLOW_nonLogicConstant_in_constant1959 = frozenset([1])
    FOLLOW_boolean_in_cBoolean1980 = frozenset([1])
    FOLLOW_integer_in_cInt2006 = frozenset([1])
    FOLLOW_MINUS_in_cFloat2025 = frozenset([40])
    FOLLOW_FLOAT_in_cFloat2028 = frozenset([1])
    FOLLOW_string_in_cString2049 = frozenset([1])
    FOLLOW_factor_in_expr2073 = frozenset([1, 33, 41])
    FOLLOW_PLUS_in_expr2087 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_factor_in_expr2092 = frozenset([1, 33, 41])
    FOLLOW_MINUS_in_expr2102 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_factor_in_expr2106 = frozenset([1, 33, 41])
    FOLLOW_expr_in_exprList2147 = frozenset([1, 66])
    FOLLOW_66_in_exprList2160 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_expr_in_exprList2164 = frozenset([1, 66])
    FOLLOW_term_in_factor2187 = frozenset([1, 16, 42, 43])
    FOLLOW_STAR_in_factor2201 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_term_in_factor2208 = frozenset([1, 16, 42, 43])
    FOLLOW_SLASH_in_factor2221 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_term_in_factor2227 = frozenset([1, 16, 42, 43])
    FOLLOW_PERCENT_in_factor2240 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_term_in_factor2244 = frozenset([1, 16, 42, 43])
    FOLLOW_pattern_in_term2281 = frozenset([1])
    FOLLOW_functionName_in_term2322 = frozenset([63])
    FOLLOW_63_in_term2324 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 64, 66, 67, 69])
    FOLLOW_exprList_in_term2328 = frozenset([64])
    FOLLOW_64_in_term2330 = frozenset([1])
    FOLLOW_63_in_term2342 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_expr_in_term2346 = frozenset([64])
    FOLLOW_64_in_term2348 = frozenset([1])
    FOLLOW_anum_in_functionName2392 = frozenset([1])
    FOLLOW_anum_in_name2413 = frozenset([1])
    FOLLOW_DOT_in_path2436 = frozenset([1, 67])
    FOLLOW_67_in_path2452 = frozenset([33, 34])
    FOLLOW_integer_in_path2456 = frozenset([68])
    FOLLOW_68_in_path2458 = frozenset([1, 44, 67])
    FOLLOW_pathPart_in_path2472 = frozenset([1, 44, 67])
    FOLLOW_DOT_in_path2490 = frozenset([50])
    FOLLOW_name_in_path2495 = frozenset([1, 44, 67])
    FOLLOW_pathPart_in_path2507 = frozenset([1, 44, 67])
    FOLLOW_DOT_in_pathPart2528 = frozenset([50])
    FOLLOW_name_in_pathPart2532 = frozenset([1])
    FOLLOW_67_in_pathPart2540 = frozenset([33, 34])
    FOLLOW_integer_in_pathPart2544 = frozenset([68])
    FOLLOW_68_in_pathPart2546 = frozenset([1])
    FOLLOW_nonLogicConstant_in_pattern2573 = frozenset([1])
    FOLLOW_selector_in_pattern2583 = frozenset([1])
    FOLLOW_67_in_pattern2599 = frozenset([33, 34, 37, 38, 39, 40, 44, 50, 66, 67, 68, 69])
    FOLLOW_pattern_in_pattern2606 = frozenset([66, 68])
    FOLLOW_66_in_pattern2618 = frozenset([33, 34, 37, 38, 39, 40, 44, 50, 67, 69])
    FOLLOW_pattern_in_pattern2622 = frozenset([66, 68])
    FOLLOW_68_in_pattern2633 = frozenset([1])
    FOLLOW_69_in_pattern2639 = frozenset([33, 34, 37, 38, 39, 40, 66, 71])
    FOLLOW_string_in_pattern2646 = frozenset([70])
    FOLLOW_70_in_pattern2648 = frozenset([33, 34, 37, 38, 39, 40, 44, 50, 67, 69])
    FOLLOW_pattern_in_pattern2652 = frozenset([66, 71])
    FOLLOW_66_in_pattern2664 = frozenset([33, 34, 37, 38, 39, 40])
    FOLLOW_string_in_pattern2668 = frozenset([70])
    FOLLOW_70_in_pattern2670 = frozenset([33, 34, 37, 38, 39, 40, 44, 50, 67, 69])
    FOLLOW_pattern_in_pattern2674 = frozenset([66, 71])
    FOLLOW_71_in_pattern2684 = frozenset([1])
    FOLLOW_path_in_selector2705 = frozenset([1])
    FOLLOW_lfactor_in_predicate2784 = frozenset([1, 45])
    FOLLOW_AND_in_predicate2798 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_lfactor_in_predicate2802 = frozenset([1, 45])
    FOLLOW_lterm_in_lfactor2837 = frozenset([1, 46])
    FOLLOW_OR_in_lfactor2851 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_lterm_in_lfactor2855 = frozenset([1, 46])
    FOLLOW_NOT_in_lterm2892 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_63_in_lterm2912 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_predicate_in_lterm2916 = frozenset([64])
    FOLLOW_64_in_lterm2918 = frozenset([1])
    FOLLOW_logicConstant_in_lterm2931 = frozenset([1])
    FOLLOW_expr_in_lterm2941 = frozenset([48, 65, 72, 73, 74, 75, 76, 77, 78, 79])
    FOLLOW_comparaisonOp_in_lterm2955 = frozenset([16, 33, 34, 37, 38, 39, 40, 44, 50, 63, 67, 69])
    FOLLOW_expr_in_lterm2959 = frozenset([1])
    FOLLOW_IS_in_lterm2973 = frozenset([39])
    FOLLOW_NULL_in_lterm2975 = frozenset([1])
    FOLLOW_IS_in_lterm3006 = frozenset([49])
    FOLLOW_KEY_in_lterm3008 = frozenset([1])
    FOLLOW_72_in_comparaisonOp3075 = frozenset([1])
    FOLLOW_73_in_comparaisonOp3084 = frozenset([1])
    FOLLOW_65_in_comparaisonOp3092 = frozenset([1])
    FOLLOW_74_in_comparaisonOp3101 = frozenset([1])
    FOLLOW_75_in_comparaisonOp3109 = frozenset([1])
    FOLLOW_76_in_comparaisonOp3117 = frozenset([1])
    FOLLOW_77_in_comparaisonOp3125 = frozenset([1])
    FOLLOW_78_in_comparaisonOp3133 = frozenset([1])
    FOLLOW_79_in_comparaisonOp3142 = frozenset([1])
    FOLLOW_ANUM_in_anum3163 = frozenset([1])
    FOLLOW_63_in_synpred1_MFQL2905 = frozenset([16, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 50, 63, 67, 69])
    FOLLOW_predicate_in_synpred1_MFQL2907 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MFQLLexer", MFQLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
