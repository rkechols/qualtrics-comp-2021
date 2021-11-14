#!/bin/python3

import os


def all_equal(h1_sum, h2_sum, h3_sum):
    return h1_sum == h2_sum and h2_sum == h3_sum


def equalStacks(h1, h2, h3):
    h1 = list(reversed(h1))
    h2 = list(reversed(h2))
    h3 = list(reversed(h3))
    h1_sum = sum(h1)
    h2_sum = sum(h2)
    h3_sum = sum(h3)
    while not all_equal(h1_sum, h2_sum, h3_sum):
        if h1_sum >= h2_sum and h1_sum >= h3_sum:
            to_remove = h1[-1]
            del h1[-1]
            h1_sum -= to_remove
        elif h2_sum >= h1_sum and h2_sum >= h3_sum:
            to_remove = h2[-1]
            del h2[-1]
            h2_sum -= to_remove
        else:
            to_remove = h3[-1]
            del h3[-1]
            h3_sum -= to_remove
    return h1_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    fptr.write(str(result) + '\n')
    fptr.close()
