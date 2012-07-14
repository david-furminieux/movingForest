# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 MFQL.g 2011-04-01 00:04:06

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__68=68
T__69=69
T__66=66
WHERE=15
T__67=67
STAR=16
T__64=64
T__65=65
T__62=62
T__63=63
ISTREAM=11
DSTR=38
INPUT=6
UPDATE=19
TABLE=5
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
RSTREAM=13
NULL=39
ON=55
RANGE=28
SET=20
RIGHT=57
HAVING=52
DELETE=22
MINUS=33
TRUE=35
JOIN=53
NUM=34
DSTREAM=12
MINUTES=31
GROUP=51
T__71=71
WS=61
T__72=72
T__70=70
DROP=21
OR=46
ROWS=29
FROM=14
T__76=76
T__75=75
UNBOUNDED=26
FALSE=36
DISTINCT=10
T__74=74
OUTPUT=7
T__73=73
T__79=79
HOURS=32
T__78=78
T__77=77


class MFQLLexer(Lexer):

    grammarFileName = "MFQL.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(MFQLLexer, self).__init__(input, state)


        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )






    # $ANTLR start "T__62"
    def mT__62(self, ):

        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # MFQL.g:7:7: ( ';' )
            # MFQL.g:7:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__62"



    # $ANTLR start "T__63"
    def mT__63(self, ):

        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # MFQL.g:8:7: ( '(' )
            # MFQL.g:8:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__63"



    # $ANTLR start "T__64"
    def mT__64(self, ):

        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # MFQL.g:9:7: ( ')' )
            # MFQL.g:9:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):

        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # MFQL.g:10:7: ( '=' )
            # MFQL.g:10:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):

        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # MFQL.g:11:7: ( ',' )
            # MFQL.g:11:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):

        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # MFQL.g:12:7: ( '[' )
            # MFQL.g:12:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):

        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # MFQL.g:13:7: ( ']' )
            # MFQL.g:13:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):

        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # MFQL.g:14:7: ( '{' )
            # MFQL.g:14:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):

        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # MFQL.g:15:7: ( ':' )
            # MFQL.g:15:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):

        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # MFQL.g:16:7: ( '}' )
            # MFQL.g:16:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):

        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # MFQL.g:17:7: ( '<' )
            # MFQL.g:17:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):

        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # MFQL.g:18:7: ( '<=' )
            # MFQL.g:18:9: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):

        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # MFQL.g:19:7: ( '==' )
            # MFQL.g:19:9: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):

        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # MFQL.g:20:7: ( '<>' )
            # MFQL.g:20:9: '<>'
            pass 
            self.match("<>")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):

        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # MFQL.g:21:7: ( '!=' )
            # MFQL.g:21:9: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):

        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # MFQL.g:22:7: ( '>=' )
            # MFQL.g:22:9: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):

        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # MFQL.g:23:7: ( '>' )
            # MFQL.g:23:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):

        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # MFQL.g:24:7: ( '><' )
            # MFQL.g:24:9: '><'
            pass 
            self.match("><")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__79"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # MFQL.g:495:4: ( ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'D' | 'd' ) )
            # MFQL.g:495:12: ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "AS"
    def mAS(self, ):

        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:496:3: ( ( 'A' | 'a' ) ( 'S' | 's' ) )
            # MFQL.g:496:12: ( 'A' | 'a' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS"



    # $ANTLR start "BY"
    def mBY(self, ):

        try:
            _type = BY
            _channel = DEFAULT_CHANNEL

            # MFQL.g:497:3: ( ( 'B' | 'b' ) ( 'Y' | 'y' ) )
            # MFQL.g:497:12: ( 'B' | 'b' ) ( 'Y' | 'y' )
            pass 
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BY"



    # $ANTLR start "CREATE"
    def mCREATE(self, ):

        try:
            _type = CREATE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:498:7: ( ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' ) )
            # MFQL.g:498:12: ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CREATE"



    # $ANTLR start "DELETE"
    def mDELETE(self, ):

        try:
            _type = DELETE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:499:7: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'T' | 't' ) ( 'E' | 'e' ) )
            # MFQL.g:499:12: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'T' | 't' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DELETE"



    # $ANTLR start "DISTINCT"
    def mDISTINCT(self, ):

        try:
            _type = DISTINCT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:500:9: ( ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'C' | 'c' ) ( 'T' | 't' ) )
            # MFQL.g:500:12: ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'C' | 'c' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISTINCT"



    # $ANTLR start "DROP"
    def mDROP(self, ):

        try:
            _type = DROP
            _channel = DEFAULT_CHANNEL

            # MFQL.g:501:5: ( ( 'D' | 'd' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'P' | 'p' ) )
            # MFQL.g:501:12: ( 'D' | 'd' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'P' | 'p' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DROP"



    # $ANTLR start "DSTREAM"
    def mDSTREAM(self, ):

        try:
            _type = DSTREAM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:502:8: ( ( 'D' | 'd' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' ) )
            # MFQL.g:502:12: ( 'D' | 'd' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DSTREAM"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:503:6: ( ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )
            # MFQL.g:503:12: ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "FROM"
    def mFROM(self, ):

        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:504:5: ( ( 'F' | 'f' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'M' | 'm' ) )
            # MFQL.g:504:12: ( 'F' | 'f' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROM"



    # $ANTLR start "GROUP"
    def mGROUP(self, ):

        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # MFQL.g:505:6: ( ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'P' | 'p' ) )
            # MFQL.g:505:12: ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'P' | 'p' )
            pass 
            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GROUP"



    # $ANTLR start "HAVING"
    def mHAVING(self, ):

        try:
            _type = HAVING
            _channel = DEFAULT_CHANNEL

            # MFQL.g:506:7: ( ( 'H' | 'h' ) ( 'A' | 'a' ) ( 'V' | 'v' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'G' | 'g' ) )
            # MFQL.g:506:12: ( 'H' | 'h' ) ( 'A' | 'a' ) ( 'V' | 'v' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'G' | 'g' )
            pass 
            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 86 or self.input.LA(1) == 118:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HAVING"



    # $ANTLR start "HOURS"
    def mHOURS(self, ):

        try:
            _type = HOURS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:507:6: ( ( 'H' | 'h' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'S' | 's' ) )
            # MFQL.g:507:12: ( 'H' | 'h' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HOURS"



    # $ANTLR start "INPUT"
    def mINPUT(self, ):

        try:
            _type = INPUT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:508:6: ( ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'P' | 'p' ) ( 'U' | 'u' ) ( 'T' | 't' ) )
            # MFQL.g:508:12: ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'P' | 'p' ) ( 'U' | 'u' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INPUT"



    # $ANTLR start "INSERT"
    def mINSERT(self, ):

        try:
            _type = INSERT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:509:7: ( ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'T' | 't' ) )
            # MFQL.g:509:12: ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSERT"



    # $ANTLR start "INTO"
    def mINTO(self, ):

        try:
            _type = INTO
            _channel = DEFAULT_CHANNEL

            # MFQL.g:510:5: ( ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( 'O' | 'o' ) )
            # MFQL.g:510:12: ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'T' | 't' ) ( 'O' | 'o' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTO"



    # $ANTLR start "IS"
    def mIS(self, ):

        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:511:3: ( ( 'I' | 'i' ) ( 'S' | 's' ) )
            # MFQL.g:511:12: ( 'I' | 'i' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IS"



    # $ANTLR start "ISTREAM"
    def mISTREAM(self, ):

        try:
            _type = ISTREAM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:512:8: ( ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' ) )
            # MFQL.g:512:12: ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISTREAM"



    # $ANTLR start "JOIN"
    def mJOIN(self, ):

        try:
            _type = JOIN
            _channel = DEFAULT_CHANNEL

            # MFQL.g:513:5: ( ( 'J' | 'j' ) ( 'O' | 'o' ) ( 'I' | 'i' ) ( 'N' | 'n' ) )
            # MFQL.g:513:12: ( 'J' | 'j' ) ( 'O' | 'o' ) ( 'I' | 'i' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "JOIN"



    # $ANTLR start "KEY"
    def mKEY(self, ):

        try:
            _type = KEY
            _channel = DEFAULT_CHANNEL

            # MFQL.g:514:4: ( ( 'K' | 'k' ) ( 'E' | 'e' ) ( 'Y' | 'y' ) )
            # MFQL.g:514:12: ( 'K' | 'k' ) ( 'E' | 'e' ) ( 'Y' | 'y' )
            pass 
            if self.input.LA(1) == 75 or self.input.LA(1) == 107:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "KEY"



    # $ANTLR start "LEFT"
    def mLEFT(self, ):

        try:
            _type = LEFT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:515:5: ( ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'T' | 't' ) )
            # MFQL.g:515:12: ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT"



    # $ANTLR start "MINUTES"
    def mMINUTES(self, ):

        try:
            _type = MINUTES
            _channel = DEFAULT_CHANNEL

            # MFQL.g:516:8: ( ( 'M' | 'm' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'S' | 's' ) )
            # MFQL.g:516:12: ( 'M' | 'm' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUTES"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:517:4: ( ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'T' | 't' ) )
            # MFQL.g:517:12: ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NOW"
    def mNOW(self, ):

        try:
            _type = NOW
            _channel = DEFAULT_CHANNEL

            # MFQL.g:518:4: ( ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'W' | 'w' ) )
            # MFQL.g:518:12: ( 'N' | 'n' ) ( 'O' | 'o' ) ( 'W' | 'w' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOW"



    # $ANTLR start "NULL"
    def mNULL(self, ):

        try:
            _type = NULL
            _channel = DEFAULT_CHANNEL

            # MFQL.g:519:5: ( ( 'N' | 'n' ) ( 'U' | 'u' ) ( 'L' | 'l' ) ( 'L' | 'l' ) )
            # MFQL.g:519:12: ( 'N' | 'n' ) ( 'U' | 'u' ) ( 'L' | 'l' ) ( 'L' | 'l' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NULL"



    # $ANTLR start "ON"
    def mON(self, ):

        try:
            _type = ON
            _channel = DEFAULT_CHANNEL

            # MFQL.g:520:3: ( ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # MFQL.g:520:12: ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ON"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # MFQL.g:521:3: ( ( 'O' | 'o' ) ( 'R' | 'r' ) )
            # MFQL.g:521:12: ( 'O' | 'o' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "OUTER"
    def mOUTER(self, ):

        try:
            _type = OUTER
            _channel = DEFAULT_CHANNEL

            # MFQL.g:522:6: ( ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) )
            # MFQL.g:522:12: ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTER"



    # $ANTLR start "OUTPUT"
    def mOUTPUT(self, ):

        try:
            _type = OUTPUT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:523:7: ( ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'P' | 'p' ) ( 'U' | 'u' ) ( 'T' | 't' ) )
            # MFQL.g:523:12: ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'T' | 't' ) ( 'P' | 'p' ) ( 'U' | 'u' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTPUT"



    # $ANTLR start "PARTITION"
    def mPARTITION(self, ):

        try:
            _type = PARTITION
            _channel = DEFAULT_CHANNEL

            # MFQL.g:524:10: ( ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'R' | 'r' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # MFQL.g:524:12: ( 'P' | 'p' ) ( 'A' | 'a' ) ( 'R' | 'r' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARTITION"



    # $ANTLR start "RANGE"
    def mRANGE(self, ):

        try:
            _type = RANGE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:525:6: ( ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' ) ( 'E' | 'e' ) )
            # MFQL.g:525:12: ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RANGE"



    # $ANTLR start "RIGHT"
    def mRIGHT(self, ):

        try:
            _type = RIGHT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:526:6: ( ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'G' | 'g' ) ( 'H' | 'h' ) ( 'T' | 't' ) )
            # MFQL.g:526:12: ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'G' | 'g' ) ( 'H' | 'h' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT"



    # $ANTLR start "RSTREAM"
    def mRSTREAM(self, ):

        try:
            _type = RSTREAM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:527:8: ( ( 'R' | 'r' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' ) )
            # MFQL.g:527:12: ( 'R' | 'r' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RSTREAM"



    # $ANTLR start "ROWS"
    def mROWS(self, ):

        try:
            _type = ROWS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:528:5: ( ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'W' | 'w' ) ( 'S' | 's' ) )
            # MFQL.g:528:12: ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'W' | 'w' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROWS"



    # $ANTLR start "SECONDS"
    def mSECONDS(self, ):

        try:
            _type = SECONDS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:529:8: ( ( 'S' | 's' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'D' | 'd' ) ( 'S' | 's' ) )
            # MFQL.g:529:12: ( 'S' | 's' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'D' | 'd' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SECONDS"



    # $ANTLR start "SELECT"
    def mSELECT(self, ):

        try:
            _type = SELECT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:530:7: ( ( 'S' | 's' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'T' | 't' ) )
            # MFQL.g:530:12: ( 'S' | 's' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SELECT"



    # $ANTLR start "SET"
    def mSET(self, ):

        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # MFQL.g:531:4: ( ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' ) )
            # MFQL.g:531:12: ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SET"



    # $ANTLR start "STREAM"
    def mSTREAM(self, ):

        try:
            _type = STREAM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:532:7: ( ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' ) )
            # MFQL.g:532:12: ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'A' | 'a' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STREAM"



    # $ANTLR start "TABLE"
    def mTABLE(self, ):

        try:
            _type = TABLE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:533:6: ( ( 'T' | 't' ) ( 'A' | 'a' ) ( 'B' | 'b' ) ( 'L' | 'l' ) ( 'E' | 'e' ) )
            # MFQL.g:533:12: ( 'T' | 't' ) ( 'A' | 'a' ) ( 'B' | 'b' ) ( 'L' | 'l' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TABLE"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:534:5: ( ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )
            # MFQL.g:534:12: ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "UNBOUNDED"
    def mUNBOUNDED(self, ):

        try:
            _type = UNBOUNDED
            _channel = DEFAULT_CHANNEL

            # MFQL.g:535:10: ( ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'B' | 'b' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'D' | 'd' ) )
            # MFQL.g:535:12: ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'B' | 'b' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNBOUNDED"



    # $ANTLR start "UPDATE"
    def mUPDATE(self, ):

        try:
            _type = UPDATE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:536:7: ( ( 'U' | 'u' ) ( 'P' | 'p' ) ( 'D' | 'd' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' ) )
            # MFQL.g:536:12: ( 'U' | 'u' ) ( 'P' | 'p' ) ( 'D' | 'd' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UPDATE"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):

        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # MFQL.g:537:6: ( ( 'W' | 'w' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'E' | 'e' ) )
            # MFQL.g:537:12: ( 'W' | 'w' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:539:6: ( '-' )
            # MFQL.g:539:10: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:540:5: ( '+' )
            # MFQL.g:540:10: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # MFQL.g:541:5: ( '*' )
            # MFQL.g:541:10: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "SLASH"
    def mSLASH(self, ):

        try:
            _type = SLASH
            _channel = DEFAULT_CHANNEL

            # MFQL.g:542:6: ( '/' )
            # MFQL.g:542:10: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASH"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:543:4: ( '.' )
            # MFQL.g:543:10: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "DOTDOT"
    def mDOTDOT(self, ):

        try:
            _type = DOTDOT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:544:7: ( '..' )
            # MFQL.g:544:10: '..'
            pass 
            self.match("..")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOTDOT"



    # $ANTLR start "AT"
    def mAT(self, ):

        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:545:3: ( '@' )
            # MFQL.g:545:10: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AT"



    # $ANTLR start "PERCENT"
    def mPERCENT(self, ):

        try:
            _type = PERCENT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:546:8: ( '%' )
            # MFQL.g:546:10: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENT"



    # $ANTLR start "COMMENTS"
    def mCOMMENTS(self, ):

        try:
            _type = COMMENTS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:548:9: ( '#' ( . )* '\\n' )
            # MFQL.g:548:11: '#' ( . )* '\\n'
            pass 
            self.match(35)
            # MFQL.g:548:15: ( . )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 10) :
                    alt1 = 2
                elif ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 65535)) :
                    alt1 = 1


                if alt1 == 1:
                    # MFQL.g:548:15: .
                    pass 
                    self.matchAny()


                else:
                    break #loop1
            self.match(10)
            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENTS"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # MFQL.g:549:3: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # MFQL.g:549:5: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # MFQL.g:549:5: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((9 <= LA2_0 <= 10) or LA2_0 == 13 or LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # MFQL.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1
            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # MFQL.g:550:6: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* )
            # MFQL.g:550:8: ( '0' .. '9' )+ '.' ( '0' .. '9' )*
            pass 
            # MFQL.g:550:8: ( '0' .. '9' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # MFQL.g:550:9: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1
            self.match(46)
            # MFQL.g:550:24: ( '0' .. '9' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # MFQL.g:550:25: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop4



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "NUM"
    def mNUM(self, ):

        try:
            _type = NUM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:551:4: ( ( '0' .. '9' )+ )
            # MFQL.g:551:6: ( '0' .. '9' )+
            pass 
            # MFQL.g:551:6: ( '0' .. '9' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57)) :
                    alt5 = 1


                if alt5 == 1:
                    # MFQL.g:551:7: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM"



    # $ANTLR start "ANUM"
    def mANUM(self, ):

        try:
            _type = ANUM
            _channel = DEFAULT_CHANNEL

            # MFQL.g:553:3: ( ( '_' | 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+ | '`' ( '\\\\' . | ~ ( '\\\\' | '\\`' ) )* '`' )
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if ((48 <= LA8_0 <= 57) or (65 <= LA8_0 <= 90) or LA8_0 == 95 or (97 <= LA8_0 <= 122)) :
                alt8 = 1
            elif (LA8_0 == 96) :
                alt8 = 2
            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae

            if alt8 == 1:
                # MFQL.g:553:5: ( '_' | 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+
                pass 
                # MFQL.g:553:5: ( '_' | 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 57) or (65 <= LA6_0 <= 90) or LA6_0 == 95 or (97 <= LA6_0 <= 122)) :
                        alt6 = 1


                    if alt6 == 1:
                        # MFQL.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


            elif alt8 == 2:
                # MFQL.g:554:5: '`' ( '\\\\' . | ~ ( '\\\\' | '\\`' ) )* '`'
                pass 
                self.match(96)
                # MFQL.g:554:9: ( '\\\\' . | ~ ( '\\\\' | '\\`' ) )*
                while True: #loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 92) :
                        alt7 = 1
                    elif ((0 <= LA7_0 <= 91) or (93 <= LA7_0 <= 95) or (97 <= LA7_0 <= 65535)) :
                        alt7 = 2


                    if alt7 == 1:
                        # MFQL.g:554:11: '\\\\' .
                        pass 
                        self.match(92)
                        self.matchAny()


                    elif alt7 == 2:
                        # MFQL.g:554:20: ~ ( '\\\\' | '\\`' )
                        pass 
                        if (0 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 95) or (97 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop7
                self.match(96)


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANUM"



    # $ANTLR start "STR"
    def mSTR(self, ):

        try:
            _type = STR
            _channel = DEFAULT_CHANNEL

            # MFQL.g:557:4: ( '\\'' ( '\\\\' . | ~ ( '\\\\' | '\\'' ) )* '\\'' )
            # MFQL.g:557:7: '\\'' ( '\\\\' . | ~ ( '\\\\' | '\\'' ) )* '\\''
            pass 
            self.match(39)
            # MFQL.g:557:12: ( '\\\\' . | ~ ( '\\\\' | '\\'' ) )*
            while True: #loop9
                alt9 = 3
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 92) :
                    alt9 = 1
                elif ((0 <= LA9_0 <= 38) or (40 <= LA9_0 <= 91) or (93 <= LA9_0 <= 65535)) :
                    alt9 = 2


                if alt9 == 1:
                    # MFQL.g:557:14: '\\\\' .
                    pass 
                    self.match(92)
                    self.matchAny()


                elif alt9 == 2:
                    # MFQL.g:557:23: ~ ( '\\\\' | '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop9
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR"



    # $ANTLR start "DSTR"
    def mDSTR(self, ):

        try:
            _type = DSTR
            _channel = DEFAULT_CHANNEL

            # MFQL.g:558:5: ( '\"' ( '\\\\' . | ~ ( '\\\\' | '\"' ) )* '\"' )
            # MFQL.g:558:7: '\"' ( '\\\\' . | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # MFQL.g:558:11: ( '\\\\' . | ~ ( '\\\\' | '\"' ) )*
            while True: #loop10
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 92) :
                    alt10 = 1
                elif ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 91) or (93 <= LA10_0 <= 65535)) :
                    alt10 = 2


                if alt10 == 1:
                    # MFQL.g:558:13: '\\\\' .
                    pass 
                    self.match(92)
                    self.matchAny()


                elif alt10 == 2:
                    # MFQL.g:558:22: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop10
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DSTR"



    def mTokens(self):
        # MFQL.g:1:8: ( T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | AND | AS | BY | CREATE | DELETE | DISTINCT | DROP | DSTREAM | FALSE | FROM | GROUP | HAVING | HOURS | INPUT | INSERT | INTO | IS | ISTREAM | JOIN | KEY | LEFT | MINUTES | NOT | NOW | NULL | ON | OR | OUTER | OUTPUT | PARTITION | RANGE | RIGHT | RSTREAM | ROWS | SECONDS | SELECT | SET | STREAM | TABLE | TRUE | UNBOUNDED | UPDATE | WHERE | MINUS | PLUS | STAR | SLASH | DOT | DOTDOT | AT | PERCENT | COMMENTS | WS | FLOAT | NUM | ANUM | STR | DSTR )
        alt11 = 76
        alt11 = self.dfa11.predict(self.input)
        if alt11 == 1:
            # MFQL.g:1:10: T__62
            pass 
            self.mT__62()


        elif alt11 == 2:
            # MFQL.g:1:16: T__63
            pass 
            self.mT__63()


        elif alt11 == 3:
            # MFQL.g:1:22: T__64
            pass 
            self.mT__64()


        elif alt11 == 4:
            # MFQL.g:1:28: T__65
            pass 
            self.mT__65()


        elif alt11 == 5:
            # MFQL.g:1:34: T__66
            pass 
            self.mT__66()


        elif alt11 == 6:
            # MFQL.g:1:40: T__67
            pass 
            self.mT__67()


        elif alt11 == 7:
            # MFQL.g:1:46: T__68
            pass 
            self.mT__68()


        elif alt11 == 8:
            # MFQL.g:1:52: T__69
            pass 
            self.mT__69()


        elif alt11 == 9:
            # MFQL.g:1:58: T__70
            pass 
            self.mT__70()


        elif alt11 == 10:
            # MFQL.g:1:64: T__71
            pass 
            self.mT__71()


        elif alt11 == 11:
            # MFQL.g:1:70: T__72
            pass 
            self.mT__72()


        elif alt11 == 12:
            # MFQL.g:1:76: T__73
            pass 
            self.mT__73()


        elif alt11 == 13:
            # MFQL.g:1:82: T__74
            pass 
            self.mT__74()


        elif alt11 == 14:
            # MFQL.g:1:88: T__75
            pass 
            self.mT__75()


        elif alt11 == 15:
            # MFQL.g:1:94: T__76
            pass 
            self.mT__76()


        elif alt11 == 16:
            # MFQL.g:1:100: T__77
            pass 
            self.mT__77()


        elif alt11 == 17:
            # MFQL.g:1:106: T__78
            pass 
            self.mT__78()


        elif alt11 == 18:
            # MFQL.g:1:112: T__79
            pass 
            self.mT__79()


        elif alt11 == 19:
            # MFQL.g:1:118: AND
            pass 
            self.mAND()


        elif alt11 == 20:
            # MFQL.g:1:122: AS
            pass 
            self.mAS()


        elif alt11 == 21:
            # MFQL.g:1:125: BY
            pass 
            self.mBY()


        elif alt11 == 22:
            # MFQL.g:1:128: CREATE
            pass 
            self.mCREATE()


        elif alt11 == 23:
            # MFQL.g:1:135: DELETE
            pass 
            self.mDELETE()


        elif alt11 == 24:
            # MFQL.g:1:142: DISTINCT
            pass 
            self.mDISTINCT()


        elif alt11 == 25:
            # MFQL.g:1:151: DROP
            pass 
            self.mDROP()


        elif alt11 == 26:
            # MFQL.g:1:156: DSTREAM
            pass 
            self.mDSTREAM()


        elif alt11 == 27:
            # MFQL.g:1:164: FALSE
            pass 
            self.mFALSE()


        elif alt11 == 28:
            # MFQL.g:1:170: FROM
            pass 
            self.mFROM()


        elif alt11 == 29:
            # MFQL.g:1:175: GROUP
            pass 
            self.mGROUP()


        elif alt11 == 30:
            # MFQL.g:1:181: HAVING
            pass 
            self.mHAVING()


        elif alt11 == 31:
            # MFQL.g:1:188: HOURS
            pass 
            self.mHOURS()


        elif alt11 == 32:
            # MFQL.g:1:194: INPUT
            pass 
            self.mINPUT()


        elif alt11 == 33:
            # MFQL.g:1:200: INSERT
            pass 
            self.mINSERT()


        elif alt11 == 34:
            # MFQL.g:1:207: INTO
            pass 
            self.mINTO()


        elif alt11 == 35:
            # MFQL.g:1:212: IS
            pass 
            self.mIS()


        elif alt11 == 36:
            # MFQL.g:1:215: ISTREAM
            pass 
            self.mISTREAM()


        elif alt11 == 37:
            # MFQL.g:1:223: JOIN
            pass 
            self.mJOIN()


        elif alt11 == 38:
            # MFQL.g:1:228: KEY
            pass 
            self.mKEY()


        elif alt11 == 39:
            # MFQL.g:1:232: LEFT
            pass 
            self.mLEFT()


        elif alt11 == 40:
            # MFQL.g:1:237: MINUTES
            pass 
            self.mMINUTES()


        elif alt11 == 41:
            # MFQL.g:1:245: NOT
            pass 
            self.mNOT()


        elif alt11 == 42:
            # MFQL.g:1:249: NOW
            pass 
            self.mNOW()


        elif alt11 == 43:
            # MFQL.g:1:253: NULL
            pass 
            self.mNULL()


        elif alt11 == 44:
            # MFQL.g:1:258: ON
            pass 
            self.mON()


        elif alt11 == 45:
            # MFQL.g:1:261: OR
            pass 
            self.mOR()


        elif alt11 == 46:
            # MFQL.g:1:264: OUTER
            pass 
            self.mOUTER()


        elif alt11 == 47:
            # MFQL.g:1:270: OUTPUT
            pass 
            self.mOUTPUT()


        elif alt11 == 48:
            # MFQL.g:1:277: PARTITION
            pass 
            self.mPARTITION()


        elif alt11 == 49:
            # MFQL.g:1:287: RANGE
            pass 
            self.mRANGE()


        elif alt11 == 50:
            # MFQL.g:1:293: RIGHT
            pass 
            self.mRIGHT()


        elif alt11 == 51:
            # MFQL.g:1:299: RSTREAM
            pass 
            self.mRSTREAM()


        elif alt11 == 52:
            # MFQL.g:1:307: ROWS
            pass 
            self.mROWS()


        elif alt11 == 53:
            # MFQL.g:1:312: SECONDS
            pass 
            self.mSECONDS()


        elif alt11 == 54:
            # MFQL.g:1:320: SELECT
            pass 
            self.mSELECT()


        elif alt11 == 55:
            # MFQL.g:1:327: SET
            pass 
            self.mSET()


        elif alt11 == 56:
            # MFQL.g:1:331: STREAM
            pass 
            self.mSTREAM()


        elif alt11 == 57:
            # MFQL.g:1:338: TABLE
            pass 
            self.mTABLE()


        elif alt11 == 58:
            # MFQL.g:1:344: TRUE
            pass 
            self.mTRUE()


        elif alt11 == 59:
            # MFQL.g:1:349: UNBOUNDED
            pass 
            self.mUNBOUNDED()


        elif alt11 == 60:
            # MFQL.g:1:359: UPDATE
            pass 
            self.mUPDATE()


        elif alt11 == 61:
            # MFQL.g:1:366: WHERE
            pass 
            self.mWHERE()


        elif alt11 == 62:
            # MFQL.g:1:372: MINUS
            pass 
            self.mMINUS()


        elif alt11 == 63:
            # MFQL.g:1:378: PLUS
            pass 
            self.mPLUS()


        elif alt11 == 64:
            # MFQL.g:1:383: STAR
            pass 
            self.mSTAR()


        elif alt11 == 65:
            # MFQL.g:1:388: SLASH
            pass 
            self.mSLASH()


        elif alt11 == 66:
            # MFQL.g:1:394: DOT
            pass 
            self.mDOT()


        elif alt11 == 67:
            # MFQL.g:1:398: DOTDOT
            pass 
            self.mDOTDOT()


        elif alt11 == 68:
            # MFQL.g:1:405: AT
            pass 
            self.mAT()


        elif alt11 == 69:
            # MFQL.g:1:408: PERCENT
            pass 
            self.mPERCENT()


        elif alt11 == 70:
            # MFQL.g:1:416: COMMENTS
            pass 
            self.mCOMMENTS()


        elif alt11 == 71:
            # MFQL.g:1:425: WS
            pass 
            self.mWS()


        elif alt11 == 72:
            # MFQL.g:1:428: FLOAT
            pass 
            self.mFLOAT()


        elif alt11 == 73:
            # MFQL.g:1:434: NUM
            pass 
            self.mNUM()


        elif alt11 == 74:
            # MFQL.g:1:438: ANUM
            pass 
            self.mANUM()


        elif alt11 == 75:
            # MFQL.g:1:443: STR
            pass 
            self.mSTR()


        elif alt11 == 76:
            # MFQL.g:1:447: DSTR
            pass 
            self.mDSTR()







    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\4\uffff\1\60\6\uffff\1\63\1\uffff\1\66\24\54\4\uffff\1\134\4\uffff"
        u"\1\135\13\uffff\1\54\1\140\1\141\13\54\1\160\6\54\1\170\1\171\15"
        u"\54\4\uffff\1\u0089\2\uffff\16\54\1\uffff\1\54\1\u0099\2\54\1\u009c"
        u"\1\u009d\1\54\2\uffff\10\54\1\u00a8\6\54\1\uffff\3\54\1\u00b2\2"
        u"\54\1\u00b5\5\54\1\u00bb\1\54\1\u00bd\1\uffff\1\u00be\1\54\2\uffff"
        u"\1\u00c0\6\54\1\u00c7\2\54\1\uffff\2\54\1\u00cc\6\54\1\uffff\1"
        u"\54\1\u00d4\1\uffff\1\u00d5\1\54\1\u00d7\1\u00d8\1\54\1\uffff\1"
        u"\54\2\uffff\1\54\1\uffff\1\u00dc\2\54\1\u00df\1\u00e0\1\54\1\uffff"
        u"\3\54\1\u00e5\1\uffff\2\54\1\u00e8\1\u00e9\1\u00ea\2\54\2\uffff"
        u"\1\u00ed\2\uffff\1\u00ee\2\54\1\uffff\1\u00f1\1\54\2\uffff\2\54"
        u"\1\u00f5\1\u00f6\1\uffff\1\54\1\u00f8\3\uffff\1\54\1\u00fa\2\uffff"
        u"\1\u00fb\1\u00fc\1\uffff\1\54\1\u00fe\1\u00ff\2\uffff\1\54\1\uffff"
        u"\1\u0101\3\uffff\1\54\2\uffff\1\54\1\uffff\1\u0104\1\u0105\2\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\u0106\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\11\3\uffff\1\75\6\uffff\1\75\1\uffff\1\74\1\116\1\131\1\122"
        u"\1\105\1\101\1\122\1\101\1\116\1\117\2\105\1\111\1\117\1\116\2"
        u"\101\1\105\1\101\1\116\1\110\4\uffff\1\56\4\uffff\1\56\13\uffff"
        u"\1\104\2\60\1\105\1\114\1\123\1\117\1\124\1\114\2\117\1\126\1\125"
        u"\1\120\1\60\1\111\1\131\1\106\1\116\1\124\1\114\2\60\1\124\1\122"
        u"\1\116\1\107\1\124\1\127\1\103\1\122\1\102\1\125\1\102\1\104\1"
        u"\105\4\uffff\1\60\2\uffff\1\101\1\105\1\124\1\120\1\122\1\123\1"
        u"\115\1\125\1\111\1\122\1\125\1\105\1\117\1\122\1\uffff\1\116\1"
        u"\60\1\124\1\125\2\60\1\114\2\uffff\1\105\1\124\1\107\1\110\1\122"
        u"\1\123\1\117\1\105\1\60\1\105\1\114\1\105\1\117\1\101\1\122\1\uffff"
        u"\2\124\1\111\1\60\2\105\1\60\1\120\1\116\1\123\1\124\1\122\1\60"
        u"\1\105\1\60\1\uffff\1\60\1\124\2\uffff\1\60\1\122\1\125\1\111\1"
        u"\105\1\124\1\105\1\60\1\116\1\103\1\uffff\1\101\1\105\1\60\1\125"
        u"\1\124\3\105\1\116\1\uffff\1\101\1\60\1\uffff\1\60\1\107\2\60\1"
        u"\124\1\uffff\1\101\2\uffff\1\105\1\uffff\1\60\2\124\2\60\1\101"
        u"\1\uffff\1\104\1\124\1\115\1\60\1\uffff\1\116\1\105\3\60\1\103"
        u"\1\115\2\uffff\1\60\2\uffff\1\60\1\115\1\123\1\uffff\1\60\1\111"
        u"\2\uffff\1\115\1\123\2\60\1\uffff\1\104\1\60\3\uffff\1\124\1\60"
        u"\2\uffff\2\60\1\uffff\1\117\2\60\2\uffff\1\105\1\uffff\1\60\3\uffff"
        u"\1\116\2\uffff\1\104\1\uffff\2\60\2\uffff"
        )

    DFA11_max = DFA.unpack(
        u"\1\175\3\uffff\1\75\6\uffff\1\76\1\uffff\1\75\1\163\1\171\1\162"
        u"\1\163\2\162\1\157\1\163\1\157\2\145\1\151\2\165\1\141\1\163\1"
        u"\164\1\162\1\160\1\150\4\uffff\1\56\4\uffff\1\172\13\uffff\1\144"
        u"\2\172\1\145\1\154\1\163\1\157\1\164\1\154\2\157\1\166\1\165\1"
        u"\164\1\172\1\151\1\171\1\146\1\156\1\167\1\154\2\172\1\164\1\162"
        u"\1\156\1\147\1\164\1\167\1\164\1\162\1\142\1\165\1\142\1\144\1"
        u"\145\4\uffff\1\172\2\uffff\1\141\1\145\1\164\1\160\1\162\1\163"
        u"\1\155\1\165\1\151\1\162\1\165\1\145\1\157\1\162\1\uffff\1\156"
        u"\1\172\1\164\1\165\2\172\1\154\2\uffff\1\160\1\164\1\147\1\150"
        u"\1\162\1\163\1\157\1\145\1\172\1\145\1\154\1\145\1\157\1\141\1"
        u"\162\1\uffff\2\164\1\151\1\172\2\145\1\172\1\160\1\156\1\163\1"
        u"\164\1\162\1\172\1\145\1\172\1\uffff\1\172\1\164\2\uffff\1\172"
        u"\1\162\1\165\1\151\1\145\1\164\1\145\1\172\1\156\1\143\1\uffff"
        u"\1\141\1\145\1\172\1\165\1\164\3\145\1\156\1\uffff\1\141\1\172"
        u"\1\uffff\1\172\1\147\2\172\1\164\1\uffff\1\141\2\uffff\1\145\1"
        u"\uffff\1\172\2\164\2\172\1\141\1\uffff\1\144\1\164\1\155\1\172"
        u"\1\uffff\1\156\1\145\3\172\1\143\1\155\2\uffff\1\172\2\uffff\1"
        u"\172\1\155\1\163\1\uffff\1\172\1\151\2\uffff\1\155\1\163\2\172"
        u"\1\uffff\1\144\1\172\3\uffff\1\164\1\172\2\uffff\2\172\1\uffff"
        u"\1\157\2\172\2\uffff\1\145\1\uffff\1\172\3\uffff\1\156\2\uffff"
        u"\1\144\1\uffff\2\172\2\uffff"
        )

    DFA11_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\7\1\10\1\11\1\12\1\uffff"
        u"\1\17\25\uffff\1\76\1\77\1\100\1\101\1\uffff\1\104\1\105\1\106"
        u"\1\107\1\uffff\1\112\1\113\1\114\1\15\1\4\1\14\1\16\1\13\1\20\1"
        u"\22\1\21\44\uffff\1\103\1\102\1\111\1\110\1\uffff\1\24\1\25\16"
        u"\uffff\1\43\7\uffff\1\54\1\55\17\uffff\1\23\17\uffff\1\46\2\uffff"
        u"\1\51\1\52\12\uffff\1\67\11\uffff\1\31\2\uffff\1\34\5\uffff\1\42"
        u"\1\uffff\1\45\1\47\1\uffff\1\53\6\uffff\1\64\4\uffff\1\72\7\uffff"
        u"\1\33\1\35\1\uffff\1\37\1\40\3\uffff\1\56\2\uffff\1\61\1\62\4\uffff"
        u"\1\71\2\uffff\1\75\1\26\1\27\2\uffff\1\36\1\41\2\uffff\1\57\3\uffff"
        u"\1\66\1\70\1\uffff\1\74\1\uffff\1\32\1\44\1\50\1\uffff\1\63\1\65"
        u"\1\uffff\1\30\2\uffff\1\60\1\73"
        )

    DFA11_special = DFA.unpack(
        u"\u0106\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\2\52\2\uffff\1\52\22\uffff\1\52\1\14\1\56\1\51\1\uffff"
        u"\1\50\1\uffff\1\55\1\2\1\3\1\44\1\43\1\5\1\42\1\46\1\45\12\53\1"
        u"\11\1\1\1\13\1\4\1\15\1\uffff\1\47\1\16\1\17\1\20\1\21\1\54\1\22"
        u"\1\23\1\24\1\25\1\26\1\27\1\30\1\31\1\32\1\33\1\34\1\54\1\35\1"
        u"\36\1\37\1\40\1\54\1\41\3\54\1\6\1\uffff\1\7\1\uffff\2\54\1\16"
        u"\1\17\1\20\1\21\1\54\1\22\1\23\1\24\1\25\1\26\1\27\1\30\1\31\1"
        u"\32\1\33\1\34\1\54\1\35\1\36\1\37\1\40\1\54\1\41\3\54\1\10\1\uffff"
        u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65\1\64"),
        DFA.unpack(u"\1\67\4\uffff\1\70\32\uffff\1\67\4\uffff\1\70"),
        DFA.unpack(u"\1\71\37\uffff\1\71"),
        DFA.unpack(u"\1\72\37\uffff\1\72"),
        DFA.unpack(u"\1\73\3\uffff\1\74\10\uffff\1\75\1\76\21\uffff\1\73"
        u"\3\uffff\1\74\10\uffff\1\75\1\76"),
        DFA.unpack(u"\1\77\20\uffff\1\100\16\uffff\1\77\20\uffff\1\100"),
        DFA.unpack(u"\1\101\37\uffff\1\101"),
        DFA.unpack(u"\1\102\15\uffff\1\103\21\uffff\1\102\15\uffff\1\103"),
        DFA.unpack(u"\1\104\4\uffff\1\105\32\uffff\1\104\4\uffff\1\105"),
        DFA.unpack(u"\1\106\37\uffff\1\106"),
        DFA.unpack(u"\1\107\37\uffff\1\107"),
        DFA.unpack(u"\1\110\37\uffff\1\110"),
        DFA.unpack(u"\1\111\37\uffff\1\111"),
        DFA.unpack(u"\1\112\5\uffff\1\113\31\uffff\1\112\5\uffff\1\113"),
        DFA.unpack(u"\1\114\3\uffff\1\115\2\uffff\1\116\30\uffff\1\114\3"
        u"\uffff\1\115\2\uffff\1\116"),
        DFA.unpack(u"\1\117\37\uffff\1\117"),
        DFA.unpack(u"\1\120\7\uffff\1\121\5\uffff\1\123\3\uffff\1\122\15"
        u"\uffff\1\120\7\uffff\1\121\5\uffff\1\123\3\uffff\1\122"),
        DFA.unpack(u"\1\124\16\uffff\1\125\20\uffff\1\124\16\uffff\1\125"),
        DFA.unpack(u"\1\126\20\uffff\1\127\16\uffff\1\126\20\uffff\1\127"),
        DFA.unpack(u"\1\130\1\uffff\1\131\35\uffff\1\130\1\uffff\1\131"),
        DFA.unpack(u"\1\132\37\uffff\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\136\1\uffff\12\53\7\uffff\32\54\4\uffff\1\54\1\uffff"
        u"\32\54"),
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
        DFA.unpack(u"\1\137\37\uffff\1\137"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\142\37\uffff\1\142"),
        DFA.unpack(u"\1\143\37\uffff\1\143"),
        DFA.unpack(u"\1\144\37\uffff\1\144"),
        DFA.unpack(u"\1\145\37\uffff\1\145"),
        DFA.unpack(u"\1\146\37\uffff\1\146"),
        DFA.unpack(u"\1\147\37\uffff\1\147"),
        DFA.unpack(u"\1\150\37\uffff\1\150"),
        DFA.unpack(u"\1\151\37\uffff\1\151"),
        DFA.unpack(u"\1\152\37\uffff\1\152"),
        DFA.unpack(u"\1\153\37\uffff\1\153"),
        DFA.unpack(u"\1\154\2\uffff\1\155\1\156\33\uffff\1\154\2\uffff\1"
        u"\155\1\156"),
        DFA.unpack(u"\12\54\7\uffff\23\54\1\157\6\54\4\uffff\1\54\1\uffff"
        u"\23\54\1\157\6\54"),
        DFA.unpack(u"\1\161\37\uffff\1\161"),
        DFA.unpack(u"\1\162\37\uffff\1\162"),
        DFA.unpack(u"\1\163\37\uffff\1\163"),
        DFA.unpack(u"\1\164\37\uffff\1\164"),
        DFA.unpack(u"\1\165\2\uffff\1\166\34\uffff\1\165\2\uffff\1\166"),
        DFA.unpack(u"\1\167\37\uffff\1\167"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\172\37\uffff\1\172"),
        DFA.unpack(u"\1\173\37\uffff\1\173"),
        DFA.unpack(u"\1\174\37\uffff\1\174"),
        DFA.unpack(u"\1\175\37\uffff\1\175"),
        DFA.unpack(u"\1\176\37\uffff\1\176"),
        DFA.unpack(u"\1\177\37\uffff\1\177"),
        DFA.unpack(u"\1\u0080\10\uffff\1\u0081\7\uffff\1\u0082\16\uffff"
        u"\1\u0080\10\uffff\1\u0081\7\uffff\1\u0082"),
        DFA.unpack(u"\1\u0083\37\uffff\1\u0083"),
        DFA.unpack(u"\1\u0084\37\uffff\1\u0084"),
        DFA.unpack(u"\1\u0085\37\uffff\1\u0085"),
        DFA.unpack(u"\1\u0086\37\uffff\1\u0086"),
        DFA.unpack(u"\1\u0087\37\uffff\1\u0087"),
        DFA.unpack(u"\1\u0088\37\uffff\1\u0088"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008a\37\uffff\1\u008a"),
        DFA.unpack(u"\1\u008b\37\uffff\1\u008b"),
        DFA.unpack(u"\1\u008c\37\uffff\1\u008c"),
        DFA.unpack(u"\1\u008d\37\uffff\1\u008d"),
        DFA.unpack(u"\1\u008e\37\uffff\1\u008e"),
        DFA.unpack(u"\1\u008f\37\uffff\1\u008f"),
        DFA.unpack(u"\1\u0090\37\uffff\1\u0090"),
        DFA.unpack(u"\1\u0091\37\uffff\1\u0091"),
        DFA.unpack(u"\1\u0092\37\uffff\1\u0092"),
        DFA.unpack(u"\1\u0093\37\uffff\1\u0093"),
        DFA.unpack(u"\1\u0094\37\uffff\1\u0094"),
        DFA.unpack(u"\1\u0095\37\uffff\1\u0095"),
        DFA.unpack(u"\1\u0096\37\uffff\1\u0096"),
        DFA.unpack(u"\1\u0097\37\uffff\1\u0097"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0098\37\uffff\1\u0098"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u009a\37\uffff\1\u009a"),
        DFA.unpack(u"\1\u009b\37\uffff\1\u009b"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u009e\37\uffff\1\u009e"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009f\12\uffff\1\u00a0\24\uffff\1\u009f\12\uffff"
        u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1\37\uffff\1\u00a1"),
        DFA.unpack(u"\1\u00a2\37\uffff\1\u00a2"),
        DFA.unpack(u"\1\u00a3\37\uffff\1\u00a3"),
        DFA.unpack(u"\1\u00a4\37\uffff\1\u00a4"),
        DFA.unpack(u"\1\u00a5\37\uffff\1\u00a5"),
        DFA.unpack(u"\1\u00a6\37\uffff\1\u00a6"),
        DFA.unpack(u"\1\u00a7\37\uffff\1\u00a7"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00a9\37\uffff\1\u00a9"),
        DFA.unpack(u"\1\u00aa\37\uffff\1\u00aa"),
        DFA.unpack(u"\1\u00ab\37\uffff\1\u00ab"),
        DFA.unpack(u"\1\u00ac\37\uffff\1\u00ac"),
        DFA.unpack(u"\1\u00ad\37\uffff\1\u00ad"),
        DFA.unpack(u"\1\u00ae\37\uffff\1\u00ae"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00af\37\uffff\1\u00af"),
        DFA.unpack(u"\1\u00b0\37\uffff\1\u00b0"),
        DFA.unpack(u"\1\u00b1\37\uffff\1\u00b1"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00b3\37\uffff\1\u00b3"),
        DFA.unpack(u"\1\u00b4\37\uffff\1\u00b4"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00b6\37\uffff\1\u00b6"),
        DFA.unpack(u"\1\u00b7\37\uffff\1\u00b7"),
        DFA.unpack(u"\1\u00b8\37\uffff\1\u00b8"),
        DFA.unpack(u"\1\u00b9\37\uffff\1\u00b9"),
        DFA.unpack(u"\1\u00ba\37\uffff\1\u00ba"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00bc\37\uffff\1\u00bc"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00bf\37\uffff\1\u00bf"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00c1\37\uffff\1\u00c1"),
        DFA.unpack(u"\1\u00c2\37\uffff\1\u00c2"),
        DFA.unpack(u"\1\u00c3\37\uffff\1\u00c3"),
        DFA.unpack(u"\1\u00c4\37\uffff\1\u00c4"),
        DFA.unpack(u"\1\u00c5\37\uffff\1\u00c5"),
        DFA.unpack(u"\1\u00c6\37\uffff\1\u00c6"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00c8\37\uffff\1\u00c8"),
        DFA.unpack(u"\1\u00c9\37\uffff\1\u00c9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ca\37\uffff\1\u00ca"),
        DFA.unpack(u"\1\u00cb\37\uffff\1\u00cb"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00cd\37\uffff\1\u00cd"),
        DFA.unpack(u"\1\u00ce\37\uffff\1\u00ce"),
        DFA.unpack(u"\1\u00cf\37\uffff\1\u00cf"),
        DFA.unpack(u"\1\u00d0\37\uffff\1\u00d0"),
        DFA.unpack(u"\1\u00d1\37\uffff\1\u00d1"),
        DFA.unpack(u"\1\u00d2\37\uffff\1\u00d2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d3\37\uffff\1\u00d3"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00d6\37\uffff\1\u00d6"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00d9\37\uffff\1\u00d9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00da\37\uffff\1\u00da"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00db\37\uffff\1\u00db"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00dd\37\uffff\1\u00dd"),
        DFA.unpack(u"\1\u00de\37\uffff\1\u00de"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00e1\37\uffff\1\u00e1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e2\37\uffff\1\u00e2"),
        DFA.unpack(u"\1\u00e3\37\uffff\1\u00e3"),
        DFA.unpack(u"\1\u00e4\37\uffff\1\u00e4"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e6\37\uffff\1\u00e6"),
        DFA.unpack(u"\1\u00e7\37\uffff\1\u00e7"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00eb\37\uffff\1\u00eb"),
        DFA.unpack(u"\1\u00ec\37\uffff\1\u00ec"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00ef\37\uffff\1\u00ef"),
        DFA.unpack(u"\1\u00f0\37\uffff\1\u00f0"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00f2\37\uffff\1\u00f2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f3\37\uffff\1\u00f3"),
        DFA.unpack(u"\1\u00f4\37\uffff\1\u00f4"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f7\37\uffff\1\u00f7"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f9\37\uffff\1\u00f9"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fd\37\uffff\1\u00fd"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0100\37\uffff\1\u0100"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0102\37\uffff\1\u0102"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0103\37\uffff\1\u0103"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(MFQLLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
