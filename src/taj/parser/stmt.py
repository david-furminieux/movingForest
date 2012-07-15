from taj.exception import InconsistentStatement
from taj.expr import Expression
from taj.parser.base import ASTNode

class Statement(ASTNode):
    '''
    generic class representing all statements known by MFQL
    '''
    def __init__(self):
        super(Statement, self).__init__()

class ManipulatingStatement(Statement):
    '''
    a super class for all statement which transform a stream or a relation
    '''

class AssignmentStatement(Statement):
    '''
    representation of a statement which assign some global values
    
      SET bla= {"hello": true}
    '''
    
    def __init__(self):
        super(AssignmentStatement, self).__init__()
        self._name = None
        self._value = None
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def setValue(self, value):
        self._value = value
        
    def getValue(self):
        return self._value
    
    def walk(self, visitor):
        visitor.assign(self._name, self._value)

class Relation(ASTNode):
    '''
    a super class for all realtions
    '''

class ComposedRelation(Relation):
    '''
    an abject representing a join between some realtions.
    '''
    CROSS = 1
    
    def __init__(self):
        super(ComposedRelation, self).__init__()
        self._joined = []
        
    def cross(self, relation):
        '''
        cross join another relation
        @param relation: the relation to be cross joined.
        @type relation: Relation
        '''
        if not isinstance(relation, Relation):
            raise InconsistentStatement(type(relation))
        self._joined.append((ComposedRelation.CROSS, relation))
    
    def walk(self, visitor):
        visitor.enterRelationComposition()
        for (type, rel) in self._joined:
            rel.walk(visitor)
            if type==ComposedRelation.CROSS:
                visitor.crossJoin()
            else:
                raise InconsistentStatement('unrecognized join type')
        visitor.leaveRelationComposition()
            
class WindowedStream(Relation):
    
    def __init__(self, stream):
        super(WindowedStream, self).__init__()
        self._stream = stream
        self._window = None
        
    def setWindow(self, win):
        if not isinstance(win, Window):
            raise InconsistentStatement(type(win))
        self._window = win
        
    def walk(self, visitor):
        visitor.enterWindowedStream()
        self._stream.walk(visitor)
        self._window.walk(visitor)
        visitor.leaveWindowedStream()

class SimpleRelation(Relation):
    '''
    a relation that can be joined with other simple relations.
    '''
    
    def __init__(self, name):
        super(SimpleRelation, self).__init__()
        self._name = name
        self._renamed = None
    
    def setRenamedAs(self, path):
        self._renamed = path
    
    def getName(self):
        return self._name

    def walk(self, visitor):
        visitor.enterSimpleRelOrStrRef(self._name)

class Window(ASTNode):
    '''
    an abstract representation of a window that can be put over a stream.
    since all windows can be partitioned, the abstraction can.
    '''
    
    def __init__(self):
        super(Window, self).__init__()
        self._partition = None
    
    def setPartition(self, part):
        '''
        set the partitions for this window.
        @param part: a list of paths with wich partition should be done.
        @type param: list<Path>
        '''
        self._partition = part
    
    def getPartition(self):
        return self._partition

class TimeWindow(Window):
    '''
    a window which is defined over time
    '''
    
    def __init__(self, seconds):
        super(TimeWindow, self).__init__()
        self._time = seconds
        
    def walk(self, visitor):
        visitor.enterTimedWindow(self._time)
        visitor.leaveTimedWindow()
        
class AmountWindow(Window):
    '''
    a window which is defined by an amount of events
    '''
    def __init__(self, amount):
        super(AmountWindow, self).__init__()
        self._amount = amount

    def walk(self, visitor):
        visitor.enterAmountWindow(self._amount)
        visitor.leaveAmountWindow()

class Stream(ASTNode):
    '''
    a super class for all streams.
    '''
    
    DEFAULT  = 1 
    INSERT   = 1
    DELETE   = 2
    RELATION = 3
    NONE     = 4
    
    def __init__(self):
        super(Stream, self).__init__()

