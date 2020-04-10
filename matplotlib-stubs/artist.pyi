class Artist:
    def set_label(self, s: str) -> None: ...

class Line2D(Artist):
    pass

class Collection(Artist):
    pass

class LineCollection(Collection):
    pass

class Patch(Artist):
    pass

class Rectangle(Patch):
    pass
