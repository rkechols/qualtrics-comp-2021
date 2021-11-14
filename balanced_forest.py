#!/bin/python3

import os


# <code>


from typing import Dict, Set, List


MIN = -1


def dfs_weights(graph: Dict[int, Set[int]], c: List[int], index: int) -> int:
    for child in graph[index]:
        c[index] += dfs_weights(graph, c, child)
    return c[index]


def findcut(parents: Set[int], prev: Set[int], cut: int, nw: int) -> bool:
    # print("----FINDCUT----")
    # print(f"{parents=}")
    # print(f"{prev=}")
    # print(f"{cut=}")
    # print(f"{nw=}")
    # print("----FINDCUT END----")
    if cut in prev:
        return True
    if cut + nw in parents:
        return True
    return False


def upmin(x: int):
    global MIN
    if MIN == -1 or x < MIN:
        MIN = x


def tricut(parents: Set[int], prev: Set[int], tw: int, nw: int):
    if nw < (tw / 3):
        if (tw - nw) % 2 == 0:
            tw_stuff = (tw - nw) // 2
            if findcut(parents, prev, tw_stuff, nw):
                # print("FINDCUT SAID YES")
                upmin(tw_stuff - nw)
    elif nw == tw - nw:
        # upmin(nw)
        pass
    elif nw > (tw / 3):
        if findcut(parents, prev, nw, nw) or findcut(parents, prev, tw - (2 * nw), nw):
            # print("FINDCUT SAID YES")
            upmin((3 * nw) - tw)


def find_sol(parents: Set[int], tw: int, prev: Set[int], index: int, graph: Dict[int, Set[int]], c: List[int]):
    # print(f"{parents=}")
    # print(f"{tw=}")
    # print(f"{prev=}")
    # print(f"{index=}")
    # print(f"{graph=}")
    # print(f"{c=}")
    # print("-----")
    if len(parents) > 0:
        tricut(parents, prev, tw, c[index])
        # print(MIN)
    parents.add(c[index])
    for child in graph[index]:
        find_sol(parents, tw, prev, child, graph, c)
    parents.discard(c[index])
    prev.add(c[index])


def balancedForest(c, edges):
    # print("******************************************")
    global MIN
    MIN = -1
    n = len(c)
    graph = { i: set() for i in range(n) }
    for x, y in edges:
        graph[x - 1].add(y - 1)
    root = 0
    while True:
        for top, children in graph.items():
            if root in children:
                root = top
                break
        else:
            break
    dfs_weights(graph, c, root)
    parents = set()
    prev = set()
    find_sol(parents, c[root], prev, root, graph, c)
    return MIN


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        c = list(map(int, input().rstrip().split()))
        edges = []
        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))
        result = balancedForest(c, edges)
        fptr.write(str(result) + '\n')
    fptr.close()
