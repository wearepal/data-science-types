from typing import Optional, Union

from . import experimental
from .._core import Tensor

class SummaryWriter:
    pass

def create_file_writer(logdir: str) -> SummaryWriter: ...
def image(name: str, data: Tensor, step: Optional[int] = ...) -> None: ...
def scalar(name: str, data: Union[Tensor, int, float], step: Optional[int] = ...) -> None: ...
