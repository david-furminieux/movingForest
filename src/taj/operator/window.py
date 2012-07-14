from taj.core import RelationListener, StreamListener
from taj.operator.common import StreamRelationOperator
import logging

class UnboundWindow(StreamRelationOperator):
    '''
    this implements the unbound window [RANGE UNBOUND] and [ROWS UNBOUND]
    '''
    
    def __init__(self):
        super(UnboundWindow, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
    
    def notifyTree(self, tree, op, time):
        
        if op == StreamListener.HEART_BEAT:
            self._notifyListener(tree, RelationListener.HEART_BEAT, time)
            return
        
        self._log.debug('accepted tree %s', tree)
        self._notifyListener(tree, RelationListener.ADDITION, time)

class TimedWindowOperator(StreamRelationOperator):
    '''
    a instance of this will transform a stream to a relation over a
    Timed window.
    '''
    
    def __init__(self):
        super(TimedWindowOperator, self).__init__()
        raise NotImplementedError()

    def setTime(self, amount):
        self._amount = amount
        
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

class AmountWindowOperator(StreamRelationOperator):
    
    def __init__(self):
        super(AmountWindowOperator, self).__init__()
        raise NotImplementedError()

    def setAmount(self, amount):
        self._amount = amount
        
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name
