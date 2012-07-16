from taj.core import Transport
from taj.parser.stmt import StreamCreationStatement
import sys
from taj.exception import TransportException

SPECIAL_STREAMS = {
  '/dev/stdin':  sys.__stdin__,
  '/dev/stdout': sys.__stdout__,
  '/dev/stderr': sys.__stderr__
}

class FileTransport(Transport):

    _fileNames = set()

    def __init__(self, name, direction, options):
        super(FileTransport, self).__init__(name, direction, options)

        # what is the name of the file, and is it already open.
        fileName    = self.getOption(options, 'file')
        if fileName is None:
            self._log.error('stream "%s" has no "file" property. skipping'
                              % name)
            raise TransportException('file property not set')
        if fileName in FileTransport._fileNames:
            self._log.error(('stream "%s" uses a file which is already in'
                               +' use, skipping') % name)
            raise TransportException('double use of filename')
        FileTransport._fileNames.add(fileName)

        # determine in which writing mode this file should be opened
        if type == StreamCreationStatement.INPUT:
            mode = 'r'
        else:
            mode = 'a'
        
        origStream = None
        if SPECIAL_STREAMS.has_key(fileName):
            origStream = SPECIAL_STREAMS[fileName]
        else:
            try:
                origStream = open(fileName, mode)
            except IOError, (code,msg):
                self._log.error('stream "%s" with file "%s"' % (name, fileName))
                self._log.exception((code, msg))
                raise TransportException((code, msg))

        self._stream = origStream
