from Queue import Queue, Empty
from os import unlink
from select import select
from socket import socket, AF_UNIX, SOCK_STREAM
from taj.exception import TransportException
from taj.parser.stmt import StreamCreationStatement
from taj.transport.unix import UnixSocketTransport
from threading import Thread
from time import sleep
import unittest

class Server(Thread):
    
    def __init__(self, queue):
        super(Server, self).__init__()
        self.init()
        self.queue = queue
        self.reconnect = False
    
    def init(self):
        try:
            unlink('socket')
        except:
            pass
        self.socket = socket(AF_UNIX, SOCK_STREAM)
        self.socket.bind('socket')
        self.socket.listen(32)
    
    def run(self):
        
        while True:
            (rds, _, ers) = select([self.socket], [], [self.socket], 0.05)
            if len(ers) != 0:
                raise Exception('error')
            
            if self.reconnect:
                self.doReconnect()
                continue
            
            if len(rds)==0:
                continue
            sock, _ = rds[0].accept()
            msg = sock.recv(1024)
            sock.close()
            self.queue.put(msg)
    
    def doReconnect(self):
        self.reconnect = False
        self.socket.close()
        sleep(5)
        try:
            unlink('socket')
        except:
            pass
        self.socket = socket(AF_UNIX, SOCK_STREAM)
        self.socket.bind('socket')
        self.socket.listen(32)
    
    def setReconnect(self):
        self.reconnect = True

class Test(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.server = Server(self.queue)
        self.server.daemon = True
        self.server.start()

    def tearDown(self):
        pass

    def testUSocketConfig(self):
        
        exp = False
        try:
            UnixSocketTransport()
        except TypeError:
            exp = True
        self.assertTrue(exp, "empty construtor not allowed")
        
        exp = None
        try:
            config = {'socket': 'bla'}
            UnixSocketTransport('test', StreamCreationStatement.OUTPUT, config)
        except TransportException, ex:
            exp = ex
        self.assertTrue(isinstance(exp, TransportException), "invalid config %s" % exp)
        
        exp = None
        try:
            config = {'socket': 'socket'}
            UnixSocketTransport('test', StreamCreationStatement.OUTPUT, config)
        except TransportException, ex:
            exp = ex
        self.assertTrue(exp is None, "invalid config %s" % exp)

    def testReconnect(self):
        
        msg = 'hello\n'
        exp = None
        
        try:
            config = {'socket': 'socket'}
            sock = UnixSocketTransport('test', StreamCreationStatement.OUTPUT, config)
            sock.write(msg)
            
            try:
                msg2 = self.queue.get(True, 0.5)
            except Empty:
                msg2 = None
        except Exception, ex:
            exp = ex
        self.assertTrue(exp is None, 'exception while operating %s' % exp)
        self.assertTrue(msg2==msg, 'invalid info "%s" "%s"' % (msg, msg2))
        
        self.server.setReconnect()
        sleep(1)

        sock.write(msg)
        try:
            msg2 = self.queue.get(True, 5)
        except Empty:
            msg2 = None
        self.assertTrue(msg2==msg, 'invalid info')
        
#        self.socket.close()
#        sock.write(msg)
#
#        conn, _ = self.socket.accept()
#        tmp = conn.recv(1024);
#        conn.close()
#        self.assertTrue(tmp==msg)
        
        
#        except Exception, ex:
#            exp = ex
#        finally:
#            raise
#            self.assertTrue(exp is None, 'error while operating %s' % exp)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()