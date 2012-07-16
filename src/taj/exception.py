
class TAJException(Exception):
    '''
    common abstract exception for all MovingForest exceptions.
    '''
    
    def __init__(self, msg=''):
        super(TAJException, self).__init__(msg)

class IllegalCondition(TAJException):
    '''
    some conditions occurred which are not allowed by the system.
    '''

class InternalError(TAJException):
    '''
    is raised when some conditions occurs that are actually impossible.
    '''

class InconsistentPredicateException(TAJException):
    '''
    some inconsistencies occurred while building a logical construction.
    '''

class InconsistentExpression(TAJException):
    '''
    some inconsistencies occurred while building an arithmetic construction.
    '''

class UnknownFunction(InconsistentExpression):
    '''
    a function has been used which is not knwon.
    '''

class InvalidFunctionArity(InconsistentExpression):
    '''
    a function has been called with an invalid amount of elems.
    '''

class InconsistentStatement(TAJException):
    '''
    some inconsistencies occurred while building query statement.
    '''

class AdapterInitializationException(TAJException):
    '''
    some problems occurred while initializing a stream adapter.
    '''

class ArithmeticException(TAJException):
    '''
    some issues occurred while computing an arithmetic expression.
    '''

class LogicException(TAJException):
    '''
    some issues occurred while computing a logical expression.
    '''

class TransportException(TAJException):
    '''
    some issues have occured while initializing or using a transport
    '''

class DeprecatedUsageException(DeprecationWarning, TAJException):
    '''
    some elements a used which may not be used anymore.
    '''
    def __init__(self, msg=''):
        super(DeprecatedUsageException, self).__init__(msg)


