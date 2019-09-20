from typing import List

from .layers import Layer

class Model(Layer):
    pass

class Sequential(Model):
    def __init__(self, layers: List[Layer]): ...
