# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:58:11 2019

@author: ASH
"""

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        value = 1
    elif n == 1:
        value = 1
    elif n == 2:
        value = n
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value
    
for i in range(10000):
    print(i + 1, ":", fibonacci(i))


# Second Method from lru_cache

from functools import lru_cache

@lru_cache(maxsize = 100)
def fibonacci2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 2:
        return fibonacci2(n-1) + fibonacci2(n-2)

for i in range(1, 10000):
    print(i + 1, ":", fibonacci2(i))