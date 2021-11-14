#!/bin/python3

import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


# <code>


def insertNodeAtPosition(llist: SinglyLinkedListNode, data: int, position: int) -> SinglyLinkedListNode:
    if position == 0:
        new_head = SinglyLinkedListNode(data)
        new_head.next = llist
        return new_head

    current = llist
    for _ in range(1, position):
        current = current.next
    new_node = SinglyLinkedListNode(data)
    new_node.next = current.next
    current.next = new_node
    return llist


# </code>


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    llist_count = int(input())
    llist_ = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist_.insert_node(llist_item)
    data_ = int(input())
    position_ = int(input())
    llist_head = insertNodeAtPosition(llist_.head, data_, position_)
    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')
    fptr.close()
