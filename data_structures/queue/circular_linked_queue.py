from data_structures.exceptions import Empty


class CircularQueue:
    """Queue implementation using circularly linked list for storage"""
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next) -> None:
            self._element = element
            self._next = next
    
    def __init__(self) -> None:
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail_next