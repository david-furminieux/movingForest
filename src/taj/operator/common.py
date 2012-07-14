from taj.core import StreamListener, TreeStream, TreeRelation, RelationListener

class StreamRelationOperator(TreeRelation, StreamListener):
    '''
    a base class for all stream-relation operations.
    '''
    
    def __init__(self):
        super(StreamRelationOperator, self).__init__()

class RelationRelationOperator(TreeRelation, RelationListener):
    '''
    a base class for all relation-relation operations. 
    '''
    
    def __init__(self):
        super(RelationRelationOperator, self).__init__()

class RelationStreamOperator(TreeStream, RelationListener):
    '''
    a base class for all relation-stream operations.
    '''
    
    def __init__(self):
        super(RelationStreamOperator, self).__init__()

class Filter(object):
    '''
    a common interface for all erlement that together builds UPDATE/DELETE.
    '''
    
    def __init__(self):
        super(Filter, self).__init__()
    
    def init(self, props):
        raise NotImplementedError(type(self))
    
    def start(self):
        pass

    def apply(self, tree, op):
        '''
        apply this filter to a tree possibly modifiing it and telling if it
        should be kept.
        @param tree: the tree to be inspected.
        @type tree: any.
        @param op: standard op
        @return: True if the filter decided to keep the tree, False else.
        @return: the new Tree
        @rtype: (bool, any)
        '''
        raise NotImplementedError(type(self))

    def stop(self):
        pass
    
    def shutdown(self):
        pass
