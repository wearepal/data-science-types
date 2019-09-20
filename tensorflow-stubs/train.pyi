from typing import Union, Optional

from ._core import Variable, Module
from .keras import Model
from .optimizers import Optimizers

class Checkpoint:
    def __init__(self, **kwargs: Union[Variable, Model, Module, Optimizers]): ...
    def restore(self, save_path: str) -> None: ...

class CheckpointManager:
    def __init__(
        self,
        checkpoint: Checkpoint,
        directory: str,
        max_to_keep: int,
        keep_checkpoint_every_n_hours: Optional[int] = ...,
        checkpoint_name: str = ...,
    ): ...
    @property
    def latest_checkpoint(self) -> str: ...
    def save(self, checkpoint_number: Optional[int] = ...) -> str: ...
