class _DoubleLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return len(self) == 0
    
    def __iter__(self):
        walk = self._header._next
        while walk is not None and walk._next is not None:
            yield walk._element
            walk = walk._next
    
    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node: _Node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
