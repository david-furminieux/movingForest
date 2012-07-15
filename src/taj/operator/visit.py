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
        self.__newName    = False # should the next expression be interpreted as a name
        self.__lastRel    = None  # last impl of relation visited

        self._props       = {}
        self._toStart     = []
        
    def init(self, props):
        self._props = props
        self.__expr.init(props)

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
    
    def getOperatorsToBeStarted(self):
        return self._toStart
    
    def enterSourceRelation(self):
        self.__acc    = []
        self.__inputs = list()
        
    def enterSimpleRelOrStrRef(self, name):
        proxy = RelationProxy()
        self._toStart.append(proxy)
        proxy.init(self._props)
        self.__lastRel = proxy
        self.__lastRel.setName(name)
        self.__acc.append(self.__lastRel)
        self.__inputs.append((name, self.__lastRel))
    
    def enterRelationRename(self):
        self.__newName = True
    
    def leaveRelationRename(self):
        self.__lastRel.setName(self.__newName)
        self.__newName = False
    
    def enterTimedWindow(self, time):
        win = TimedWindowOperator()
        self._toStart.append(win)
        win.init(self._props)
        win.setTime(time)
        win.setName(self._lastStrName)
        self._lastStrName = None
        self.__acc.append(win)
        self.__inputs.append((self._lastStrName, win))
    
    def enterAmountWindow(self, amount):
        win = AmountWindowOperator()
        win.init(self._props)
        self._toStart.append(win)
        win.setAmount(amount)
        win.setName(self._lastStrName)
        self._lastStrName = None
        self.__acc.append(win)
        self.__inputs.append((self._lastStrName, win))
    
    def enterRelationComposition(self):
        self.__activeExpr = True
        self.__expr.reset()
        
        join = BinaryJoin()
        join.init(self._props)
        self._toStart.append(join)
        self.__acc.append(join)

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
        if self.__newName is True:
            self.__newName = expr
        if not self.__activeExpr: return
        expr.walk(self.__expr)
    
class AccessExtractor(LogicVisitor, ExpressionVisitor):
    '''
    extracts the logical part of join selection so that it can report it to
    other components. 
    '''

    def __init__(self):
        super(AccessExtractor, self).__init__()
        self._props = {}
    
    def init(self, props):
        self._props = props

    def reset(self):
        '''
        forget about all input relations.
        '''
        pass