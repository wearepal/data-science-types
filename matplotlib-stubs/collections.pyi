from .artist import Artist
from .cm import ScalarMappable

class Collection(Artist, ScalarMappable):
    pass

class _CollectionWithSizes(Collection):
    pass

class PolyCollection(_CollectionWithSizes):
    pass
