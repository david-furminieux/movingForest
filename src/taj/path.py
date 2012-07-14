from taj.expr import Expression
from taj.exception import InconsistentExpression
from taj.logic import Disjunction, Predicate
from taj.parser.base import ASTNode

class Selector(Expression):
    '''
    HAS BEEN POSTPONED.
    '''
    
    def __init__(self):
        super(Selector, self).__init__()
        self._members = []
        self._relative = None

    def append(self, elem):
        self._members.append(elem)

    def getMembers(self):
        return self._members

    def setRelative(self, rel):
        self._relative = rel
        
    def getRelative(self):
        return self._relative
    
    def walk(self, visitor):
        visitor.enterSelector(self._relative)
        for part in self._members:
            part.walk(visitor)
        visitor.leaveSelector()
    
class Path(Selector):
    
    def __init__(self):
        super(Path, self).__init__()
    
    def append(self, elem):
        assert isinstance(elem, PathPart)
        Selector.append(self, elem)

    def setRelative(self, rel):
        raise InconsistentExpression('no relative path allowed')

    def walk(self, visitor):
        visitor.enterPath()
        for part in self._members:
            part.walk(visitor)
        visitor.leavePath()
    
class SelectorPart(ASTNode):

    def __init__(self):
        super(SelectorPart, self).__init__()
        
class PathPart(SelectorPart): pass

class AttributeAccess(PathPart):
    
    def __init__(self, attrName):
        super(AttributeAccess, self).__init__()
        self._attr = attrName
    
    def getAttributeName(self):
        return self._attr
    
    def walk(self, visitor):
        visitor.attributeAccess(self._attr)

class IdxAccess(PathPart):
    
    def __init__(self, idx):
        super(IdxAccess, self).__init__()
        self._idx = idx

    def getIndex(self):
        return self._idx

    def walk(self, visitor):
        visitor.idxAccess(self._idx)

class DeepAttributeAccess(SelectorPart):
    
    def __init__(self, attrName):
        super(DeepAttributeAccess, self).__init__()
        self._attr = attrName

    def getAttributeName(self):
        return self._attr

class WideAttributeAccess(SelectorPart):
    '''
    '''

class WideDeepAttributeAccess(SelectorPart):
    '''
    '''

class ConditionalAccess(SelectorPart):
    '''
    '''
    
    def __init__(self):
        super(ConditionalAccess, self).__init__()
        self._condition = Disjunction()
    
    def add(self, pred):
        if not isinstance(pred, Predicate):
            raise InconsistentExpression(type(pred))
        self._condition.add(pred)

class RangeAccess(SelectorPart):
    
    def __init__(self, start, stop=None, step=None):
        super(RangeAccess, self).__init__()
        self._start = start
        self._stop  = stop
        self._step  = step

class EnumAccess(SelectorPart):
    
    def __init__(self, elems):
        super(EnumAccess, self).__init__()
        self._elems = elems

class PathAccess(SelectorPart):
    
    def __init__(self, path):
        super(PathAccess, self).__init__()
        if not isinstance(path, Path):
            raise InconsistentExpression(type(path))
        self._path = path
        self._relative = False
    
    def getMembers(self):
        return self._path.getMembers()

    def setRelative(self, rel):
        self._relative = rel
        
    def getRelative(self):
        return self._relative
