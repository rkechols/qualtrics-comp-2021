#!/bin/python3

import os


# <code>


def alternatingCharacters(s: str) -> int:
    dels = 0
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            dels += 1
    return dels


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s_ = input()
        result = alternatingCharacters(s_)
        fptr.write(str(result) + '\n')
    fptr.close()
