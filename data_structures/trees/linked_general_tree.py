from data_structures.trees.tree_adt import Tree


class LinkedGeneralTree(Tree):
    """Linked representation of a general tree structure"""

    class _Node:
        __slots__ = '_element', '_parent', '_children'
        
        def __init__(self, element, parent=None, children=[]):
            self._element = element
            self._parent = parent
            self._children = children  # This is better implemented with a Positional List data_structures/linked_lists/positional_list.py

    class Position(Tree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p) -> _Node:
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated node
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node) -> Position:
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    def __len__(self):
        """Running Performance: This runs in O(1) time because it only has to access a property of the object that takes constant time"""
        return self._size
    
    def root(self) -> Position:
        """Running Performance: This runs in O(1) time because it only has to access a property of the object that takes constant time"""
        return self._make_position(self._root)
    
    def parent(self, p) -> Position:
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        node = self._validate(p)
        if node:
            for c in node._children:
                yield self._make_position(c)
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    