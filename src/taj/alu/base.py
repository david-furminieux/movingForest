class ALU(object):
    '''
    the interface a that arithmetic logic unit have to implement.
    '''
    
    def __init__(self):
        super(ALU, self).__init__()
    
    def setValueToExpr(self, tree, variable, expr):
        raise NotImplementedError()
    
    def deleteKey(self, tree, variable):
        raise NotImplementedError()


    