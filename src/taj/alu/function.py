
import __builtin__
import datetime as dt
import types

def int(value):
    return __builtin__.int(value)

def str(value):
    return __builtin__.str(value)

def datetime(value):

    if isinstance(value, types.StringType) or isinstance(value, types.UnicodeType):
        return dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    else:
        raise TypeError()

def date(value):
    if isinstance(value, types.StringType) or isinstance(value, types.UnicodeType):
        tmp = dt.datetime.strptime(value, '%Y-%m-%d')
        return dt.date(tmp.year, tmp.month, tmp.day)
    else:
        raise TypeError()
