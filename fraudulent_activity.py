#!/bin/python3

import os


# <code>


def activityNotifications(expenditure, d):
    count = 0
    for i in range(d, len(expenditure)):
        chunk = expenditure[i - d:i]
        chunk.sort()
        n = len(chunk)
        split_index = n // 2
        if n % 2 == 0:
            first = chunk[split_index]
            second = chunk[split_index - 1]
            median = (first + second) / 2
        else:
            median = chunk[split_index]
        if expenditure[i] >= median * 2:
            count += 1
    return count


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
