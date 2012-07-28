'''
interface definitions for AST visitors
@see QueryVisitor
@see ExpressionVisitor
@see LogicVisitor
'''

from taj.parser.base import SyntaxError
import logging

class ExpressionVisitor(object):
    '''
    an instance of this can visit a full MFQL Expression. 
    '''
    def __init__(self):
        super(ExpressionVisitor, self).__init__()

    def enterPath(self):
        '''
        enter a path definition. a path is a variable.
        '''
    
    def attributeAccess(self, name):
        '''
        an attribute is been accessed within path or a selector
        @param name: the name of the accessed attribute.
        @type name: string 
        '''

    def idxAccess(self, idx):
        '''
        an index is been accessed within  path or a selector
        @param idx: the index that is been accessed.
        @type name: int
        '''

    def leavePath(self):
        '''
        leave a path definition
        '''
        pass
    
    def enterSumm(self):
        '''
        enter a summ
        '''
        pass

    def leaveSumm(self):
        '''
        leave a summ
        '''
        pass
    
    def leaveAdd(self):
        pass
    
    def leaveSub(self):
        pass
    
    def enterProduct(self):
        '''
        enter a summ
        '''
        pass

    def leaveProduct(self):
        '''
        leave a summ
        '''
    
    def leaveMult(self):
        pass
    
    def leaveDiv(self):
        pass
    
    def enterMod(self):
        pass
    
    def leaveMod(self):
        pass
    
    def enterArray(self):
        '''
        enter an array definition (Constant or Pattern).
        '''
    
    def enterMap(self):
        '''
        enter a map definition (Constant or Pattern).
        '''
    
    def next(self, name=None):
        '''
        while traversing a structure (Map Or Array) tell that we will see the
        next one.
        @param name: if traversing a map the key name of the previous item.
        @type name: str | none
        '''

    def leaveArray(self):
        '''
        leave an array definition (Constant or Pattern).
        '''
    
    def leaveMap(self):
        '''
        leave a map definition (Constant or Pattern).
        '''
    
    def nullConstant(self):
        '''
        visit a NULL constant.
        '''

    def intConstant(self, value):
        '''
        visit an integer contant.
        @param value: the value of the constant.
        @type value: int
        '''
        
    def stringConstant(self, value):
        '''
        visit an string contant.
        @param value: the value of the constant.
        @type value: str
        '''

    def floatConstant(self, value):
        '''
        visit an float contant.
        @param value: the value of the constant.
        @type value: float
        '''

    def boolConstant(self, value):
        '''
        visit an boolean contant.
        @param value: the value of the constant.
        @type value: bool
        '''

    def enterFunction(self, name, arity):
        '''
        CONSIDER REMOVING THIS
        
        enter a function call.
        @param name: the name of the function.
        @type name: string
        @param arity: the amount of elements that have been passed to the
                      function.
        @type arity: int. 
        '''
    
    def leaveFunction(self, name, arity):
        '''
        enter a function call.
        @param name: the name of the function.
        @type name: string
        @param arity: the amount of elements that have been passed to the
                      function.
        @type arity: int. 
        '''
    
class LogicVisitor(object):
    '''
    an instance of this can visit any logical expression.
    '''

    def __init__(self):
        super(LogicVisitor, self).__init__()

    def enterComparaison(self, operator):
        '''
        enter a comparison construction where the operator is given.
        @param operator: which operator is used to compare.
        @type operator: int. 
        '''
    
    def rvalue(self):
        '''
        in a comparison, this is called to the visitor so that separation
        between lvalue and rvalue can be made without ambiguity.
        '''
        pass

    def leaveComparaison(self, operator):
        '''
        leaves a comparaison construction.
        '''

    def enterConjunction(self):
        '''
        enter terms which have to be anded together.
        '''
    
    def enterDisjunction(self):
        '''
        enter terms which have to be ored together.
        '''
    
    def leaveConjunction(self):
        '''
        leave a list of terms that should be anded.
        '''
    
    def leaveDisjunction(self):
        '''
        leave a list of terms to be ored. 
        '''
    
    def operate(self):
        '''
        depending on the logical structure we are in, AND or OR should be
        operated.
        '''
        
    def enterIsNull(self):
        '''
        check if the structure is NULL.
        '''
    
    def leaveIsNull(self):
        '''
        terminate a structure to be checked of being null.
        '''
    def enterIsKey(self):
        pass
    
    def leaveIsKey(self):
        pass
    
    def leaveNegation(self):
        pass

    def acceptExpression(self, expr):
        pass
    
