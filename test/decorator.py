__author__ = 'chenwei'
# -*- coding: utf-8 -*-

import functools,math

def log(text='null'):
    def decorator(func):
        print 'begin call %s():' %func.__name__
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            # return func(*args, **kw)
            result = func(*args, **kw)
            print 'end call %s():' %func.__name__
            return result
        return wrapper
    return decorator

@log("execute:")
def isNotPrime(n):
    if n <= 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

print filter(isNotPrime,range(1,101))

# @log("")
# def isNotPrime(n):
#     if n <= 1:
#         return True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return True
#     return False
#
# print filter(isNotPrime,range(1,101))