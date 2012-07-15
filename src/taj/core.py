from taj.exception import IllegalCondition

class RelationListener(object):
    '''
    an instance of this can be used to listen to a Relation
    '''
    
    ADDITION   = 1
    REMOVAL    = 2
    HEART_BEAT = 3
    
    def __init__(self):
        super(RelationListener, self).__init__()

    def notifyTree(self, tree, op, time):
        '''
        notify an addition or a removal of a tree to a relation,
        or a heart beat.
        @param tree: the  tree to be removed or added. this is None if heart
                     beat notification.
        @type tree: any
        @param op: one of ADDITION, REMOVAL or HEART_BEAT.
        @param time: the time at which the event occured.
        '''
        raise NotImplementedError(type(self))

class StreamListener(object):
    '''
    an instance of this can be used to listen to a Stream
    '''
    
    EVENT      = 4
    HEART_BEAT = 5
    
    def __init__(self):
        super(StreamListener, self).__init__()
    
    def notifyTree(self, tree, op, time):
        '''
        notify an event arrival, or a heart beat.
        @param tree: the  tree that arrived . this is None if heart
                     beat notification.
        @type tree: any
        @param op: one of EVENT or HEART_BEAT.
        @param time: the time at which the event occured.
        '''
        raise NotImplementedError()

class LifeCycle(object):
    '''
    an instance of this can be managed with following lifecycle.
    INIT (START STOP)* SHUTDOWN
    '''
    
    def __init__(self):
        super(LifeCycle, self).__init__()
    
    def init(self, props={}):
        '''
        initialize this instance using the properties
        @param props: the propserties used to initialize this instance.
        @type props: dict<str, any>
        '''
        
    def start(self):
        '''
        tell this instance that the system has been started.
        '''

    def stop(self):
        '''
        tell this instance that the system has been stopped.
        '''
    
    def shutdown(self):
        '''
        tell this instance that the system is going down.
        '''

class Forest(LifeCycle):
    '''
    base class for TreeStream and TreeRelation
    '''
    
    def __init__(self):
        super(Forest, self).__init__()

    def isStream(self):
        '''
        tell if this is an instance of TreeStream
        @return: True if self is an instance of TreeStream, False else.
        @rtype: boolean
        '''
        raise NotImplementedError(type(self))
    
class TreeStream(Forest):
    '''
    a stream of trees.
    this as the standard lifecycle
      INIT ( START STOP )* SHUTDOWN
    '''
    
    def __init__(self):
        super(TreeStream, self).__init__()
        self._listeners = []
        self._alu = None
    
    def addListener(self, listener):
        if not isinstance(listener, StreamListener):
            raise IllegalCondition("%s not a stream listener" % type(listener))
        self._listeners.append(listener)

    def _notifyListener(self, tree, op, time):
        for listener in self._listeners:
            listener.notifyTree(tree, op, time)

    def isStream(self):
        return True

class TreeRelation(Forest):
    '''
    an instantaneous relation of trees.
    '''
    
    def __init__(self):
        super(TreeRelation, self).__init__()
        self._listeners = list()
        
    def addListener(self, listener):
        if not isinstance(listener, RelationListener):
            raise IllegalCondition('not a relation listener')
        self._listeners.append(listener)
    
    def _notifyListener(self, tree, op, time):
        for listener in self._listeners:
            listener.notifyTree(tree, op, time)

    def isStream(self):
        return False

    def addIndex(self, pathLst):
        '''
        adds an index to this relation
        @param pathLst: a list of pathes to be considered for each tree.
        @type pathLst: list<Path> 
        '''
        raise NotImplementedError()
    
    def findTrees(self, pathValueLst):
        '''
        find all trees in this relation having 
        @para
        '''
        raise NotImplementedError()

class StreamAdapter(TreeStream, StreamListener):
    '''
    a stream of trees coming from or going outside.
    '''
    
    def __init__(self):
        super(StreamAdapter, self).__init__()
        self._stream       = None
        self._type         = None
        
        # are the event in sync (time ordered) 
        self._synchron     = None
        # should time of event occurence be generated or extracted.
        self._externalSync = False
        # should external heart beat be used.
        self._externalHeartBeat = False
        
    def init(self, definition):
        '''
        @see TreeStream#init
        '''
        self._def = definition
    
    def setExternalSync(self, external):
        '''
        tell the adapter if external synchronization should be done externaly
        @param external: is the synchronization external.
        @type external: bool
        '''
        self._externalSync = external
    
    def setExternalHeartBeat(self, external):
        '''
        tell the adapter if heart beat should be read and or written from/to
        external streams.
        @param external: externalize heart beats.
        @type external: bool
        '''
        self._externalHeartBeat = external
    
    def setStream(self, stream):
        '''
        set the stream this adapter should read/write from/to.
        @param stream: the stream to operate on.
        @type stream: io 
        '''
        self._stream = stream
    
    def fileno(self):
        '''
        behave like a file object.
        '''
        return self._stream.fileno()

    def setType(self, type):
        '''
        tell this adapter if he is an input or an output stream adapter.
        @param type: the type of this adapter.
        @type type: int.
        '''
        self._type = type
        
    def shutdown(self):
        '''
        shutdown this adapter
        @see TreeStream#shutdown
        '''
        if self._stream is not None:
            self._stream.close()

    def notifyTree(self, tree, op, time):
        if op==StreamListener.HEART_BEAT:
            if self._externalHeartBeat:
                tree = self.generateHeartBeat(time)
            else:
                return 
        self.write(tree)

    def read(self):
        raise NotImplementedError()
    
    def write(self, tree):
        raise NotImplementedError()
    
    def generateHeartBeat(self, time):
        raise NotImplementedError()
    
class Runner(object):
    '''
    an interface for all objects capable of running a query plan.
    it also must respect the standard lifecycle
      INIT (START STOP)* SHUTDOWN
    '''
    def __init__(self):
        '''
        standard constructor
        '''
        super(Runner, self).__init__()

    def init(self, queryPlan, props):
        '''
        initialization phase
        @param queryPlan: the queryPlan to be executed.
        @type queryPlan: list<Statement>
        @param props: the properties that have been configured.
        @type props: dict<string, any> 
        '''
        raise NotImplementedError()

    def start(self):
        '''
        start the system.
        '''
        raise NotImplementedError()
    
    def stop(self):
        '''
        stop the system
        '''
        raise NotImplementedError()

    def shutdown(self):
        '''
        shutdown procedure before the system goes down.
        '''
        raise NotImplementedError()