class QueryVisitor(object):
    '''
    an instance of this will be notified of every structural a query has.
    '''
    
    def __init__(self):
        super(QueryVisitor, self).__init__()

    def assign(self, name, value):
        '''
        a global assignment
        @param name: the name of the variable.
        @param value: the value to be assigned.
        '''
    
    def enterTableCreation(self, name):
        '''
        enter a table creation declaration
        @param name: the name of the created relation.
        @type name: string
        '''

    def leaveTableCreation(self):
        '''
        leaves a table creation.
        '''

    def enterStreamCreation(self, name, strType, options):
        '''
        enter a stream creation declaration
        @param name: the name of the created stream.
        @strType name: string
        @param strType: is it an input or an output stream
        @strType: int
        @param options: the options for the stream
        @strType options: dict
        '''

    def leaveStreamCreation(self):
        pass

    def enterSelectStmt(self):
        '''enter a representation of a SELECT statement.'''

    def acceptStreamOp(self, op):
        '''
        tell if this relation has been transformed to a stream using one of
        ISTREAM, RSTREAM or DSTREAM.
        @param op: which of the stream operator has been used. one of
            Stream.DEFAULT, Stream.INSERT, Stream.DELETE, Stream.RELATION,
            Stream.NONE
        @type op: int.
        '''

    def leaveSelectStmt(self):
        pass

    def enterUpdateStmt(self):
        '''enter a representation of an UPDATE statement.'''

    def leaveUpdateStmt(self):
        pass

    def enterInsertStmt(self):
        '''enter a representation of an INSERT statement.'''
        
    def leaveInsertStmt(self):
        pass

    def enterDeleteStmt(self):
        pass

    def leaveDeleteStmt(self):
        pass
    
    def enterSourceRelation(self):
        '''
        enter a relation on which operation will be done.
        '''

    def leaveSourceRelation(self):
        '''
        leaves the relation on which operations should be done.
        '''

    def setTargetRelation(self, name):
        '''
        enter the target in which insertion should be done.
        @param name: the name of the relation in which insertion should be done.
        @type name: str.
        '''

    def enterSelection(self):
        '''
        eneter the definition of the part of the source relation what should be
        considered.
        '''
    
    def leaveSelection(self):
        pass
    
    def enterProjection(self, distinct):
        '''
        enter the projection part used by a statement.
        @param distinct: is the projection distinct?
        @type distinct: boolean
        '''
    
    def leaveProjection(self):
        '''
        leave the projection part of a statement
        '''
    
    def enterSimpleRelation(self, name):
        '''
        a simple/base relation named <name> is been visited
        @param name: the name of the base relation visited.
        @type name: string 
        '''
    
    def enterAlteration(self):
        pass

    def leaveAlteration(self):
        pass
    
    def enterRename(self):
        pass
    
    def leaveRename(self):
        pass
    
    def enterDrop(self):
        pass
    
    def leaveDrop(self):
        pass
    
    def enterWindowedStream(self):
        pass
    
    def leaveWindowedStream(self):
        pass
    
    def enterSimpleStream(self, name):
        pass

    def enterTimedWindow(self, time):
        pass
    
    def leaveTimedWindow(self):
        pass
    
    def AmountWindow(self, amount):
        pass
    
    def leaveAmountWindow(self):
        pass
    
    def enterRelationComposition(self):
        '''
        enter a section where multiple relation are joined
        '''
    
    def leaveRelationComposition(self):
        '''
        enter a section where multiple relation are joined
        '''
    
    def crossJoin(self):
        pass
    
    def leaveRealtionComposition(self):
        pass
    
    def enterRelationRename(self):
        pass
    
    def leaveRelationRename(self):
        pass
    
    def enterAmountWindow(self, amount):
        pass

    def acceptExpression(self, expr):
        pass
    
    def acceptLogic(self, logic):
        pass

class CompositeVisitor(object):
    '''
    a composition of visitor objects. it will delegate all call to it to all
    components that have been registered to him.  
    '''
    def __init__(self):
        super(CompositeVisitor, self).__init__()
        self._comoponents = []
    
    def addComponent(self, cmpnt):
        self._comoponents.append(cmpnt)
    
    def __getattr__(self, name):
        def distrib(name, elems, *args):
            for elem in elems:
                meth = getattr(elem, name)
                meth(*args)
        return lambda *args: distrib(name, self._comoponents, *args)

class TracingVisitor(object):
    '''
    a visitor which will trace all calls to a logger
    '''
    def __init__(self):
        super(TracingVisitor, self).__init__()
        self._logger = logging.getLogger(__name__+'.'+self.__class__.__name__)
    
    def printSeparation(self):
        self._logger.info('----------------------------------------------------')
    
    def __getattr__(self, name):
        return lambda *args: self._logger.info(name) 

    def acceptLogic(self, logic):
        self._logger.info('acceptLogic')
        logic.walk(self)

    def acceptExpression(self, expr):
        self._logger.info('acceptExpression')
        expr.walk(self)

class FullVisitor(QueryVisitor, LogicVisitor, ExpressionVisitor):
    '''
    an instance of this is capable of visiting a complete AST.
    '''
    def __init__(self):
        super(FullVisitor, self).__init__()

    def acceptExpression(self, expr):
        expr.walk(self)
    
    def acceptLogic(self, logic):
        logic.walk(self)

class IsKeyValidator(FullVisitor):
    '''
    checks that IS KEY is not predecesed with a full expression, which is
    allowed by grammar but an illegal construction.
    '''

    def __init__(self):
        super(IsKeyValidator, self).__init__()
        self._exprFound = False
    
    def enterIsKey(self):
        self._exprFound = False
    
    def leaveIsKey(self):
        if self._exprFound:
            raise SyntaxError("expr not allowed in IS KEY")
    
    def enterSumm(self):
        self._exprFound = True
    
    def enterProduct(self):
        self._exprFound = True
    
    def nullConstant(self):
        self._exprFound = True

    def intConstant(self, value):
        self._exprFound = True

    def stringConstant(self, value):
        self._exprFound = True

    def floatConstant(self, value):
        self._exprFound = True

    def boolConstant(self, value):
        self._exprFound = True
    
    def enterConjunction(self):
        self._exprFound = True
    
    def enterDisjunction(self):
        self._exprFound = True
    
    def enterFunction(self, name, arity):
        self._exprFound = True
    
    def enterNegation(self):
        self._exprFound = True
