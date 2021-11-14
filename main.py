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


def dfs_make_directed(current: int, graph: Dict[int, Set[int]]):
    for child in graph[current]:  # base case is when it has no children
        graph[child].discard(current)
        dfs_make_directed(child, graph)


def balancedForest(c, edges):
    # print("******************************************")
    global MIN
    MIN = -1
    n = len(c)
    # build an adjacency list structure from the undirected edges
    graph = {i: set() for i in range(n)}
    for x, y in edges:
        graph[x - 1].add(y - 1)
        graph[y - 1].add(x - 1)
    # pick an arbitrary node as root and make the graph directed, edges leading only away from the root
    root = 0
    dfs_make_directed(root, graph)
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
