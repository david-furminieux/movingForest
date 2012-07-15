from inspect import getargspec
from taj.alu.base import ALU
from taj.exception import InternalError, UnknownFunction, InvalidFunctionArity
from taj.logic import Comparaison
from types import IntType, FloatType, NoneType
import logging
import taj.alu.function as function

log = logging.getLogger(__name__)

class Operator(object):
    
    def __init__(self):
        super(Operator, self).__init__()

    def nagateAtom(self, value):
        raise NotImplementedError()

    def addAtom(self, value1, value2):
        raise NotImplementedError()
    
    def subAtom(self, value1, value2):
        raise NotImplementedError()

    def invertAtom(self, value1):
        raise NotImplementedError()

    def multAtom(self, value1, value2):
        raise NotImplementedError()

    def divAtom(self, value1, value2):
        raise NotImplementedError()

    def modAtom(self, value1, value2):
        raise NotImplementedError()
    
    def compareAtom(self, value1, value2):
        if value1<value2:
            return -1
        elif value1==value2:
            return 0
        elif value1>value2:
            return 1
        else:
            raise ArithmeticError()

    def similarAtom(self, value1, value2):
        return str(value1) == str(value2)

class AnyOperator(Operator):

    def nagateAtom(self, value):
        return - value

    def addAtom(self, value1, value2):
        return value1 + value2
    
    def subAtom(self, value1, value2):
        return value1 - value2

    def invertAtom(self, value1):
        return 1/value1

    def multAtom(self, value1, value2):
        return value1 * value2

    def divAtom(self, value1, value2):
        return value1 / value2

    def modAtom(self, value1, value2):
        return value1 % value2

class NoneOperator(Operator):

    def nagateAtom(self, value):
        return None

    def addAtom(self, value1, value2):
        return None
    
    def subAtom(self, value1, value2):
        return None

    def invertAtom(self, value1):
        return None

    def multAtom(self, value1, value2):
        return None

    def divAtom(self, value1, value2):
        return None

    def modAtom(self, value1, value2):
        return None

    def compareAtom(self, value1, value2):
        return None

class NumberOperator(Operator):

    def nagateAtom(self, value):
        return -value

    def addAtom(self, value1, value2):
        if isinstance(value2, IntType) or isinstance(value2, FloatType):
            return value1 + value2
        return None
    
    def subAtom(self, value1, value2):
        if isinstance(value2, IntType) or isinstance(value2, FloatType):
            return value1 - value2
        return None

    def invertAtom(self, value1):
        return 1/value1

    def multAtom(self, value1, value2):
        if isinstance(value2, IntType) or isinstance(value2, FloatType):
            return value1 * value2
        return None

    def divAtom(self, value1, value2):
        if isinstance(value2, IntType) or isinstance(value2, FloatType):
            return value1 / value2
        return None

    def modAtom(self, value1, value2):
        if isinstance(value2, IntType) or isinstance(value2, FloatType):
            return value1 % value2
        return None

###############################################################################

class TooFewElementOnStack(InternalError):
    '''
    indicates that an operation has been atempted on the stack whci awaits a
    certain amount of elements of the stack but this amount is not available.
    '''

class VerboseAlu(object):
    
    def __init__(self, decorated):
        super(VerboseAlu, self).__init__()
        self._decorated = decorated
    
    def __getattr__(self, name):
        def distrib(name, *args):
            print "calling %s(%s)" % (name, args)
            meth = getattr(self._decorated, name)
            result = meth(*args)
            print "result %s[%s]" % (result, type(result)) 
            return result
        return lambda *args: distrib(name, *args)


