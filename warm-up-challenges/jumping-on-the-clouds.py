#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps_min = 0
    n=0

    while n < len(c)-1:
        if n+2<len(c) and c[n+2] == 0:
            jumps_min += 1
            n += 2
        elif n+1<len(c) and c[n+1] == 0:
            jumps_min += 1
            n += 1
        else:
            print("unable to jump")
            break

    return jumps_min

if __name__ == '__main__':

    n = 6
    c = [0, 0, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print("1. expected = 3, jumps = ",result)

    n = 7
    c = [0, 0, 1, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print("2. expected = 4, jumps = ",result)
