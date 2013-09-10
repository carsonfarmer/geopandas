
# Rename to avoid confusion with pandas indexes
from rtree.index import Index
from rtree.core import RTreeError

# Spatial indexing for faster queries
class RTree(Index):
    """Simple wrapper around rtree Index
    
    TODO: Add ability to serialize index to a file
          rtree can already do this, integrate 
          with pandas picking...
    """

    def __init__(self):
        Index.__init__(self)

    @property
    def size(self):
        return len(self.leaves()[0][1])

    @property
    def is_empty(self):
        if len(self.leaves()) > 1:
            return False
        return self.size < 1
