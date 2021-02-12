#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps_tot = 0
    # print(a)

    def sort(a):
        swaps = 0
        for n in range(0,len(a)-1):
            if a[n] > a[n+1]:
                a[n],a[n+1] = a[n+1],a[n]
                swaps+=1
        return a, swaps

    def check_sort_asc():
        sorted = True
        for n in range(0,len(a)-1):
            if a[n] > a[n+1]:
                return False
        return sorted

    while not check_sort_asc():
        a, swaps = sort(a)
        swaps_tot += swaps

    # print(a)
    print('Array is sorted in',swaps_tot,'swaps.')
    print('First Element:',a[0])
    print('Last Element:',a[len(a)-1])

if __name__ == '__main__':

    a = [1, 2, 3]
    countSwaps(a)

    a = [3, 2, 1]
    countSwaps(a)
