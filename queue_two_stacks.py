# <code>

from collections import deque


def q_pop(en_: deque, de_: deque):
    if len(de_) == 0:
        while len(en_) > 0:
            de_.append(en_.pop())


if __name__ == "__main__":
    q = int(input())
    en = deque()
    de = deque()
    for _ in range(q):
        line = input().split()
        if len(line) == 1:
            if line[0] == "2":
                q_pop(en, de)
                de.pop()
            else:
                q_pop(en, de)
                top = de[-1]
                print(top)
        else:
            val = line[1]
            en.append(val)


# </code>
