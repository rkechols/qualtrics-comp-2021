#!/bin/python3

import os


# <code>


from typing import List
from bisect import bisect_left, insort


def activityNotifications(expenditure: List[int], d: int) -> int:
    count = 0
    chunk = expenditure[:d]
    chunk.sort()
    split_index = d // 2
    for i in range(d, len(expenditure)):
        if d % 2 == 0:
            first = chunk[split_index]
            second = chunk[split_index - 1]
            median = (first + second) / 2
        else:
            median = chunk[split_index]
        if expenditure[i] >= median * 2:
            count += 1
        del chunk[bisect_left(chunk, expenditure[i - d])]
        insort(chunk, expenditure[i])
    return count


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d_ = int(first_multiple_input[1])
    expenditure_ = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure_, d_)
    fptr.write(str(result) + '\n')
    fptr.close()
