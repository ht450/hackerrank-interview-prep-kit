#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley_count = 0
    altitude = 0
    first_step_from_level = True
    valley = False
    mountain = False
    
    # go through steps
    for step in path:
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1
        
        if altitude == 0:
            mountain = False
            valley = False
            first_step_from_level = True
        elif altitude > 0:
            mountain = True
            first_step_from_level = False
        elif altitude < 0:
            valley = True
            if first_step_from_level:
                valley_count += 1
                first_step_from_level = False


    return valley_count

if __name__ == '__main__':
    
    steps = 8
    path = "UDDDUDUU"
    result = countingValleys(steps, path)
    print("1. expected = 1, valleys counted = ",result)

    steps = 12
    path = "DDUUDDUDUUUD"
    result = countingValleys(steps, path)
    print("2. expected = 2, valleys counted = ",result)