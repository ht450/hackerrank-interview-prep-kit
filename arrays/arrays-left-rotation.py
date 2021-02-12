#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    for rotation in range(1, d+1):
        number = a[0]
        a.append(number)
        a.remove(number)

    return a

if __name__ == '__main__':

    a_input = "33 47 70 37 8 53 13 93 71 72 51 100 60 87 97"
    n,d = 15,13
    expected_input = "87 97 33 47 70 37 8 53 13 93 71 72 51 100 60"
    a = list(map(int, a_input.rstrip().split()))
    expected = list(map(int, expected_input.rstrip().split()))
    result = rotLeft(a, d)
    print('expected:\t',expected)
    print('result:  \t', result)