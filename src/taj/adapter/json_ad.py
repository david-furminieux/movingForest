from taj.core import StreamAdapter, StreamListener
import logging

from anyjson import deserialize, serialize
from datetime import datetime

log = logging.getLogger(__name__)

class JSONAdapter(StreamAdapter):

    def setDefinition(self, definition):
        pass

    def read(self):
        txt = self._stream.readline()
        if txt == '':
            raise StopIteration()
        try:
            msg = deserialize(txt)
            log.debug('======================================================')
            log.debug('received %s' % msg)
            self._notifyListener(msg, StreamListener.EVENT, datetime.now())
            return msg
        except ValueError, msg:
            if str(msg) != 'empty JSON description':
                log.error('while decoding "%s"' % txt)
                print 'while decoding "%s"' % txt
                log.exception(msg)
            else:
                log.warning('while decoding "%s"' % txt)
    
    def write(self, msg):
        txt = serialize(msg)+'\n'
        self._stream.write(txt)
