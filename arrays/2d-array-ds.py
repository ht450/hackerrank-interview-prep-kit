#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    hourglassSumsList = []
    
    row = 0
    col = 0
    while row < len(arr)-2:
        col = 0
        while col < len(arr[0])-2:
            print('[',row,']','[',col,']', end=' ')
            
            a = arr[row][col]
            b = arr[row][col+1]
            c = arr[row][col+2]
            d = arr[row+1][col+1]
            e = arr[row+2][col]
            f = arr[row+2][col+1]
            g = arr[row+2][col+2]
            
            hourglassTotal = a+b+c+d+e+f+g
            hourglassSumsList.append(hourglassTotal)
            print('total ',hourglassTotal)
            col += 1
        row += 1
    
    print('max ',max(hourglassSumsList))
    
    return max(hourglassSumsList)

if __name__ == '__main__':

    arr = [
    [-1 ,-1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5],
    ]
    result = hourglassSum(arr)
    print('expected = -6, result = ', result)