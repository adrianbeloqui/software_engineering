class MultiMap:
    """A multimap class built upon use of an underlying map for storage"""
    _MapType = dict                     # Map type; can be redefined by subclass

    def __init__(self):
        """Create a new empty multimap instance"""
        self._map = self._MapType()
        self._n = 0

    def __iter__(self):
        """Iterate through all (k,v) pairs in multimap"""
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k, v)
    
    def add(self, k, v):
        """Add pair (k,v) to multimap"""
        container = self._map.setdefault(k, [])      # create empty list, if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k,v) with key k (or raise KeyError)"""
        secondary = self._map[k]
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]
        self._n -= 1
        return (k,v)
    
    def find(self, k):
        """Return arbitrary (k,v) pair given key (or raise KeyError)"""
        secondary = self._map[k]
        return (k, secondary[0])
    
    def find_all(self, k):
        """Generate iteration of all (k,v) pairs with given key"""
        secondary = self._map[k]
        for v in secondary:
            yield (k,v)
