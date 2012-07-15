from taj.operator.common import RelationRelationOperator
from taj.core import RelationListener

class SelectionOperator(RelationRelationOperator):
    '''
    this is the implementation of a selection. it will filter out all elements
    that do not match the condition.
    '''

    def __init__(self):
        super(SelectionOperator, self).__init__()
        self._predicate = None

    def init(self, pred):
        self._predicate = pred

    def notifyTree(self, tree, op, time):
        
        if op == RelationListener.HEART_BEAT:
            self._notifyListener(tree, op, time)
            return
        
        result = self._predicate(tree)
        if result:
            self._notifyListener(tree, op, time)