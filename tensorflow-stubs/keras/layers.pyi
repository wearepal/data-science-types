from .._core import Tensor

class Layer:
    def __call__(self, x: Tensor) -> Tensor: ...
