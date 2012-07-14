from taj.exception import IllegalCondition
from taj.operator.join import BinaryJoin
from taj.operator.table import RelationProxy
from taj.operator.window import TimedWindowOperator, AmountWindowOperator
from taj.parser.visitor import LogicVisitor, ExpressionVisitor, QueryVisitor

class JoinBuilder(QueryVisitor):
    '''
    a visitor that when visiting AST will record all joins.
    TODO: it should 
    '''
    
    def __init__(self):
        ''' ctor '''
        super(JoinBuilder, self).__init__()
        self.__acc        = None # storing the actual join
        self.__inputs     = None # storing the name of the leafs
        self._lastStrName = None
        self.__expr       = AccessExtractor()
        self.__activeExpr = False # should the acessExtractor visit

    def getResult(self):
        '''
        returns the join that has been built during visit.
        '''
        if self.__acc is None:
            raise IllegalCondition("getResult without entering relation")
        if len(self.__acc) != 1:
            raise IllegalCondition("incomplete join expression detected")
        return self.__acc.pop()
    
    def getInputRelations(self):
        '''
        @return: a list of the input relations that have been used to build
                 the join.
        @rtype: list<(string, Relation)>
        '''
        if self.__inputs is None:
            raise IllegalCondition("getInputRelations without entering relation")
        return self.__inputs
    
    def enterSourceRelation(self):
        self.__acc    = []
        self.__inputs = list()
        
    def enterSimpleRelation(self, name):
        rel = RelationProxy()
        rel.setName(name)
        self.__acc.append(rel)
        self.__inputs.append((name, rel))
    
    def enterSimpleStream(self, name):
        self._lastStrName = name
        raise NotImplementedError()
    
    def enterRelationRename(self):
        pass
    
    def leaveRelationRename(self):
        pass
    
    def enterTimedWindow(self, time):
        win = TimedWindowOperator()
        win.setTime(time)
        win.setName(self._lastStrName)
        self._lastStrName = None
        self.__acc.append(win)
        self.__inputs.append((self._lastStrName, win))
    
    def enterAmountWindow(self, amount):
        win = AmountWindowOperator()
        win.setAmount(amount)
        win.setName(self._lastStrName)
        self._lastStrName = None
        self.__acc.append(win)
        self.__inputs.append((self._lastStrName, win))
    
    def enterRelationComposition(self):
        self.__activeExpr = True
        self.__expr.reset()
        self.__acc.append(BinaryJoin())

    def leaveRelationComposition(self):
        self.__activeExpr = False
        pass

    def crossJoin(self):
        rel = self.__acc.pop()
        self.__acc[-1].addEventSource(rel)
    
    def acceptLogic(self, logic):
        if not self.__activeExpr: return
        logic.walk(self.__expr)
    
    def acceptExpression(self, expr):
        if not self.__activeExpr: return
        expr.walk(self.__expr)
    
class AccessExtractor(LogicVisitor, ExpressionVisitor):
    '''
    extracts the logical part of join selection so that it can report it to
    other components. 
    '''

    def __init__(self):
        super(AccessExtractor, self).__init__()

    def reset(self):
        '''
        forget about all input relations.
        '''
        pass