from taj.adapter.csv_ad import CSVAdapter
from taj.adapter.json_ad import JSONAdapter
from taj.alu.any import StackALU
from taj.core import Runner, StreamListener
from taj.exception import IllegalCondition, InternalError
from taj.operator.stream import IStream
from taj.operator.visit import JoinBuilder
from taj.operator.window import UnboundWindow
from taj.parser.MFQLLexer import MFQLLexer
from taj.parser.MFQLParser import MFQLParser
from taj.parser.stmt import StreamCreationStatement
from taj.parser.visitor import TracingVisitor, CompositeVisitor, QueryVisitor, \
    IsKeyValidator
from taj.runner.visit import StreamVisitor, RelationVisitor, FilterVisitor
import antlr3
import logging
import select

KNOWN_ADAPTERS = {
  'JSON': JSONAdapter,
  'CSV':  CSVAdapter
}

class StreamReader(object):
    '''
    an object capable of reading from more than one input stream.
    '''
    
    def __init__(self):
        super(StreamReader, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self._streams = dict()
        self._fds = list()
    
    def addStream(self, name, stream):
        self._streams[stream] = name
        self._fds.append(stream)
    
    def clear(self):
        '''
        remove all streams from the reader.
        '''
        self._streams = dict()
        self._fds = list()
    
    def run(self):
        '''
        @todo: check that an stream that is EOF but waiting is not interpreted
        as EOF
        '''
        while len(self._fds)>0:
            try:
                (rs, _, es) = select.select(self._fds, [], self._fds, 0.1)
            except Exception, (err, msg):
                if err==4:
                    return False
                else:
                    raise (err, msg)
            for stream in rs:
                try:
                    msg = stream.read()
                    #self._log.debug('received message: '+str(msg))
                except StopIteration:
                    self._fds.remove(stream)
            
            if len(rs)==0 and len(es)==0:
                # interruption detected so return control
                return True
        return False
                
class SingleThreadedRunner(Runner, QueryVisitor):
    '''
    this class instaciate a running MFQL interpreter.
    This is the single threaded version of the interpreter.
    
    the runner itself is a query visitor so that global variable setting can be
    interpreted.
    '''

    def __init__(self):
        '''
        standard ctor.
        '''
        super(SingleThreadedRunner, self).__init__()
        self._log.info('runner created')

        self._alu = StackALU()   # the ALU to be used by the system
        self._inputReader = None # where to read events from
        self._istreams  = dict() # all known input streams
        self._ostreams  = dict() # all known output stream
        self._relations = dict() # all known relations.
        
        self._interupted = False # has the system been interupted.
        self._inserts    = None  # what inserts should the system realtize
        
        # operators the should be noticated about START/STOP/SHUTDOWN
        self._extraOps = []
        
    def init(self, script, props={}):
        '''
        initialize the interpreter.
        @see Runner#init
        '''
        self._log.info('init')
        
        queryPlan = self.parseMFQL(script)
        
        self._firstPassVisit(queryPlan, props)
        self._bindRelations(props)
        self._bindOutputs(props)
        self._log.info('--------- AST VISIT TERMINATED ---------')
        self._secondPassVisit(queryPlan, props)

    def parseMFQL(self, input):
        '''
        parse a MFQL source file an return a list of Statements.
        @param input: the name of the file to be parsed or directly an file
                      object.
        @type input: string || file.
        @return: the list of statements.
        @rtype: list<Statement>
        '''
        
        if isinstance(input, str) or isinstance(input, unicode):
            stream = antlr3.ANTLRStringStream(input)
        else:
            stream = antlr3.ANTLRInputStream(input)

        lexer = MFQLLexer(stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = MFQLParser(tokens)
        
        result = parser.stmts()
        parser.eof()
        
        validator = CompositeVisitor()
        validator.addComponent(IsKeyValidator())

        if isinstance(result, list):
            for elem in result:
                elem.walk(validator)
        else:
            result.walk(validator)
        
        return result

    def _firstPassVisit(self, queryPlan, props):
        '''
        go through the complete AST and extract all definitions
        @param queryPlan: the list of all queries the have been found by the
                          parser.
        @type queryPlan: list<Statement>
        '''
        # debugging visitor
        tracer      = TracingVisitor()

        # visitor that will find all streams
        streams     = StreamVisitor(self)
        streams.init(props)
        
        # visitor that will find all relations
        joinBuilder = JoinBuilder()
        joinBuilder.init(props)
        relations   = RelationVisitor(joinBuilder, self._alu)
        relations.init(props)
        
        # compose a visitor a let's go
        firstPass = CompositeVisitor()
        firstPass.addComponent(tracer)
        firstPass.addComponent(self)
        firstPass.addComponent(streams)
        firstPass.addComponent(joinBuilder)
        firstPass.addComponent(relations)
        for elem in queryPlan:
            tracer.printSeparation()
            elem.walk(firstPass)
        
        if len(self._istreams) == 0:
            raise IllegalCondition('remember what this system is about?')

        # now store what we have found
        self._relations = relations.getRelations()
        self._inserts   = relations.getInserts()
        self._extraOps  = joinBuilder.getOperatorsToBeStarted()

    def _secondPassVisit(self, queryPlan, props):

        # debugging visitor
        #tracer      = TracingVisitor()

        filters     = FilterVisitor(self._relations, self._alu)
        filters.init(props)
        secondPass = CompositeVisitor()
        #secondPass.addComponent(tracer)
        secondPass.addComponent(filters)
        for elem in queryPlan:
            #tracer.printSeparation()
            elem.walk(secondPass)
            
    def _bindRelations(self, props):
        '''
        iterate through all relations and bind them together.
        '''
        
        unbound = self._relations
        self._relations = dict()
        for (name, str) in self._istreams.iteritems():
            self._relations[name] = str
        
        found = False
        while len(unbound)>0:
            found = False
            # search all relations through for one we can connect
            newBoundNames = list()
            for (name, relation) in unbound.iteritems():
                tmp = self._bindSingleRelarion(relation, props)
                if not tmp:
                    continue
                found = True
                self._relations[name] = relation
                newBoundNames.append(name)
            
            # remove the bounded elements from the unbound list
            for name in newBoundNames:
                del unbound[name]
            
            # we have considered all possibilities so if we didn't find one
            # something is wrong
            if not found:
                (name, _) = unbound.items()[0]
                msg = 'unable to bind to input element "%s"' % name
                raise IllegalCondition(msg)
        
    def _bindSingleRelarion(self, relation, props):
        '''
        bind a relation to its dependencies.
        '''
        boundable = True
        # check if all sources can be bound
        for (srcName, _) in relation.getSources():
            if not self._relations.has_key(srcName):
                boundable = False
        if not boundable:
            return False
        # all inputs are boundable so do it.
        for (srcName, srcRel) in relation.getSources():
            # use unbound window as default window
            if self._relations[srcName].isStream():
                self._log.warn("using default UNBOUND WINDOW on %s" % srcName)
                tmp = UnboundWindow()
                self._relations[srcName].init(props)
                self._relations[srcName].addListener(tmp)
            else:
                tmp = self._relations[srcName]
            tmp.addListener(srcRel)
            tmp.init(props)
        return True
    
    def _bindOutputs(self, props):
        
        for (name, relation) in self._inserts:
            if not self._ostreams.has_key(name):
                self._log.error('unable to find output stream "%s"' % name)
                continue
            outStr = self._ostreams[name]
            if isinstance(outStr, StreamListener):
                self._log.warn('using a default ISTREAM for "%s"' % name)
                tmp = IStream()
                tmp.addListener(outStr)
                outStr = tmp 
            relation.addListener(outStr)
            self._bindSingleRelarion(relation, props)
           
    def start(self):
        '''
        starts the interpreter
        @see Runner#start
        '''
        self._log.info('start')
        
        self._inputReader = StreamReader()
        for (name, stream) in self._istreams.iteritems():
            stream.start()
            self._inputReader.addStream(name, stream)
        for (name, stream) in self._ostreams.iteritems():
            stream.start()
        for rel in self._relations.itervalues():
            rel.start()
        for op in self._extraOps:
            op.start()
    
    def interupt(self):
        '''
        tell the interpreter that an interuption has been requested.
        this will stop the run method as soon as possible.
        @see: SingleThreadedRunner#run()
        '''
        self._interupted = True
        
    def run(self):
        '''
        bring the interpreter to run.
        '''
        tmp = True
        while not self._interupted and tmp:
            tmp = self._inputReader.run();

    def stop(self):
        self._log.info('stop')

        for stream in self._istreams.itervalues():
            stream.stop()
        for stream in self._ostreams.itervalues():
            stream.stop()
        for rel in self._relations.itervalues():
            rel.stop()
        for op in self._extraOps:
            op.stop()

        if self._inputReader is None:
            raise InternalError('invalid lifecycle')
        self._inputReader.clear()
    
    def shutdown(self):
        self._log.info('shutdown')
        
        for stream in self._istreams.itervalues():
            stream.shutdown()
        for stream in self._ostreams.itervalues():
            stream.shutdown()
        for rel in self._relations.itervalues():
            rel.shutdown()
        for op in self._extraOps:
            op.shutdown()

    def _assignGlobalValue(self, name, value):
        self._log.warn('global value %s will be ignored' % name)
    
    def assign(self, name, value):
        '''
        @see QueryVisitor
        '''
        self._assignGlobalValue(name, value.getValue())
    
    def addInputStream(self, name, stream, encoding='json', props={}):
        '''
        declare an input stream under a name which is then known by the system.
        @param name: the name of the input stream.
        @type name: str
        @param stream: an input stream
        @type stream: file object. 
        '''
        if self._istreams.has_key(name):
            raise IllegalCondition('duplicate input stream "%s"' % name)
        mode = StreamCreationStatement.INPUT
        stream = self._createAdaptedStream(name, mode, encoding, stream, props)
        self._istreams[name] = stream
    
    def addOutputStream(self, name, stream, encoding='json', props={}):
        '''
        declare an output stream under a name which is then known by the system.
        @param name: the name of the output stream.
        @type name: str
        @param stream: an input stream
        @type stream: file object. 
        '''
        if self._ostreams.has_key(name):
            raise IllegalCondition('duplicate output stream "%s"' % name)
        mode = StreamCreationStatement.OUTPUT
        stream = self._createAdaptedStream(name, mode, encoding, stream, props)
        self._ostreams[name] = stream

    def _createAdaptedStream(self, name, mode, encoding, stream, props):
        '''
        create an adapted event stream by decorating a file objected with an
        adapter.
        @param name: the name under which the stream is known.
        @type name: str
        @param mode: is it an input or an output stream.
        @type mode: int
        @param encoding: the type of adapter to be used.
        @type encoding: str
        @param stream: the actual file object to be decorated.
        @type stream: file.
        @param props: the properties for the adapter.
        @type props: dict<str, any>
        @return: the adapter if no issues occurs.
        @rtype: Adapter
        @raise IllegalCondition: if any issue occurs. 
        '''
        encoding = encoding.upper()
        if not KNOWN_ADAPTERS.has_key(encoding):
            msg = 'stream "%s" has a unrecognized adapter type. "%s"' % (name, encoding)
            raise IllegalCondition(msg)

        adapter = KNOWN_ADAPTERS[encoding]()
        adapter.setStream(stream)
        adapter.setType(mode)
        adapter.init(props)
        return adapter
