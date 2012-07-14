from taj.exception import InconsistentExpression
from taj.parser.base import ASTNode

class Expression(ASTNode):
    
    def __init__(self):
        super(Expression, self).__init__()

class Pattern(Expression):
    '''
    '''
    
    def getMembers(self):
        return self._members

class Array(Pattern):
    '''
    representation of an array of constants
    '''
    def __init__(self):
        super(Array, self).__init__()
        self._members = []
    
    def add(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression()
        self._members.append(expr)
    
    def walk(self, visitor):
        visitor.enterArray()
        for elem in self._members:
            elem.walk(visitor)
            visitor.next()
        visitor.leaveArray()

class Map(Pattern):
    
    def __init__(self):
        super(Map, self).__init__()
        self._members = {}
    
    def put(self, name, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression()
        if self._members.has_key(name):
            raise InconsistentExpression('object with multiple property "%s"' % name)
        self._members[name] = expr

    def walk(self, visitor):
        visitor.enterMap()
        for (key, value) in self._members.iteritems():
            value.walk(visitor)
            visitor.next(key)
        visitor.leaveMap()

class NamedExpression(Expression):
    
    def __init__(self, name=None):
        super(NamedExpression, self).__init__()
        self._name = name
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name
        
# class Variable(NamedExpression): pass

class Constant(Expression):
    
    def __init__(self, value):
        super(Constant, self).__init__()
        self._value = value
    
    def setValue(self, obj):
        self._value = obj
        
    def getValue(self):
        return self._value

    def __str__(self):
        return str(self._value)

class NullConstant(Constant):
    
    def __init__(self):
        super(NullConstant, self).__init__(None)

    def __str__(self):
        return 'NULL'
    
    def walk(self, visitor):
        visitor.nullConstant()

class Integer(Constant):
    
    def __init__(self, value):
        super(Integer, self).__init__(value)
        assert isinstance(value, int)

    def walk(self, visitor):
        visitor.intConstant(self._value)

class String(Constant):
    
    def __str__(self):
        return '"%s"' % self._value

    def walk(self, visitor):
        visitor.stringConstant(self._value)

class Float(Constant):
    
    def walk(self, visitor):
        visitor.floatConstant(self._value)

class Summ(Expression):
    
    ADD = 1
    SUB = 2
    
    def __init__(self):
        super(Summ, self).__init__()
        self._members = []
    
    def add(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression(type(expr))
        self._members.append((Summ.ADD, expr))

    def sub(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression(type(expr))
        self._members.append((Summ.SUB, expr))
    
    def getMembers(self):
        return self._members
    
    def walk(self, visitor):
        visitor.enterSumm()
        for (type, elem) in self._members:
#            if type == Summ.ADD:
#                visitor.enterAdd()
#            else:
#                visitor.enterSub()
            elem.walk(visitor)
            if type == Summ.ADD:
                visitor.leaveAdd()
            else:
                visitor.leaveSub()
        visitor.leaveSumm()

class Product(Expression):
    
    MULT = 1
    DIV  = 2
    MOD  = 3
    
    def __init__(self):
        super(Product, self).__init__()
        self._members = []
    
    def multiply(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression(type(expr))
        self._members.append((Product.MULT, expr))

    def divide(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression(type(expr))
        self._members.append((Product.DIV, expr))
    
    def modulo(self, expr):
        if not isinstance(expr, Expression):
            raise InconsistentExpression(type(expr))
        self._members.append((Product.MOD, expr))

    def getMembers(self):
        return self._members

    def walk(self, visitor):
        visitor.enterProduct()
        for (type, elem) in self._members:
            elem.walk(visitor)
            if type == Product.MULT:
                visitor.leaveMult()
            elif type == Product.DIV:
                visitor.leaveDiv()
            else:
                visitor.leaveMod()
        visitor.leaveProduct()

class Function(NamedExpression):
    
    def __init__(self, name):
        super(Function, self).__init__(name)
        self._args = []

    def setArguments(self, exprs):
        for expr in exprs:
            if not isinstance(expr, Expression):
                raise InconsistentExpression(type(expr))
        self._args = exprs

    def getArguments(self):
        return self._args
    
    def walk(self, visitor):
        visitor.enterFunction(self.getName(), len(self._args))
        for elem in self._args:
            elem.walk(visitor)
        visitor.leaveFunction(self.getName(), len(self._args))
