#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sum = 0
    if len(n) > 1:
        for digit in n:
            sum += int(digit)
        return superDigit(str(sum*k), 1)
    else:
        return n*k
    
if __name__ == '__main__':

    n = '148'
    k = 3
    expected = 3
    result = superDigit(n, k)
    print('exp', expected)
    print('res', result)
