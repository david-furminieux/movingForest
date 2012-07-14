from taj.operator.common import RelationRelationOperator
import logging
from taj.path import AttributeAccess, IdxAccess
from taj.exception import InternalError
from taj.core import RelationListener

log = logging.getLogger(__name__)

class ProjectionOperator(RelationRelationOperator):
    '''
    implements a projection in a stream
    '''

    def __init__(self, alu):
        super(ProjectionOperator, self).__init__()
        self._projs = list()
        self._alu = alu
        self._disctinct = False

    def addProjection(self, path, expr):
        self._projs.append((self._extractPathElems(path), expr))
    
    def setDistinct(self, isDistinct):
        self._disctinct = isDistinct
    
    def isFullProjection(self):
        # by definition an empty list of projections is SELECT *
        return len(self._projs)==0
    
    def notifyTree(self, tree, op, time):
        
        if op == RelationListener.HEART_BEAT:
            self.notifyTree(tree, op, time)
            return
        
        result = dict()
        
        for (path, expr) in self._projs:
            value = expr(tree)
            result = self._alu.modifyTree(result, path, value)
        
        self._notifyListener(result, op, time)

    def _extractPathElems(self, path):
        
        result = []
        for elem in path.getMembers():
            if isinstance(elem, AttributeAccess):
                result.append(elem.getAttributeName())
            elif isinstance(elem, IdxAccess):
                result.append(elem.getIndex())
            else:
                raise InternalError()
        return result
