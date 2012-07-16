from subprocess import Popen, PIPE
from taj.core import Transport
from taj.exception import TransportException
from taj.parser.stmt import StreamCreationStatement

class SubProcessTransport(Transport):
    '''
    a transport that enable a process as input or output
    '''

    def __init__(self, name, direction, options):
        super(SubProcessTransport, self).__init__(name, direction, options)

        func = self.getOption(options, 'process')
        if func is None:
            self._log.error('stream "%s" has no process property' % name)
            raise TransportException('subprocess config')

        try:
            if direction == StreamCreationStatement.INPUT:
                pipes = Popen(func, stdin=None, stdout=PIPE)
                self._stream = pipes.stdout
            else:
                pipes = Popen(func, stdin=PIPE, stdout=None)
                self._stream = pipes.stdin
        except OSError, ex:
            raise
            raise TransportException(ex)