class StackALU(ALU):
    '''
    this alu implements a stack machine in a FORTH style.
    
    this is only a prototype. thought are made in direction of a register
    machine and in direction of an ALU beeing only a function factory.
    '''
    
    operators = {
        NoneType: NoneOperator(),
        IntType: NumberOperator(),
        FloatType: NumberOperator()
    }
    defaultOperator = AnyOperator()

    def __init__(self):
        super(StackALU, self).__init__()
        self._stack = []
    
    def debugDump(self):
        count = 0
        for elem in self._stack:
            print "%d: %s%s" % (count, elem, type(elem))
            count += 1
    
    def _getOperator(self, value):
        '''
        returns the Operator which has been registred for the type of value.
        @param value: a value on which operation will be undertaken.
        @type value: any
        @return: an Operator suitable for operation on value
        @rtype: Operator
        '''
        try:
            return StackALU.operators[type(value)]
        except KeyError, msg:
            log.exception(msg)
            return StackALU.defaultOperator

    def checkTree(self, tree, path):
        '''
        check is a path is present in a tree.
        @param tree: the tree to be instpected.
        @type tree: any
        @param path: the path to followed.
        @type list<int|str>
        '''
        tmp = tree
        for elem in path:
            if tmp is None:
                return False
            if not tmp.has_key(elem):
                return False
            tmp = tmp[elem]
        return True

    def accessTree(self, tree, path):
        '''
        extract an element out of a tree following a path.
        @param tree: the tree to be inspected.
        @type tree: any
        @param path: a list of elements to be accessed.
        @type path: list<any>
        '''
        try:
            tmp = tree
            for elem in path:
                if tmp is None:
                    return None
                tmp = tmp[elem]
            return tmp
        except:
            return None
    
    def modifyTree(self, tree, path, value):
        '''
        set or overwrite a value in the tree under a certain name.
        @param tree: the tree to be modified.
        @type tree: any
        @param path: a path indicating the position to overwrite
        @type path: list<any>
        @return: the modified tree
        @rtype: any 
        '''
        
        # special case of an empty path meaning '.'
        if(len(path)==0):
            return value
        
        if tree is None:
            tree = dict()

        lastKey = path[-1]
        
        tmp = tree
        for elem in path[:-1]:
            if not tmp.has_key(elem):
                tmp[elem] = {}
            if not isinstance(tmp[elem], list) and not isinstance(tmp[elem], dict):
                tmp[elem] = {}
            tmp = tmp[elem]
        tmp[lastKey] = value
        
        return tree
    
    def deleteTree(self, tree, path):
        '''
        removes a path from a tree.
        @param tree: the tree to be modified.
        @type tree: any
        @param path: the path to be deleted.
        @type path: list<any>
        @return: the modified tree
        @rtype: any.
        '''
        if len(path) == 0:
            return None

        if tree is None:
            return None
        
        lastKey = path[-1]
        tmp = tree

        for elem in path[:-1]:
            if not tmp.has_key(elem):
                return tree
            if not isinstance(tmp[elem], list) and not isinstance(tmp[elem], dict):
                return tree
            tmp = tmp[elem]
        try:
            del tmp[lastKey]
        except:
            pass
        
        return tree
        
    def checkFunction(self, name, arity):
        '''
        tell if the kernel knows about a function with a certain arity
        @param name: the name of the function to be checked.
        @type name: string
        @return: the function that can be called
        @raise UnknownFunction: if the function is unknown
        @raise InvalidFunctionArity: if the function is known but was called
                                     with wrong amount of elements. 
        '''
        try:
            func = getattr(function, name)
            (args, _, _, defaults) = getargspec(func)
            
            max = len(args)
            if defaults is None:
                min = 0
            else:
                min = max - len(defaults)
            
            if arity>max or arity<min:
                msg = 'function %s must have between %d and %d params' % (name, min, max)
                raise InvalidFunctionArity(msg)
            return func
        except AttributeError:
            raise UnknownFunction(name)
    
    def callFunction(self, func, arity):
        '''
        calls a function using the top elements of the stack and pushing the
        result on the stack.
        @param func: a callable function.
        @type func: callable.
        @param arity: the amount of elements in the function.
        @type arity: int.
        '''
        
        args = []
        while arity > 0:
            args.append(self.pop())
            arity -= 1
        args.reverse()
        self._stack.append(func(*args))

    def clear(self):
        '''
        clears the stack.
        '''
        self._stack = []
    
    def drop(self):
        '''
        drops the top element of the stack.
        '''
        self.pop()
    
    def push(self, value):
        '''
        pushs a value on the stack.
        @param value: the value to be pushed.
        @type value: any
        '''
        self._stack.append(value)

    def pop(self):
        '''
        take the upper most element from the stack.
        '''
        try:
            return self._stack.pop()
        except IndexError:
            raise TooFewElementOnStack()
    
    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            raise TooFewElementOnStack()
    
    def add(self):
        '''
        operates an addition on the stack
        '''
        val2 = self.pop()
        val1 = self.pop()
        op = self._getOperator(val1)
        self._stack.append(op.addAtom(val1,val2))
    
    def sub(self):
        '''
        operates a substraction on the stack.
        '''
        val2 = self.pop()
        val1 = self.pop()
        op = self._getOperator(val1)
        self._stack.append(op.subAtom(val1,val2))

    def mult(self):
        '''
        operates a multiplication on the stack.
        '''
        val2 = self.pop()
        val1 = self.pop()
        op = self._getOperator(val1)
        self._stack.append(op.multAtom(val1,val2))
    
    def div(self):
        '''
        operates a division on the stack
        '''
        val2 = self.pop()
        val1 = self.pop()
        op = self._getOperator(val1)
        self._stack.append(op.divAtom(val1,val2))

    def mod(self):
        '''
        operates a division on the stack
        '''
        val2 = self.pop()
        val1 = self.pop()
        op = self._getOperator(val1)
        self._stack.append(op.modAtom(val1,val2))

    def lnot(self):
        '''
        operates a logical not on the top of the stack.
        '''
        self._stack[-1] = not self._stack[-1]
    
    def land(self):
        '''
        operates a logical and between to two top elems of the stack
        '''
        val1 = self.pop()
        val2 = self.pop()
        self._stack.append(val1 and val2)

    def lor(self):
        '''
        operates a logical and between to two top elems of the stack
        '''
        val1 = self.pop()
        val2 = self.pop()
        self._stack.append(val1 or val2)

    def compare(self, op):
        '''
        operate a comparison of the two top elements on the stack.
        @param op: one of Comparaison.LESS, Comparaison.LESS_EQUAL,
                   Comparaison.EQUAL, UNEQUAL, GREATER_EQUAL, GREATER, SIMILAR
        @type op: int.
        '''
        
        val2 = self.pop()
        val1 = self.pop()
        
        if val1 is None or val2 is None:
            self._stack.append(False)
        
        opr = self._getOperator(val1)
        
        if op == Comparaison.SIMILAR:
            self._stack.append(opr.similarAtom(val1, val2))
            return
        
        result = opr.compareAtom(val1, val2)
        if op == Comparaison.EQUAL:
            self._stack.append(result == 0)
        elif op == Comparaison.UNEQUAL:
            self._stack.append(result != 0)
        elif op == Comparaison.GREATER_EQUAL:
            self._stack.append(result != -1)
        elif op == Comparaison.GREATER:
            self._stack.append(result == 1)
        elif op == Comparaison.LESS:
            self._stack.append(result == -1)
        elif op == Comparaison.LESS_EQUAL:
            self._stack.append(result != 1)
        else:
            raise InternalError('unrecognized comprison operator')
