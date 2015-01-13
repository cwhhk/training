__author__ = 'chenwei'
# -*- coding: utf-8 -*-
#请尝试用filter()删除1~100的素数。
import math
def isNotPrime(n):
    if n <= 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

print isNotPrime(2)
print filter(isNotPrime,range(1,101))
