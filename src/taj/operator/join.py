from taj.core import RelationListener, TreeRelation
from taj.exception import InternalError
import logging

class NamedRelationListener(RelationListener):
    
    def __init__(self, name, join):
        super(NamedRelationListener, self).__init__()
        self._name = name
        self._join = join
    
    def init(self, props):
        pass
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def shutdown(self):
        pass
    
    def notifyTree(self, tree, op, time):
        self._join.notifyTree(self._name, tree, op, time)

class BinaryJoin(TreeRelation):
    '''
    '''
    
    def __init__(self):
        super(BinaryJoin, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self._sources = list()
        self._props = {}
        self._elems = []
    
    def init(self, props):
        self._props = props
        
    def start(self):
        self._log.info('start')

        print "INITIALIZING JOIN"

        for source in self._sources:
            name = source.getName()
            listener = NamedRelationListener(name, self)
            listener.init(self._props)
            source.addListener(listener)
            self._elems.append((name, list()))
            source.start()

    def stop(self):
        for elem in self._elems:
            elem.stop()
    
    def shutdown(self):
        for elem in self._elems:
            elem.shutdown()
    
    def addEventSource(self, relation):
        self._log.debug('%s[%s] added to join' % (relation.getName(), type(relation)))
        
        name = relation.getName()
        if name is None:
            raise InternalError('no name found')
        self._sources.append(relation)
    
    def notifyTree(self, name, tree, op, time):
        if op == RelationListener.HEART_BEAT:
            raise NotImplementedError()
        evs = self.generateJoin(name, self._elems, tree)
        for (sName, lst) in self._elems:
            if sName==name:
                if op==RelationListener.ADDITION:
                    lst.append(tree)
                else:
                    lst.remove(tree)
        for ev in evs:
            self._notifyListener(ev, op, time)

    def generateJoin(self, name, lsts, tree):
        '''
        THIS IS AN ABSOLUTLY TRIVIAL IMPL.
        
        IT MUST BE OPTIMIZED
        '''
        print "GEN JOIN %s" % lsts
        
        
        (sName, lst) = lsts[0]

        if len(lsts) == 1:
            if sName == name:
                return [tree]
                result = list()
            else:
                for elem in lst:
                    ttt = dict()
                    ttt[sName] = elem
                    result.append(ttt)
                return result

        tmp = self.generateJoin(name, lsts[1:], tree)
        if sName==name:
            for elem in tmp:
                elem[name] = tree
            return tmp
        
        result = []
        for elem2 in lst:
            for elem1 in tmp:
                ttt = elem1
                ttt[sName] = elem2
                result.append(ttt)
        return result
