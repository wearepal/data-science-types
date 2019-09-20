from ._core import Tensor

class Metric:
    def update_state(self, values: Tensor) -> None: ...
    def result(self) -> Tensor: ...

class Mean(Metric):
    pass
