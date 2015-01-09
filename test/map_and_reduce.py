__author__ = 'chenwei'
# -*- coding: utf-8 -*-
# def f(n):
#     return n*n
# print map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))
#
# print str2int("13579")
#
# def char2num2(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# def str2int2(s):
#     return reduce(lambda x,y: x*10+y, map(char2num2, s))
#
# print str2int2("13579")

def first_upper(s):
    if len(s)>0 and isinstance(s,str):
        return s.capitalize()

print map(first_upper,['adam', 'LISA', 'barT'])

def prod(x,y):
    return x * y
print reduce(prod,[1,2,3,4,5,6])