from cStringIO import StringIO
from io import BufferedIOBase
from logging import basicConfig, getLogger
from os import fork, pipe, close, write, read, _exit
from anyjson import deserialize
from taj.runner.singlethread import SingleThreadedRunner
import logging
import logging.config as logConf
import unittest

class Test(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

        try:
            basicConfig(level=logging.NOTSET)
            confFile = open('etc/log.conf')
            logConf.fileConfig(confFile)
            confFile.close()
        except IOError:
            pass
        
        self._log = getLogger(__name__)

    def setUp(self):
        self._runner = SingleThreadedRunner()
        self._log.info('system starting')

    def tearDown(self):
        self._runner.stop()
        self._runner.shutdown()

    def _createReader(self, string):
        inputStr = StringIO(string)
        (reader, writer) = pipe()
        if fork()==0:
            # we are the child
            close(reader)
            for line in inputStr:
                write(writer, line)
            close(writer)
            _exit(0)
        else:
            close(writer)
            return FdIO(reader)
    
    def extractResult(self, strBuffer):
        result = []
        idx = strBuffer.find('\n')
        last = 0
        while idx != -1:
            result.append(deserialize(strBuffer[last:idx]))
            last = idx+1
            idx = strBuffer.find('\n', last)
        return result

    def testPassThrough(self):
        inputStr = '''
          {"a":1, "b":2}
        '''
        self._runner.addInputStream('stream1', self._createReader(inputStr))
        output = StringIO()
        self._runner.addOutputStream('out', output)
        
        self._runner.init('''
          INSERT INTO out SELECT * from stream1; 
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        self.assertTrue(len(result)==1)
        self.assertTrue(result[0]=={ 'a':1, 'b':2})
    
    def testCreateTable(self):
        inputStr = '''
          {"a":1, "b":2}
        '''
        self._runner.addInputStream('stream1', self._createReader(inputStr))
        output = StringIO()
        self._runner.addOutputStream('out', output)
        
        self._runner.init('''
          CREATE TABLE buffer AS SELECT * FROM stream1;
          INSERT INTO out SELECT * from buffer; 
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        self.assertTrue(len(result)==1)
        self.assertTrue(result[0] == {'a':1, 'b':2})

    def testSimpleScenario(self):
        inputStr = '''
          {"a":1, "b":2}
          {"a":3, "b":2}
          {"a":3, "b":4}
        '''
        self._runner.addInputStream('stdin', self._createReader(inputStr))
        output = StringIO()
        self._runner.addOutputStream('stdout', output)
        
        self._runner.init('''
          CREATE TABLE buffer AS SELECT * FROM stdin WHERE a = 3;
          UPDATE buffer SET c = a + b DROP b WHERE b = 4;
          DELETE FROM buffer WHERE c=7;
          INSERT INTO stdout SELECT a AS b, c*a AS a.e, c AS f FROM buffer;
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        self.assertTrue(len(result)==1)
        self.assertTrue(result[0]=={'a': {'e': None}, 'b': 3, 'f': None})

    def testDoubleInsert(self):
        inputStr = '''
          {"a":1, "b":2}
        '''
        self._runner.addInputStream('stdin', self._createReader(inputStr))
        output = StringIO()
        self._runner.addOutputStream('stdout', output)
        
        self._runner.init('''
          CREATE TABLE buffer AS SELECT * FROM stdin;
          INSERT INTO stdout SELECT * FROM buffer;
          INSERT INTO stdout SELECT * FROM buffer;
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        self.assertTrue(len(result)==2)
        self.assertTrue(result[0]=={'a': 1, 'b': 2})
        self.assertTrue(result[1]=={'a': 1, 'b': 2})

#    def testBasicGroupBy(self):
#        inputStr = '''
#          {"a":1, "b":2}
#          {"a":2, "b":2}
#        '''
#        self._runner.addInputStream('stdin', self._createReader(inputStr))
#        output = StringIO()
#        self._runner.addOutputStream('stdout', output)
#        
#        self._runner.init('''
#          CREATE TABLE buffer AS SELECT * FROM stdin;
#          INSERT INTO stdout SELECT SUM(b) FROM buffer GROUP BY a;
#        ''', {})
#        self._runner.start()
#        self._runner.run()
#
#        result = self.extractResult(output.getvalue())
#        print "RESULT %s" % result
#        self.assertTrue(len(result)==2)
    
    def testBasicJoin(self):
        input1 = '{"a":1, "b":2}'
        self._runner.addInputStream('input1', self._createReader(input1))
        input2 = '{"a":1, "c":"hello"}'
        self._runner.addInputStream('input2', self._createReader(input2))
        output = StringIO()
        self._runner.addOutputStream('stdout', output)
        
        self._runner.init('''
          CREATE TABLE buffer AS SELECT * FROM input1, input2 WHERE input1.a=input2.a;
          INSERT INTO stdout SELECT * FROM buffer;
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        #print "RESULT %s" % result
        self.assertTrue(len(result)==1)
        self.assertTrue(result[0] == {'input1': {'a': 1, 'b': 2},
                                      'input2': {'a': 1, 'c': 'hello'}})
    
    def testJoin2(self):
        input1 = '''
          {"a":1, "b":2}
          {"a":1, "b":17}
        '''
        self._runner.addInputStream('input1', self._createReader(input1))
        input2 = '''
          {"a":1, "c":"hello"}
          {"a":2, "c":"bla"}
        '''
        self._runner.addInputStream('input2', self._createReader(input2))
        output = StringIO()
        self._runner.addOutputStream('stdout', output)
        
        self._runner.init('''
          CREATE TABLE buffer AS
          SELECT
            *
          FROM
            input1 AS .,
            input2 AS .c;
          #WHERE input1.a=input2.a;
          INSERT INTO stdout SELECT * FROM buffer;
        ''', {})
        self._runner.start()
        self._runner.run()

        result = self.extractResult(output.getvalue())
        print "RESULT %s" % result
        #self.assertTrue(len(result)==1)
        #self.assertTrue(result[0] == {'input1': {'a': 1, 'b': 2},
        #                              'input2': {'a': 1, 'c': 'hello'}})
        


class FdIO(BufferedIOBase):
    
    def __init__(self, fd):
        super(FdIO, self).__init__()
        self._fd = fd
    
    def fileno(self):
        return self._fd
    
    def read(self, amount=-1):
        if amount==-1:
            return read(self._fd)
        else:
            return read(self._fd, amount)


if __name__ == "__main__":
    unittest.main()