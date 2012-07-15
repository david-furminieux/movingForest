from taj.exception import InternalError
from taj.operator.common import Filter
from taj.path import AttributeAccess, IdxAccess

class DeleteManipulator(Filter):
    '''
    implementation of a DELETE statement.
    '''
    
    def __init__(self, alu):
        super(DeleteManipulator, self).__init__()
        self._cond = None
        self._alu  = alu

    def init(self):
        '''
        @param condition: the condition used to delete
        @type condition: lambda<tree>
        '''
        
    def setSelection(self, cond):
        self._cond = cond

    def apply(self, tree):
        '''
        apply filter of this tree
        @param tree: the tree to be checked for deletion.
        @type tree: jsonobject.
        @param op: one of RelationListener.ADDITION or RelationListener.REMOVAL
        @type op: int.
        '''
        
        cond = True
        if self._cond:
            cond = self._cond(tree)
        return (not cond, tree)

class UpdateManipulator(Filter):
    
    def __init__(self, alu):
        super(UpdateManipulator, self).__init__()
        
        self._alu          = alu
        self._cond         = None
        self._modificators = list()
        
    def setSelection(self, cond):
        self._cond = cond
    
    def addAlteration(self, path, expr):
        path = self._extractMembers(path)
        def makeAlteration(alu, path, expr, tree):
            value = expr(tree)
            return alu.modifyTree(tree, path, value)
        fun = lambda tree: makeAlteration(self._alu, path, expr, tree)
        self._modificators.append(fun)
    
    def addRemoval(self, path):
        path = self._extractMembers(path)
        def makeRemoval(alu, path, tree):
            return alu.deleteTree(tree, path)
        fun = lambda tree: makeRemoval(self._alu, path, tree)
        self._modificators.append(fun)

    def apply(self, tree):
        
        cond = True
        if self._cond:
            cond = self._cond(tree)
        if cond:
            for modif in self._modificators:
                tree = modif(tree)
        return (True, tree)
    
    def _extractMembers(self, path):
        
        result = []
        for elem in path.getMembers():
            if isinstance(elem, AttributeAccess):
                result.append(elem.getAttributeName())
            elif isinstance(elem, IdxAccess):
                result.append(elem.getIndex())
            else:
                raise InternalError()
        return result
