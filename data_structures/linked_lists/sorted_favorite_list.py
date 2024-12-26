from data_structures.linked_lists.positional_list import PositionalList

class FavoriteList:
    """List of elements ordered from most frequently accessed to least."""

    class _Item:
        __slots__ = ['_value', '_count']
        def __init__(self, e) -> None:
            self._value = e
            self._count = 0
            
    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))
                
    def __init__(self) -> None:
        self._data = PositionalList()
        
    def __len__(self):
        return len(self._data)
    
    def __str__(self) -> str:
        return ",".join(str(i) for i in self)
    
    def __iter__(self):
        walk = self._data._header._next
        while walk is not None and walk._next is not None:
            yield walk._element
            walk = walk._next
    
    def is_empty(self):
        return len(self) == 0
    
    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)
        
    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
            
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
            
    