class SimpleStream(Stream):

    def __init__(self, name):
        super(SimpleStream, self).__init__()
        self._name     = name    

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def walk(self, visitor):
        visitor.enterSimpleRelOrStrRef(self._name)
    
class SelectStatement(Statement, Relation):
    '''
    represention of a selection
    
      SELECT DISTINCT a,b FROM bla WHERE a=1
      
    the single parts are
      SELECT projection FROM source WHERE selection 
    '''
    
    def __init__(self):
        super(SelectStatement, self).__init__()
        self._src      = None
        self._proj     = list()
        self._sel      = None
        self._distinct = False
        self._streamOp = None

    def setSource(self, src):
        '''
        set the source from which this selection should take his events from
        @param src: a list of relations where events comes from.
        @type src: Relation
        '''
        if not isinstance(src, Relation):
            raise InconsistentStatement(type(src))
        self._src = src
    
    def getSource(self):
        return self._src
    
    def setProjections(self, proj):
        self._proj = proj
        
    def getProjections(self):
        return self._proj
    
    def setSelection(self, sel):
        self._sel = sel
        
    def getSelection(self):
        return self._sel
    
    def setDistinct(self, value):
        self._distinct = value
    
    def getDistinct(self):
        return self._distinct

    def setStreamingOp(self, op):
        self._streamOp = op

    def walk(self,visitor):
        visitor.enterSelectStmt()
        visitor.enterSourceRelation()
        self._src.walk(visitor)
        visitor.leaveSourceRelation()
        visitor.enterSelection()
        if self._sel is not None:
            visitor.acceptLogic(self._sel)
        visitor.leaveSelection()
        visitor.enterProjection(self._distinct)
        for elem in self._proj:
            elem.walk(visitor)
        visitor.leaveProjection()
        visitor.acceptStreamOp(self._streamOp)
        visitor.leaveSelectStmt()

class CreationStatement(Statement):
    
    def __init__(self, name):
        super(CreationStatement, self).__init__()
        self._options = dict()
        self._name = name
    
    def getName(self):
        return self._name

    def setOptions(self, opts):
        self._options = opts
    
    def getOptions(self):
        return self._options
    
class StreamCreationStatement(CreationStatement):
    '''
    the representation of a statement like
    CREATE INPUT STREAM stdin (file = '/dev/stdin')
    '''
    
    INPUT  = 1
    OUTPUT = 2
    
    def __init__(self, name, defin, type):
        super(StreamCreationStatement, self).__init__(name)
        if type not in [self.INPUT, self.OUTPUT]:
            raise InconsistentStatement('invalid stream type')
        self._type = type
        
        self._checkDef(defin)
        self.setOptions(defin)
    
    def setType(self, type):
        self._type = type;
    
    def getType(self):
        return self._type

    def _checkDef(self, defin):
        if defin is None:
            raise InconsistentStatement()
    
    def walk(self, visitor):
        visitor.enterStreamCreation(self._name, self._type, self.getOptions())
        visitor.leaveStreamCreation()

class TableCreationStatement(CreationStatement):
    
    def __init__(self, name, definition):
        super(TableCreationStatement, self).__init__(name)
        self._verifyDef(definition)
        self._definition = definition
    
    def getDefinition(self):
        return self._definition
    
    def _verifyDef(self, defin):
        if defin is None:
            raise InconsistentStatement()
    
    def walk(self, visitor):
        visitor.enterTableCreation(self._name)
        self._definition.walk(visitor)
        visitor.leaveTableCreation()

