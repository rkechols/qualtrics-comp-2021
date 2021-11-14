#!/bin/python3

import os


# <code>


from typing import Dict, Set, List


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


def dfs_make_directed(current: int, graph: Dict[int, Set[int]]):
    for child in graph[current]:  # base case is when it has no children
        graph[child].discard(current)
        dfs_make_directed(child, graph)


class Solver:
    def __init__(self, c: List[int], edges: List[List[int]]):
        self.c = c
        self.minimum = -1
        # build an adjacency list structure from the undirected edges
        self.graph = {i: set() for i in range(len(c))}
        for x, y in edges:
            self.graph[x - 1].add(y - 1)
            self.graph[y - 1].add(x - 1)
        # pick an arbitrary node as root and make the graph directed, edges leading only away from the root
        self.root = 0
        dfs_make_directed(self.root, self.graph)
        # adjust the values of c
        self._dfs_weights(self.root)

    def _dfs_weights(self, index: int) -> int:
        for child in self.graph[index]:
            self.c[index] += self._dfs_weights(child)
        return self.c[index]

    def solve(self, parents: Set[int], tw: int, prev: Set[int], index: int):
        # print(f"{parents=}")
        # print(f"{tw=}")
        # print(f"{prev=}")
        # print(f"{index=}")
        # print(f"{graph=}")
        # print(f"{c=}")
        # print("-----")
        if len(parents) > 0:
            self.tricut(parents, prev, tw, self.c[index])
            # print(MIN)
        parents.add(self.c[index])
        for child in self.graph[index]:
            self.solve(parents, tw, prev, child)
        parents.discard(self.c[index])
        prev.add(self.c[index])

    def tricut(self, parents: Set[int], prev: Set[int], tw: int, nw: int):
        if nw < (tw / 3):
            if (tw - nw) % 2 == 0:
                tw_stuff = (tw - nw) // 2
                if findcut(parents, prev, tw_stuff, nw):
                    # print("FINDCUT SAID YES")
                    self.upmin(tw_stuff - nw)
        # elif nw == tw - nw:
        #     # upmin(nw)
        #     pass
        elif nw > (tw / 3):
            if findcut(parents, prev, nw, nw) or findcut(parents, prev, tw - (2 * nw), nw):
                # print("FINDCUT SAID YES")
                self.upmin((3 * nw) - tw)

    def upmin(self, x: int):
        if self.minimum == -1 or x < self.minimum:
            self.minimum = x


def balancedForest(c: List[int], edges: List[List[int]]) -> int:
    # print("******************************************")
    solver = Solver(c, edges)
    parents = set()
    prev = set()
    solver.solve(parents, c[solver.root], prev, solver.root)
    return solver.minimum


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n_ = int(input().strip())
        c_ = list(map(int, input().rstrip().split()))
        edges_ = []
        for _ in range(n_ - 1):
            edges_.append(list(map(int, input().rstrip().split())))
        result = balancedForest(c_, edges_)
        fptr.write(str(result) + '\n')
    fptr.close()
