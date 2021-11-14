#!/bin/python3

import os


# <code>


A_INT = ord("a")


def sherlockAndAnagrams(s: str) -> int:
    final = dict()
    prev = dict()
    for c in s:
        c_int = ord(c) - A_INT
        next_ = dict()
        t = tuple((1 if i == c_int else 0) for i in range(26))
        next_[t] = 1
        for k, v in prev.items():
            k_copy = tuple((val if i != c_int else val + 1) for i, val in enumerate(k))
            if k_copy in next_:
                next_[k_copy] += v
            else:
                next_[k_copy] = v
        for k, v in next_.items():
            if k in final:
                final[k] += v
            else:
                final[k] = v
        prev = next_

    count = 0
    for k, v in final.items():
        # print(f"{k} : {v}")
        count += (v * (v - 1)) // 2

    return count


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s_ = input()
        result = sherlockAndAnagrams(s_)
        fptr.write(str(result) + '\n')
    fptr.close()
