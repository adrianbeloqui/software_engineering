class EulerTour:
    """Abstract base class for performing Euler tour of a tree.
    
    _hook_previsit and _hook_postivist may be overriden by subclasses"""

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree"""
        self._tree = tree
    
    def tree(self):
        """Return reference to the tree being traversed"""
        return self._tree
    
    def execute(self):
        """Perform the tour and return any results from. post visit of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])
        
    def _tour(self, p, d, path):
        """Perform tour of subree rooted at Position p
        
        p    Position of current node being visited
        d    depth of p in tree
        path list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer
    
    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path):
        pass
    