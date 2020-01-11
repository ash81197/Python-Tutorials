# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:35:55 2019

@author: ASH
"""

import time
import threading

def calc_sq(numbers):
    print("Calculating the Square of numbers: ")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n)


def calc_cube(numbers):
    print("Calculating the Cube of numbers: ")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n*n*n)

arr = [2,3,4,5]

start = time.time()

t1 = threading.Thread(target = calc_sq, args = (arr,))
t2 = threading.Thread(target = calc_cube, args = (arr, ))

t1.start()
t2.start()

t1.join()
t2.join()


print("Done in: ", time.time() - start)