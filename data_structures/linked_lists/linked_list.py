from data_structures.linked_lists.node import Node

# Look at the implementation of Stack and Queue using linked lists

class LinkedList:
    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def append(self, element) -> None:
        newest = Node(element, None)
        if self._size == 0:
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1