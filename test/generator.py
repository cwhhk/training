__author__ = 'chenwei'
# -*- coding: utf-8 -*-
def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

def fab1(max):
    n,a,b=0,0,1
    for s in range(n,max):
        yield b
        a,b=b,a+b

for n in fab(32):
    print n
for n in fab1(32):
    print n