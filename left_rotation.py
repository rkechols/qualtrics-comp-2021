#!/bin/python3

import os


# <code>


from typing import List


def rotateLeft(d: int, arr: List[int]) -> List[int]:
    answer = []
    n = len(arr)
    for i in range(n):
        answer.append(arr[(i + d) % n])
    return answer


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n_ = int(first_multiple_input[0])
    d_ = int(first_multiple_input[1])
    arr_ = list(map(int, input().rstrip().split()))
    result = rotateLeft(d_, arr_)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
