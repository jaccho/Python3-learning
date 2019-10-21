# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time, functools
def metric(textFunc):
    def wrapperSub(fn): 
        @functools.wraps(fn)
        def wrapper(*arg, **kw):
            print('%s %s at %s' % (fn.__name__, text, time.time()))
            r = fn(*arg, **kw)
            print('%s ended at %s' % (fn.__name__, time.time()))
            return r
        return wrapper

    if isinstance(textFunc,str):
        text = textFunc
        def decorator(fn):
           return wrapperSub(fn)
        return decorator
    else:
        text = 'excuted'
        fn = textFunc
        return wrapperSub(fn)
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric('called')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')