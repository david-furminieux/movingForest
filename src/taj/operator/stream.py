from taj.operator.common import RelationStreamOperator
from taj.core import RelationListener, StreamListener

class StreamWriter(RelationStreamOperator):
    '''
    USAGE UNCLEAR, CANDIDATE FOR DELETION
    '''
    def __init__(self):
        super(StreamWriter, self).__init__()
        self._target = None

    def init(self, targetStream):
        self._target = targetStream
        
    def notifyTree(self, tree, op, time):
        raise NotImplementedError()
        self._target.write(tree)

class IStream(RelationStreamOperator):
    
    def __init__(self):
        super(IStream, self).__init__()
    
    def notifyTree(self, tree, op, time):
        if op == RelationListener.HEART_BEAT:
            self._notifyListener(tree, StreamListener.HEART_BEAT, time)
        elif op == RelationListener.ADDITION:
            self._notifyListener(tree, StreamListener.EVENT, time)

class DStream(RelationStreamOperator):

    def __init__(self):
        super(DStream, self).__init__()
        self._target = None
    
    def notifyTree(self, tree, op, time):
        if op == RelationListener.HEART_BEAT:
            self._notifyListener(tree, StreamListener.HEART_BEAT, time)
        elif op == RelationListener.REMOVAL:
            self._notifyListener(tree, StreamListener.EVENT, time)
