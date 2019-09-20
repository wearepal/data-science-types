from .._core import Tensor

class Layer:
    def __call__(self, x: Tensor, training: bool = ...) -> Tensor: ...

class Flatten(Layer):
    pass
