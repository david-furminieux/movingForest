from socket import error as SocketError, socket, AF_UNIX, SOCK_STREAM
from taj.core import Transport
from taj.exception import TransportException
from taj.parser.stmt import StreamCreationStatement
from time import sleep
import errno

class UnixSocketTransport(Transport):
    '''
    an implementation of transport over unix socket.
    reconnection logic is implemented.
    '''
    
    ACCEPTED_SOCKET_ERRORS = [
      errno.ECONNREFUSED,
      errno.EPIPE
    ]
    
    def __init__(self, name, direction, options):
        super(UnixSocketTransport, self).__init__(name, direction, options)

        if not direction == StreamCreationStatement.OUTPUT:
            raise NotImplementedError()

        path = self.getOption(options, 'socket')
        if path is None:
            self._log.error('stream "%s" has no socket property' % name)
            raise TransportException('socket config')
        self._path = path
        self._connected = False
        self._connect()

    def _connect(self):
        if self._connected: return
        while True:
            try:
                self._connectRaw()
                return
            except Exception, ex:
                self._handleException(ex)
                
    def _connectRaw(self):
        sock = socket(AF_UNIX, SOCK_STREAM)
        sock.connect(self._path)
        self._stream = sock
        self._connected = True

    def _handleException(self, ex):
        
        #print "%s[%s]" % (ex, type(ex))
        
        while True:
            if isinstance(ex, SocketError):
                try:
                    if self._stream is not None:
                        self._stream.close()
                        self._stream = None
                except IOError:
                    pass
                self._connected = False
                
                if ex.errno in UnixSocketTransport.ACCEPTED_SOCKET_ERRORS:
                    # ignore connection refused and wait a bit
                    sleep(0.1)
                    try:
                        self._connectRaw()
                        return
                    except Exception, ex2:
                        ex = ex2
                elif ex.errno == errno.ENOENT:
                    raise TransportException(ex)
                else:
                    raise ex
            else:
                raise ex

#    def fileno(self):
#        self._connect()
#        return self._stream.fileno()
#    
#    def readline(self, size=-1):
#        while True:
#            try:
#                return self._stream.readline(size)
#            except Exception, ex:
#                self._handleException(ex)
    
    def write(self, string):
        while True:
            try:
                return self._stream.send(string)
            except Exception, ex:
                self._handleException(ex)
    
    def close(self):
        self._stream.close()

