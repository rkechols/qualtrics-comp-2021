#!/bin/python3

import os


# <code>


def rotateLeft(d, arr):
    answer = []
    n = len(arr)
    for i in range(n):
        answer.append(arr[(i + d) % n])
    return answer


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
