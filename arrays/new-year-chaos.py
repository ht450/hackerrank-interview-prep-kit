#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    moves = 0

    # reduce numbers by 1 to match list index
    queue = [num-1 for num in q]

    for pos_final,person in enumerate(queue):

        # if more than 2 away from starting position
        if person - pos_final > 2:
            print("Too chaotic")
            return

        # for each person, count the bribes they recieved
        # looking between one ahead of starting pos (person-1)
        # to one ahead of current position (pos_final-1)(+1 to work in range())
        for index in range(max(person-1,0),pos_final-1+1):
            # if someone ahead is larger then they paid a bribe
            if queue[index] > person:
                moves += 1

    print(moves)
    return


if __name__ == '__main__':

    test_list = [
        {"q_input": "5 1 2 3 7 8 6 4","expected": "Too choatic"},
        {"q_input": "1 2 5 3 7 8 6 4","expected": "7"},
        {"q_input": "3 4 5 6 2 1","expected": "9"},
    ]

    for test in test_list:
        q = list(map(int, test['q_input'].rstrip().split()))
        print(q)
        print('ans = ',test['expected'])
        minimumBribes(q)
        print('----------------')