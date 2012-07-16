from taj.adapter.csv_ad import CSVAdapter
from taj.adapter.json_ad import JSONAdapter
from taj.alu.any import StackALU
from taj.alu.visit import LogicBuilder, ExpressionEvalBuilder
from taj.core import Runner, StreamListener
from taj.exception import IllegalCondition, InternalError, TransportException
from taj.operator.manipulator import UpdateManipulator, DeleteManipulator
from taj.operator.projection import ProjectionOperator
from taj.operator.selection import SelectionOperator
from taj.operator.stream import IStream
from taj.operator.table import TableOperator
from taj.operator.visit import JoinBuilder
from taj.operator.window import UnboundWindow
from taj.parser.MFQLLexer import MFQLLexer
from taj.parser.MFQLParser import MFQLParser
from taj.parser.stmt import StreamCreationStatement
from taj.parser.visitor import TracingVisitor, CompositeVisitor, QueryVisitor, \
    IsKeyValidator
from taj.transport.file import FileTransport
from taj.transport.unix import UnixSocketTransport
import antlr3
import logging
import select
import sys
from taj.transport.process import SubProcessTransport


KNOWN_ADAPTERS = {
  'JSON': JSONAdapter,
  'CSV':  CSVAdapter
}

KNOWN_DRIVERS = {
  'file': FileTransport,
  'usocket': UnixSocketTransport,
  'subprocess': SubProcessTransport
}

class RelationVisitor(QueryVisitor):
    '''
    will record all relation definitions and create them
    '''
    
    def __init__(self, joinBuilder, alu):
        '''
        @param joinBuilder: a visitor that has to be also visiting the AST.
        @type joinBuilder: JoinBuilder
        @param alu: the ALU to be used to operate
        @type alu: ALU
        '''
        super(RelationVisitor, self).__init__()
        self._logic = LogicBuilder(alu)
        self._join  = joinBuilder
        self._expr  = ExpressionEvalBuilder(alu)
        self._alu   = alu
        
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        
        self._actualRelationName = None
        self._actualSelection    = None
        self._actualProjection   = None
        self._actualSource       = None
        self._actualInputs       = None
        self._active             = False
        self._exprStack          = None  # a stack on which projection are pushed.
        self._logicFound         = False # have we traversed any logic since last reset.
        
        self._relations = dict()
        self._inserts   = list()
        self._log.info('init')
        
    def getRelations(self):
        '''
        returns all relations that have been found while traversing
        '''
        return self._relations
    
    def getInserts(self):
        '''
        returns all inserts that have been seen while traversing.
        '''
        return self._inserts
    
    def enterTableCreation(self, name):
        self._active             = True
        self._actualRelationName = name
        self._actualSelection    = None
        self._actualProjection   = None
        self._actualSource       = None
    
    def leaveTableCreation(self):
        self._active             = False
        if self._actualRelationName is None:
            raise InternalError('rel name is None')
        if self._definedRelation is None:
            raise InternalError('select without a source')
        
        relation = TableOperator()
        self._definedRelation.addListener(relation)
        self._relations[self._actualRelationName] = relation
        for (name, rel) in self._actualInputs:
            relation.addSource(name, rel)
        self._actualRelationName = None
        self._actualInputs = list()

    def enterInsertStmt(self):
        self._active             = True
        self._actualRelationName = None
        
    def leaveInsertStmt(self):
        self._active             = False
        if self._actualRelationName is None:
            raise InternalError('rel name is None')
        if self._definedRelation is None:
            raise InternalError()
        
        relation = TableOperator()
        self._definedRelation.addListener(relation)
        self._inserts.append((self._actualRelationName,relation))
        for (name, rel) in self._actualInputs:
            relation.addSource(name, rel)
        self._actualRelationName = None
        self._actualInputs = list()

    def setTargetRelation(self, name):
        if not self._active: return
        self._actualRelationName = name
    
    def enterSelectStmt(self):
        if not self._active: return

        self._actualSelection    = None
        self._actualProjection   = None
        self._actualSource       = None
        self._definedRelation    = None
    
    def leaveSelectStmt(self):
        if not self._active: return

        relation = self._actualSource
        if self._actualSelection is not None:
            relation.addListener(self._actualSelection)
            relation = self._actualSelection
        if self._actualProjection is not None:
            relation.addListener(self._actualProjection)
            relation = self._actualProjection

        self._definedRelation = relation
        
        self._actualSelection    = None
        self._actualProjection   = None
        self._actualSource       = None
    
    def leaveSourceRelation(self):
        if not self._active: return
        self._actualSource = self._join.getResult()
        self._actualInputs = []
        for (name, rel) in self._join.getInputRelations():
            self._actualInputs.append((name, rel))

    def enterSelection(self):
        if not self._active: return
        self._actualSelection = None
        self._logicFound = False
    
    def leaveSelection(self):
        if not self._active: return
        if not self._logicFound: return
        tmp = SelectionOperator()
        tmp.init(self._logic.getResult())
        self._actualSelection = tmp
    
    def enterProjection(self, distinct):
        if self._actualProjection is None:
            self._actualProjection = ProjectionOperator(self._alu)
            self._actualProjection.setDistinct(distinct)
    
    def leaveProjection(self):
        if self._actualProjection is None:
            # no projections defined
            return
        if  self._actualProjection.isFullProjection():
            self._actualProjection = None

    def enterRename(self):
        pass
        
    def leaveRename(self):
        path = self._exprStack[0]
        expr = self._exprStack[1]
        self._exprStack = None
        self._actualProjection.addProjection(path, expr)

    def acceptLogic(self, logic):
        if not self._active: return
        self._logicFound = True
        logic.walk(self._logic)
    
    def acceptExpression(self, expr):
        if self._actualProjection is None: return
        if self._exprStack is None:
            self._exprStack = list()
            self._exprStack.append(expr)
        else:
            expr.walk(self._expr)
            self._exprStack.append(self._expr.getResult())

