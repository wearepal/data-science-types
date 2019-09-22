from typing import (
    List,
    Iterator,
    Type,
    Generic,
    TypeVar,
)
import numpy as _np

from .series import Series

_T = TypeVar('_T', str, int)

class Index(Generic[_T]):
    # magic methods
    def __eq__(self, other: object) -> Series: ...  # type: ignore
    def __getitem__(self, idx: int) -> _T: ...
    def __iter__(self) -> Iterator: ...
    #
    # properties
    @property
    def names(self) -> List[str]: ...
    @property
    def values(self) -> _np.ndarray: ...
    #
    # methods
    def astype(self, dtype: Type) -> Index: ...
    def get_level_values(self, level: str) -> Index: ...
    def to_frame(self) -> DataFrame: ...
