#!/bin/python3

import os


# <code>


class TreeNode:
    def __init__(self, value: int, n_children: int = 0):
        self.value = value
        self.n_children = n_children
        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError("cannot compare TreeNode with non-TreeNode")
        return self.value < other.value

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError("cannot compare TreeNode with non-TreeNode")
        return self.value == other.value


class Tree:
    def __init__(self):
        self.root: TreeNode = None

    def insert(self, val: int):
        if self.root is None:
            self.root = TreeNode(val)
            return
        assert isinstance(self.root, TreeNode)
        new_node = TreeNode(val)
        current = self.root
        while current is not None:
            if val == current.value:  # found a duplicate
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                elif current.left is None:
                    current.left = new_node
                    new_node.parent = current
                else:  # both children
                    new_node.left = current.left
                    new_node.left.parent = new_node
                    current.left = new_node
                    new_node.parent = current
                break
            elif val < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
        else:
            raise ValueError("Couldn't find an end to the tree...?")
        current = new_node.parent
        while current is not None:
            current.n_children += 1
            current = current.parent

    def remove(self, val: int):
        root = self.root
        if root is None:
            raise ValueError("NO TREE")
        # find the one to delete
        current = self.root
        while current.value != val:
            if val < current.value:
                current = current.left
            else:
                current = current.right
        target = current
        # actually delete it
        if target is root:
            if root.left is None:
                if root.right is None:
                    self.root = None
                else:
                    self.root = root.right
            else:
                if root.right is None:
                    self.root = root.left
                else:
                    # neither is None
                    current = root.left
                    while current.right is not None:
                        current = current.right
                    # right is None
                    root.value = current.value
                    if root.left is current:
                        # went nowhere
                        root.left = current.left
                        if current.left is not None:
                            current.left.parent = root
                    else:
                        current.parent.right = current.left
                        if current.left is not None:
                            current.left.parent = current.parent
                    # update heights in the gap
                    current = current.parent
                    while current is not target:
                        current.n_children -= 1
                        current = current.parent
                    target.n_children -= 1
        else:
            is_left = (target.parent.left is target)
            if target.left is None:
                if target.right is None:
                    if is_left:
                        target.parent.left = None
                    else:
                        target.parent.right = None
                else:
                    if is_left:
                        target.parent.left = target.right
                    else:
                        target.parent.right = target.right
            else:
                if target.right is None:
                    if is_left:
                        target.parent.left = target.left
                    else:
                        target.parent.right = target.left
                else:
                    # neither is None
                    current = target.left
                    while current.right is not None:
                        current = current.right
                    # right is None
                    target.value = current.value
                    if target.left is current:
                        # went nowhere
                        target.left = current.left
                        if current.left is not None:
                            current.left.parent = target
                    else:
                        current.parent.right = current.left
                        if current.left is not None:
                            current.left.parent = current.parent
                    # update heights in the gap
                    current = current.parent
                    while current is not target:
                        current.n_children -= 1
                        current = current.parent
                    target.n_children -= 1
            # update heights above
            current = target.parent
            while current is not None:
                current.n_children -= 1
                current = current.parent

    def __len__(self) -> int:
        if self.root is None:
            return 0
        return 1 + self.root.n_children

    def _get_median_odd(self) -> float:
        split_index = len(self) // 2
        return self.at(split_index)

    def _get_median_even(self) -> float:
        split_index = len(self) // 2
        first = self.at(split_index)
        second = self.at(split_index - 1)
        return (first + second) / 2

    def get_median(self) -> float:
        if self.root is None:
            raise ValueError("NO TREE")
        n_nodes = len(self)  # 1 for the root itself
        if n_nodes % 2 == 0:
            return self._get_median_even()
        else:
            return self._get_median_odd()

    def at(self, index: int) -> int:
        if self.root is None:
            raise ValueError("NO TREE")
        current = self.root
        while current is not None:
            if current.left is None:
                count = 0
            else:
                count = current.left.n_children + 1
            if index < count:
                current = current.left
            elif index == count:
                return current.value
            else:
                index -= (count + 1)
                current = current.right
        raise IndexError("NO SUCH INDEX")


def activityNotifications(expenditure, d):
    t = Tree()
    for i in range(d):
        t.insert(expenditure[i])
    n_ = len(expenditure)
    count = 0
    for i in range(d, n_):
        median = t.get_median()
        if expenditure[i] >= median * 2:
            count += 1
        t.remove(expenditure[i - d])
        t.insert(expenditure[i])
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
