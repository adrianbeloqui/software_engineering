from data_structures.linked_lists.double_linked_base import _DoubleLinkedBase

class PositionalList(_DoubleLinkedBase):
    class Position:
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            
        def element(self):
            return self._node._element
        
        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other) -> bool:
            return not (self == other)
    
    def _validate(self, p: Position) -> _DoubleLinkedBase._Node:
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self) -> Position:
        return self._make_position(self._header._next)
    
    def last(self) -> Position:
        return self._make_position(self._trailer._prev)
    
    def before(self, p) -> Position:
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p) -> Position:
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    def _insert_between(self, e, predecessor: _DoubleLinkedBase._Node, successor: _DoubleLinkedBase._Node) -> Position:
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
            
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
        