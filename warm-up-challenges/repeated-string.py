#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """
    return the number of 'a's when the substring s is repeated for n characters.
    """

    a_in_substring = s.count('a')
    length_of_substring = len(s)

    whole_repitions = n // length_of_substring
    remainder_chars = n - (length_of_substring * whole_repitions)

    a_in_remainder = 0
    for index in range(0,remainder_chars):
        if s[index] == 'a':
            a_in_remainder += 1
        else:
            pass

    total_a = a_in_substring*whole_repitions + a_in_remainder

    return total_a

if __name__ == '__main__':

    s = 'abcac'
    n = 10
    result = repeatedString(s, n)
    print("1. expected = 4, a's = ", result)

    s = 'aba'
    n = 10
    result = repeatedString(s, n)
    print("2. expected = 7, a's = ", result)

    s = 'a'
    n = 1000000000000
    result = repeatedString(s, n)
    print("3. expected = 1000000000000, a's = ", result)
