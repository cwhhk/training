__author__ = 'chenwei'
# -*- coding: utf-8 -*-
#这是一个阶乘的函数，主要用于演示递归调用
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

def power(number,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * number
    return s
for i in range(1,33):
    print i,fact(i)
    print i,power(i)