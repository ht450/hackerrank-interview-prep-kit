#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):

    # sort prices

    # print(prices)

    prices.sort()

    # print(prices)

    # buy toys
    toys_bought = 0
    for price in prices:
        if k - price > 0:
            k -= price
            toys_bought += 1
        else:
            break

    return toys_bought

if __name__ == '__main__':

    n,k = 7, 50
    prices_input = "1 12 5 111 200 1000 10"
    prices = list(map(int, prices_input.rstrip().split()))
    expected = 4
    result = maximumToys(prices, k)
    print('ans', expected)
    print('res',result)