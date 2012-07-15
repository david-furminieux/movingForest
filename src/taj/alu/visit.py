from taj.exception import InternalError, InconsistentPredicateException
from taj.parser.visitor import ExpressionVisitor, LogicVisitor
from taj.path import IdxAccess, AttributeAccess

class ExpressionEvalBuilder(ExpressionVisitor):
    '''
    this will create an expression evaluator while traversing a Expression AST
    '''
    
    def __init__(self, alu):
        super(ExpressionEvalBuilder, self).__init__()
        self._alu = alu
        self._stack = []

        self._ops = []
        self._path = None
        
        self._firstStack = []
        
    def getResult(self, popAtEnd=True):
        def applyOps(ops, tree):
            for op in ops:
                op(tree)
            if popAtEnd:
                return self._alu.pop()
        ops = self._ops
        self._ops = []
        return lambda tree: applyOps(ops, tree)

    def enterPath(self):
        self._path = []
    
    def attributeAccess(self, name):
        self._path.append(name)

    def idxAccess(self, idx):
        self._path.append(idx)

    def leavePath(self):
        cpy = list()
        cpy.extend(self._path)
        def accessTree(tree, stack, path):
            val = stack.accessTree(tree, cpy)
            stack.push(val)
            return stack
        self._ops.append(lambda tree: accessTree(tree, self._alu, cpy))
        
    def enterSumm(self):
        self._firstStack.append(True)

    def leaveSumm(self):
        self._firstStack.pop()
    
    def leaveAdd(self):
        if self._firstStack[-1]:
            self._firstStack[-1] = False
        else:
            self._ops.append(lambda tree: self._alu.add())
    
    def leaveSub(self):
        if self._firstStack[-1]:
            self._firstStack[-1] = False
        else:
            self._ops.append(lambda tree: self._alu.sub())
    
    def enterProduct(self):
        self._firstStack.append(True)

    def leaveProduct(self):
        self._firstStack.pop()
    
    def leaveMult(self):
        if self._firstStack[-1]:
            self._firstStack[-1] = False
        else:
            self._ops.append(lambda tree: self._alu.mult())
    
    def leaveDiv(self):
        if self._firstStack[-1]:
            self._firstStack[-1] = False
        else:
            self._ops.append(lambda tree: self._alu.div())
    
    def leaveMod(self):
        if self._firstStack[-1]:
            self._firstStack[-1] = False
        else:
            self._ops.append(lambda tree: self._alu.mod())
    
    def enterArray(self):
        self._ops.append(lambda tree: self._alu.push([]))
    
    def enterMap(self):
        self._ops.append(lambda tree: self._alu.push({}))
    
    def next(self, name=None):
        def attachNamed(name):
            val = self._alu.pop()
            self._alu.top()[name] = val
        def attachLast():
            val = self._alu.pop()
            self._alu.top().append(val)
        if name is None:
            self._ops.append(lambda tree: attachLast())
        else:
            self._ops.append(lambda tree: attachNamed(name))
    
    def leaveArray(self):
        pass
    
    def leaveMap(self):
        pass
    
    def nullConstant(self):
        self._ops.append(lambda tree: self._alu.push(None))

    def intConstant(self, value):
        self._ops.append(lambda tree: self._alu.push(value))

    def stringConstant(self, value):
        self._ops.append(lambda tree: self._alu.push(value))

    def floatConstant(self, value):
        self._ops.append(lambda tree: self._alu.push(value))

    def boolConstant(self, value):
        self._ops.append(lambda tree: self._alu.push(value))

    def enterFunction(self, name, arity):
#        self._actualFunc = self._alu.checkFunction(name, arity)
#        self._actualFuncArith = arity
        pass
    
    def leaveFunction(self, name, arity):
        func = self._alu.checkFunction(name, arity)
        self._ops.append(lambda tree: self._alu.callFunction(func, arity))
    
class LogicBuilder(LogicVisitor):
    '''
    a visitor that "compiles" logical expression to lambda expressions.
    '''

    AND = 1
    OR  = 2

    def __init__(self, alu):
        super(LogicBuilder, self).__init__()
        
        self._expr = ExpressionEvalBuilder(alu)
        
        self._alu           = alu
        self._ops           = []
        self._actualCompOp  = None
        self._actualLogicOp = None
        self._isKeyCheck    = False
        self._isKeyPath     = None

    def getResult(self):
        def applyOps(ops, tree):
            for op in ops:
                op(tree)
            return self._alu.pop()
        ops = list()
        ops.extend(self._ops)
        return lambda tree: applyOps(ops, tree)

    def enterComparaison(self, operator):
        self._actualCompOp = operator
    
    def leaveComparaison(self, operator):
        self._ops.append(lambda tree: self._alu.compare(operator))

    def enterConjunction(self):
        self._actualLogicOp = LogicBuilder.AND
        self._ops.append(lambda tree: self._alu.push(True))
    
    def enterDisjunction(self):
        self._actualLogicOp = LogicBuilder.OR
        self._ops.append(lambda tree: self._alu.push(False))
    
    def operate(self):
        '''
        SINCE OPERATE IS COMMON ON BOTH "AND" AND "OR" YOU SHOULD BE ABLE TO
        CONSTRUCT INVALID FORMULAE
        '''
        if self._actualLogicOp == LogicBuilder.AND:
            self._ops.append(lambda tree: self._alu.land())
        elif self._actualLogicOp == LogicBuilder.OR:
            self._ops.append(lambda tree: self._alu.lor())
        else:
            raise InternalError()
    
    def leaveIsNull(self):
        alu = self._alu
        self._ops.append(lambda tree: alu.push(alu.pop() is None))
    
    def enterIsKey(self):
        self._isKeyCheck = True
        self._isKeyPath  = None
    
    def leaveIsKey(self):
        path = list()
        path.extend(self._isKeyPath)
        self._isKeyCheck = False
        self._ops.append(lambda tree: self._alu.push(self._alu.checkTree(tree, path)))
    
    def leaveNegation(self):
        self._ops.append(lambda tree: self._alu.lnot())

    def acceptExpression(self, expr):
        if self._isKeyCheck:
            self._isKeyPath = self._extractPath(expr)
        else:
            expr.walk(self._expr)
            self._ops.append(self._expr.getResult(False))

    def boolConstant(self, value):
        self._ops.append(lambda tree: self._alu.push(value))

    def _extractPath(self, path):
        result = []
        for elem in path.getMembers():
            if isinstance(elem, IdxAccess):
                result.append(elem.getIndex())
            elif isinstance(elem, AttributeAccess):
                result.append(elem.getAttributeName())
            else:
                raise InconsistentPredicateException()
        return result
