#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    c = Counter()

    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k

    arrSum = 0
    maxSum = 0

    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)

    return maxSum



if __name__ == '__main__':
    n,m = 5,3
    queries = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100],
    ]
    exp = 200
    result = arrayManipulation(n, queries)
    print('ans = ', exp)
    print('res = ',result)

    print('----------------')

    n,m = 10,3
    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1],
    ]
    exp = 10
    result = arrayManipulation(n, queries)
    print('ans = ', exp)
    print('res = ',result)
