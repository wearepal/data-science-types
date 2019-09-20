from .._core import Tensor

class Regularizer:
    def __call__(self) -> Tensor: ...

class L1L2(Regularizer):
    def __init__(self, l1: float = ..., l2: float = ...): ...
