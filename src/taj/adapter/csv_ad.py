from taj.core import StreamAdapter
from taj.exception import AdapterInitializationException
import csv
import logging

log = logging.getLogger(__name__)

class CSVAdapter(StreamAdapter):


    def setDefinition(self, definition):

        schema = definition.getOption('schema')
        if schema is None:
            raise AdapterInitializationException('schema property not set')

        fieldNames = schema.keys()

        self.reader = csv.DictReader(self._stream, fieldNames)
        self.writer = csv.DictWriter(self._stream, fieldNames)
    
    def start(self):
        log.debug('starting with %d listeners' % len(self._listeners))

    def read(self):
        msg = self.reader.next()
        log.debug('recieved %s' % msg)
        self.notifyListener(msg)
        return msg
    
    def write(self, msg):
        self.writer.writerow(msg)