class InsertStatement(ManipulatingStatement):
    
    def __init__(self):
        super(InsertStatement, self).__init__()
        self._target = None
        self._src    = None

    def setTarget(self, target):
        if not isinstance(target, SimpleRelation):
            raise InconsistentStatement(type(target))
        self._target = target
    
    def getTarget(self):
        return self._target

    def setSource(self, src):
        if not isinstance(src, Relation):
            raise InconsistentStatement(type(src))
        self._src = src
    
    def getSource(self):
        return self._src
    
    def walk(self, visitor):
        visitor.enterInsertStmt()
        self._src.walk(visitor)
        visitor.setTargetRelation(self._target.getName())
        visitor.leaveInsertStmt()

class UpdateStatement(ManipulatingStatement):
    '''
    this a representation of an UPDATE statement.
    '''
    
    def __init__(self):
        super(UpdateStatement, self).__init__()
        self._target = None
        self._sel    = None
        self._alters = None
    
    def setTarget(self, relation):
        if not isinstance(relation, SimpleRelation):
            raise InconsistentStatement(type(relation))
        self._target = relation
    
    def getTarget(self):
        return self._target
    
    def setAlterations(self, alters):
        if not isinstance(alters, list):
            raise InconsistentStatement(type(alters))
        self._alters = alters
    
    def getAlterations(self):
        return self._alters
    
    def setSelection(self, sel):
        self._sel = sel
        
    def getSelection(self):
        return self._sel
    
    def walk(self, visitor):
        visitor.enterUpdateStmt()
        visitor.setTargetRelation(self._target.getName())
        visitor.enterSelection()
        visitor.acceptLogic(self._sel)
        visitor.leaveSelection()
        for alter in self._alters:
            alter.walk(visitor)
        visitor.leaveUpdateStmt()

class DeleteStatement(ManipulatingStatement):
    '''
    representation of a DELETE statement
    '''
    
    def __init__(self):
        super(DeleteStatement, self).__init__()
        self._target = None
        self._sel    = None
    
    def setTarget(self, target):
        self._target = target
    
    def getTarget(self):
        return self._target
    
    def setSelection(self, sel):
        self._sel = sel
    
    def getSelection(self):
        return self._sel
    
    def walk(self, visitor):
        visitor.enterDeleteStmt()
        visitor.setTargetRelation(self._target.getName())
        visitor.enterSelection()
        if self._sel is not None:
            visitor.acceptLogic(self._sel)
        visitor.leaveSelection()
        visitor.leaveDeleteStmt()

class ModifRequest(ASTNode):
    
    def __init__(self, path):
        super(ModifRequest, self).__init__()
        self._modified = path
        
    def getModified(self):
        return self._modified

class DropRequest(ModifRequest):
    
    def walk(self, visitor):
        visitor.enterDrop()
        visitor.acceptExpression(self.getModified())
        visitor.leaveDrop()

class AlterRequest(ModifRequest):
    
    def __init__(self, path, expr):
        super(AlterRequest, self).__init__(path)
        if not isinstance(expr, Expression):
            raise InconsistentStatement(type(expr))
        self._rvalue = expr
    
    def getExpression(self):
        return self._rvalue

    def walk(self, visitor):
        visitor.enterAlteration()
        visitor.acceptExpression(self.getModified())
        visitor.acceptExpression(self._rvalue)
        visitor.leaveAlteration()

class Rename(ASTNode):
    
    def __init__(self, expr, newName):
        super(Rename, self).__init__()
        self._expr = expr
        self._name = newName
    
    def getExpression(self):
        return self._expr
    
    def getNewName(self):
        return self._name

    def walk(self, visitor):
        visitor.enterRename()
        visitor.acceptExpression(self._name)
        visitor.acceptExpression(self._expr)
        visitor.leaveRename()

class RenameRelation(Relation):
    
    def __init__(self, rel, newName):
        super(RenameRelation, self).__init__()
        if not isinstance(rel, Relation):
            raise InconsistentStatement(type(rel))
        self._rel = rel
        self._newName = newName
    
    def walk(self, visitor):
        visitor.enterRelationRename()
        visitor.acceptExpression(self._newName)
        self._rel.walk(visitor)
        visitor.leaveRelationRename()
