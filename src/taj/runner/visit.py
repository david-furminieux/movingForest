from taj.alu.visit import LogicBuilder, ExpressionEvalBuilder
from taj.exception import InternalError, IllegalCondition
from taj.operator.manipulator import UpdateManipulator, DeleteManipulator
from taj.operator.projection import ProjectionOperator
from taj.operator.selection import SelectionOperator
from taj.operator.table import TableOperator
from taj.parser.stmt import StreamCreationStatement
from taj.parser.visitor import QueryVisitor
import sys

SPECIAL_STREAMS = {
  '/dev/stdin':  sys.__stdin__,
  '/dev/stdout': sys.__stdout__,
  '/dev/stderr': sys.__stderr__
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
        self._props = {}
    
    def init(self, props):
        self._props = props

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
        self._repos = streamRep
        self._fileNames = set()
        self._props = {}
        self._log.debug('stream visitor created')
    
    def init(self, props):
        self._props = props

    def getOption(self, options, key, default=None):
        try:
            tmp = options[key]
            if hasattr(tmp, 'getValue'):
                tmp = tmp.getValue()
            return tmp
        except KeyError:
            return default 
    
    def enterStreamCreation(self, name, type, options):
        self._log.debug('tring to create stream %s' % name)

        # determine in which writing mode this file should be opened
        if type == StreamCreationStatement.INPUT:
            mode = 'r'
        else:
            mode = 'a'
        
        # what is the name of the file, and is it already open.
        fileName    = self.getOption(options, 'file')
        if fileName is None:
            self._log.warning('stream "%s" has no "file" property. skipping'
                              % name)
            return
        if fileName in self._fileNames:
            self._log.warning(('stream "%s" uses a file which is already in'
                               +' use, skipping') % name)
            return
        self._fileNames.add(fileName)

        origStream = None
        if SPECIAL_STREAMS.has_key(fileName):
            origStream = SPECIAL_STREAMS[fileName] 
        else:
            try:
                origStream = open(fileName, mode)
            except IOError, (code,msg):
                self._log.error('stream "%s" with file "%s"' % (name, fileName))
                self._log.exception((code, msg))
                return

        # determine and instantiate the adapter.
        adapterType = self.getOption(options, 'adapter', 'json').upper()      

        try:
            if type == StreamCreationStatement.INPUT:
                self._repos.addInputStream(name, origStream, adapterType, options)
            else:
                self._repos.addOutputStream(name, origStream, adapterType, options)
        except IllegalCondition, msg:
            origStream.close()
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
        self.__expr  = ExpressionEvalBuilder(alu)
        self.__logic = LogicBuilder(alu)
        self.__rels = relations
        self.__alu  = alu

        self._actualFilter  = None # should the visit be considered.
        self._actualRelName = None
        self._actualSel     = None
        self._exprStack     = None
        self._props         = {}

    def init(self, props):
        self._props = props 

    def enterUpdateStmt(self):
        self._actualFilter = UpdateManipulator(self.__alu)
        self._actualFilter.init(self._props)

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
        self._actualFilter.init(self._props)

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
