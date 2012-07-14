#!/usr/bin/python
from datetime import datetime

class Test(object):
    
    def __init__(self):
        self._bla = 0

    def incr(self):
        self._bla += 1

def meth1():
    t = Test()
    for _ in xrange(1000000):
        t.incr()

def meth2():
    t = Test()
    incr = t.incr
    
    for _ in xrange(1000000):
        incr()

def start():
    a = datetime.now()
    meth2()
    b = datetime.now()
    print b - a
    a = datetime.now()
    meth1()
    b = datetime.now()
    print b - a
    pass

if __name__ == '__main__':
    start()