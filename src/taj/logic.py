from taj.exception import InconsistentExpression
from taj.expr import Expression, Constant
from taj.parser.base import ASTNode

class Predicate(ASTNode):
    
    def __init__(self):
        super(Predicate, self).__init__()
        self._members = []
        
    def add(self, elem):
        if not isinstance(elem, Predicate):
            raise InconsistentExpression(type(elem))
        self._members.append(elem)
    
    def getMembers(self):
        return self._members

class Boolean(Constant, Predicate):
    '''
    the basic type for expressing boolean constants
    '''
    
    def walk(self, visitor):
        visitor.boolConstant(self._value)

class IsNull(Predicate):
    
    def __init__(self, expr):
        super(IsNull, self).__init__()
        self._expr = expr
    
    def getExpression(self):
        return self._expr
    
    def walk(self, visitor):
        visitor.enterIsNull()
        visitor.acceptExpression(self._expr)
        visitor.leaveIsNull()

class IsKey(Predicate):
    
    def __init__(self, var):
        super(IsKey, self).__init__()
#        if not isinstance(var, Selector):
#            raise InconsistentExpression(var)
        self._var = var
    
    def getVariable(self):
        return self._var

    def walk(self, visitor):
        visitor.enterIsKey()
        visitor.acceptExpression(self._var)
        visitor.leaveIsKey()

class Comparaison(Predicate):
    
    LESS          = 1
    LESS_EQUAL    = 2 
    EQUAL         = 3
    UNEQUAL       = 4
    GREATER_EQUAL = 5
    GREATER       = 6
    SIMILAR       = 7
    
    def __init__(self, op, lvalue, rvalue):
        if op is None:
            raise InconsistentExpression('comp op is None')
        if not isinstance(lvalue, Expression):
            raise InconsistentExpression(type(lvalue))
        if not isinstance(rvalue, Expression):
            raise InconsistentExpression(type(rvalue))
        self._op     = op
        self._lvalue = lvalue
        self._rvalue = rvalue
    
    def getOperation(self):
        return self._op
    
    def getLValue(self):
        return self._lvalue
    
    def getRValue(self):
        return self._rvalue
    
    def walk(self, visitor):
        visitor.enterComparaison(self._op)
        visitor.acceptExpression(self._lvalue)
        visitor.rvalue()
        visitor.acceptExpression(self._rvalue)
        visitor.leaveComparaison(self._op)


class Conjunction(Predicate):
    
    def walk(self, visitor):
        visitor.enterConjunction()
        for member in self.getMembers():
            member.walk(visitor)
            visitor.operate()
        visitor.leaveConjunction()
    
class Disjunction(Predicate):

    def walk(self, visitor):
        visitor.enterDisjunction()
        for member in self.getMembers():
            member.walk(visitor)
            visitor.operate()
        visitor.leaveDisjunction()
    
class Negation(Predicate):
    
    def __init__(self, val):
        super(Negation, self).__init__()
        if not isinstance(val, Predicate):
            raise InconsistentExpression(type(val))
        self._val = val

    def getValue(self):
        return self._val
    
    def walk(self, visitor):
        self._val.walk(visitor)
        visitor.leaveNegation()
