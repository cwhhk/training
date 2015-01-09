__author__ = 'chenwei'
# -*- coding: utf-8 -*-
def calc(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number*number
    return sum

a=[1,2,3,4]
print calc(1,2,3,4)
print calc(a[0],a[1],a[2],a[3])
print calc(*a)