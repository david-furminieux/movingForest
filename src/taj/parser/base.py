class SyntaxError(Exception):
    '''
    an exception that can be thrown by the parser, and by the semantical
    analyzer to tell that something is not OK.
    '''
    def __init__(self, msg=''):
        super(Exception, self).__init__(msg)

class ASTNode(object):
    '''
    abstract base class for all AST nodes.
    '''

    def __init__(self):
        super(ASTNode, self).__init__()

    def walk(self, visitor):
        '''
        all nodes may be traversed by a visitor.
        @param visitor: the visitor which wants to traverse the tree.
        @type visitor: QueryVisitor, LogicVisitor, ExpressionVisitor
        @see QueryVisitor
        @see LogicVisitor
        @see ExpressionVisitor
        '''
        raise NotImplementedError(type(self))
