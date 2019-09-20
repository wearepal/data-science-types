from typing import List

import tensorflow as _tf

class Bijector:
    def forward(self, x: _tf.Tensor) -> _tf.Tensor: ...
    def inverse(self, x: _tf.Tensor) -> _tf.Tensor: ...

class Chain(Bijector):
    def __init__(self, bijectors: List[Bijector]): ...