class StreamVisitor(QueryVisitor):
    '''
    will record all stream definitions and create them
    '''
    
    def __init__(self, streamRep):
        super(StreamVisitor, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self._repos = streamRep
        self._log.debug('stream visitor created')

    def getOption(self, options, key, default=None):
        try:
            tmp = options[key]
            if hasattr(tmp, 'getValue'):
                tmp = tmp.getValue()
            return tmp
        except KeyError:
            return default 
    
    def enterStreamCreation(self, name, type, options):
        self._log.debug('tring to create stream %s[%s]' % (name, type))

        for key, value in options.iteritems():
            self._log.debug(' OPTION %s => %s' % (key, value))

        driver = self.getOption(options, 'driver')
        driver = driver.lower()
        if driver is None:
            self._log.warning('stream "%s" has no driver property assuming file' % name)
            driver = 'file'

        if not KNOWN_DRIVERS.has_key(driver):
            self._log.error('stream "%s" has unrecognized driver "%s" skipping' % (name, driver))
            return

        try:
            driver = KNOWN_DRIVERS[driver](name, type, options)
        except TransportException, ex:
            self._log.error('while initializing "%s" %s' % (name, ex))
            return

        # determine and instantiate the adapter.
        adapterType = self.getOption(options, 'adapter', 'json').upper()      

        try:
            if type == StreamCreationStatement.INPUT:
                self._repos.addInputStream(name, driver, adapterType, options)
            else:
                self._repos.addOutputStream(name, driver, adapterType, options)
        except IllegalCondition, msg:
            driver.close()
            raise msg

class FilterVisitor(QueryVisitor):
    '''
    this will instantiate all filters on the streams
    meaning
    
      UPDATE DELETE
    '''
    def __init__(self, relations, alu):
        '''
        @param relations: a map of all known relations with name as key and the
                          relation itself as value.
        @type relations: map<str, RelationProxy>
        @param alu: the ALU to be used to operate.
        @type alu: ALU
        '''
        super(FilterVisitor, self).__init__()
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self.__expr  = ExpressionEvalBuilder(alu)
        self.__logic = LogicBuilder(alu)
        self.__rels = relations
        self.__alu  = alu

        self._actualFilter  = None # should the visit be considered.
        self._actualRelName = None
        self._actualSel     = None
        self._exprStack     = None

    def enterUpdateStmt(self):
        self._actualFilter = UpdateManipulator(self.__alu)

    def leaveUpdateStmt(self):

        name = self._actualRelName
        if not self.__rels.has_key(name):
            raise IllegalCondition('update on unknown relation "%s"' % name)
        self.__rels[name].addFilter(self._actualFilter)
        self._actualFilter  = None
        self._actualRelName = None
        self._actualSel     = None
        self._exprStack     = None

    def enterDeleteStmt(self):
        self._actualFilter = DeleteManipulator(self.__alu)

    def leaveDeleteStmt(self):
        name = self._actualRelName
        if not self.__rels.has_key(name):
            raise IllegalCondition('delete on unknown relation "%s"' % name)
        self.__rels[name].addFilter(self._actualFilter)
        self._actualFilter  = None
        self._actualRelName = None
        self._actualSel     = None
        self._exprStack     = None

    def setTargetRelation(self, name):
        if self._actualFilter is not None:
            self._actualRelName = name
        
    def enterSelection(self):
        if self._actualFilter is not None:
            pass

    def leaveSelection(self):
        if self._actualFilter is not None:
            self._actualFilter.setSelection(self.__logic.getResult())

    def enterAlteration(self):
        if self._actualFilter is not None:
            self._exprStack = list()
    
    def leaveAlteration(self):
        if self._exprStack is not None:
            path = self._exprStack[0]
            expr = self._exprStack[1]
            self._actualFilter.addAlteration(path, expr)
            self._exprStack = None
    
    def enterDrop(self):
        self._exprStack = list()

    def leaveDrop(self):
        self._actualFilter.addRemoval(self._exprStack[0])
        self._exprStack = None

    def acceptLogic(self, logic):
        if self._actualFilter is not None:
            logic.walk(self.__logic)

    def acceptExpression(self, expr):
        if self._actualFilter is None:
            return
        
        if self._exprStack is None:
            expr.walk(self.__expr)
        else:
            if len(self._exprStack)==0:
                self._exprStack.append(expr)
            else:
                expr.walk(self.__expr)
                self._exprStack.append(self.__expr.getResult())

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
        self._log = logging.getLogger(__name__+'.'+self.__class__.__name__)
        self._log.info('runner created')

        self._alu = StackALU()   # the ALU to be used by the system
        self._inputReader = None # where to read events from
        self._istreams  = dict() # all known input streams
        self._ostreams  = dict() # all known output stream
        self._relations = dict() # all known relations.
        
        self._interupted = False # has the system been interupted.
        self._inserts    = None  # what inserts should the system realtize
        
    def init(self, script, props):
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
        # for index extraction
        
        # visitor that will find all relations
        joinBuilder = JoinBuilder()
        relations   = RelationVisitor(joinBuilder, self._alu)
        
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

    def _secondPassVisit(self, queryPlan, props):

        # debugging visitor
        #tracer      = TracingVisitor()

        filters     = FilterVisitor(self._relations, self._alu)
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
