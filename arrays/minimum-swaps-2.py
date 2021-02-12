#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    arr = [num-1 for num in arr]
    arr_sorted = sorted(arr)
    index_dict = {value: index for index,value in enumerate(arr)}

    for index,value in enumerate(arr):
        correct_value = arr_sorted[index]
        if value != correct_value:
            index_to_swap = index_dict[correct_value]
            # swap
            arr[index_to_swap],arr[index] = arr[index],arr[index_to_swap]
            index_dict[value] = index_to_swap
            index_dict[correct_value] = index
            swaps += 1

    return swaps


if __name__ == '__main__':

    test_data = [
        ["4 3 1 2","3"],
        ["2 3 4 1 5", "3"],
        ["1 3 5 2 4 6 7", "3"],
    ]

    for case in test_data:
        arr = list(map(int, case[0].rstrip().split()))
        print('ans = ',case[1])
        print('res = ',minimumSwaps(arr))
        print()
