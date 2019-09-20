from typing import List, Tuple

from ._core import Tensor, Variable

class Optimizer:
    #
    # properties
    @property
    def iterations(self) -> Variable: ...
    #
    # methods
    def apply_gradients(self, grads_and_vars: List[Tuple[Tensor, Tensor]]) -> None: ...

class Adam(Optimizer):
    def __init__(
        self,
        learning_rate: float = ...,
        beta_1: float = ...,
        beta_2: float = ...,
        epsilon: float = ...,
    ): ...
