from taj.operator.common import RelationRelationOperator
import logging
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
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)    
        self._predicate = pred

    def start(self):
        self._log.debug('starting with %d listeners' % len(self._listeners))
        for l in self._listeners:
            self._log.debug('L %s' % type(l))
    
    def notifyTree(self, tree, op, time):
        
        if op == RelationListener.HEART_BEAT:
            self._notifyListener(tree, op, time)
            return
        
        self._log.debug('received %s' % tree)
        result = self._predicate(tree)
        self._log.debug('sel res %s' % result)
        if result:
            self._log.debug('decided to pass')
            self._notifyListener(tree, op, time)
        else:
            self._log.debug('decided to block')
        return result
