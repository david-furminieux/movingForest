from bsddb3.db import DB, DB_BTREE, DB_CREATE, DB_FIRST
from bsddb3 import db
from simplejson import dumps, loads
from struct import *

def start():
    
    print db.DB_VERSION_STRING
 
    base = DB()
    
    base.open('bla.db', dbtype=DB_BTREE, flags=DB_CREATE)
    
    cursor = base.cursor()
    
    print cursor.get("1", DB_FIRST)
    
    while True:
        print cursor.next()
    
#    for count in xrange(1, 100000000):
#        val = base.get(str(count))
#        if val is not None:
#            val = loads(val)
#        print "%d : %s" % (count, val)
#    for count in xrange(1, 100000000):
#        if (count % 1000) == 0: print count
#        base.put(str(count), dumps({'key': count}))
#    
    base.close()
if __name__ == '__main__':
    print pack('q', 1)
#    start()