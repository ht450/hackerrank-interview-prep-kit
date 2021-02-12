#!/bin/python3

import math
import os
import random
import re
import sys
max_daily_expenditure = 200


# Complete the activityNotifications function below.
def activityNotifications(expenditure, trailing_days):
    notifications = 0

    # count sort
    expend_sort_list = [0] * (max_daily_expenditure+1)
    for day_index in expenditure[:trailing_days]:
        expend_sort_list[day_index] += 1

    # is notification needed
    for day_index, day_spend in enumerate(expenditure[trailing_days:]):
        limit = get_limit(expend_sort_list, trailing_days)
        if day_spend >= limit:
            notifications += 1

        # set up for next day
        expend_sort_list[day_spend] += 1
        expend_sort_list[expenditure[day_index]] -= 1

    return notifications


def get_limit(expend_sort_list, trailing_days):

    count = 0
    m1 = trailing_days//2
    m2 = trailing_days//2 + 1
    m = []

    # collect middle values
    for spend, spend_count in enumerate(expend_sort_list):
        count += spend_count
        if not m and m1 <= count:
            m.append(spend)
        if m2 <= count:
            m.append(spend)
            break

    # if odd, return middle * 2, if even return (m1+m2)/2 *2
    if trailing_days % 2:
        return m[-1]*2
    else:
        return sum(m)

if __name__ == '__main__':

    n, d = 9, 5
    transactions = "2 3 4 2 3 6 8 4 5"
    expected = 2
    expenditure = list(map(int, transactions.rstrip().split()))
    result = activityNotifications(expenditure, d)
    print("ans", expected)
    print("res", result)

    n, d = 5, 4
    transactions = "1 2 3 4 4"
    expected = 0
    expenditure = list(map(int, transactions.rstrip().split()))
    result = activityNotifications(expenditure, d)
    print("ans", expected)
    print("res", result)
