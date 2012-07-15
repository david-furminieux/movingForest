from taj.core import StreamAdapter, RelationListener
from taj.exception import InternalError
from taj.operator.common import RelationRelationOperator, Filter
from taj.operator.stream import StreamWriter
import logging

class RelationProxy(RelationRelationOperator):
    '''
    This could possibly be eliminated, since it does nothing and a join
    operator is available
    '''
    def __init__(self):
        super(RelationProxy, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self._name = None
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def notifyTree(self, tree, op, time):
        self._notifyListener(tree, op, time)

class TableOperator(RelationRelationOperator):

    def __init__(self):
        super(TableOperator, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self.filters = list()
        self.__sources = list() 

    def start(self):
        self._log.debug('starting with %d listeners' % len(self._listeners))
        for l in self._listeners:
            self._log.debug('L %s' % type(l))

    def addFilter(self, filter):
        self._log.debug('adding filter %s' % filter)
        if not isinstance(filter, Filter):
            raise InternalError('not a filter')
        self.filters.append(filter)
    
    def addListener(self, listener):
        self._log.debug('adding listener %s' % listener)
        if isinstance(listener, StreamAdapter):
            tmp = StreamWriter()
            tmp.init(listener)
            listener = tmp
        super(TableOperator, self).addListener(listener)

    def notifyTree(self, tree, op, time):
        if op==RelationListener.HEART_BEAT:
            self._notifyListener(tree, op, time)
            return
        
        flag = True
        for filter in self.filters:
            (flag, tree) = flag and filter.apply(tree)
            if not flag:
                break
        if flag:
            self._notifyListener(tree, op, time)

    def addSource(self, name, rel):
        self._log.info('source "%s" added to relation' % name)
        self.__sources.append((name, rel))
        
    def getSources(self):
        if len(self.__sources)==0:
            raise InternalError('empty sources')
        return self.__sources
