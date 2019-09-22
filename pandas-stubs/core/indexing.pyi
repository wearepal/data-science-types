from typing import (
    Union,
    overload,
    Sequence,
)
import numpy as _np

class _iLocIndexer:
    @overload
    def __getitem__(self, idx: int) -> Series: ...
    @overload
    def __getitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[int], Index[int]]
    ) -> DataFrame: ...
    @overload
    def __setitem__(self, idx: int, value: Series) -> None: ...
    @overload
    def __setitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[int], Index[int]], value: DataFrame
    ) -> None: ...

class _LocIndexer:
    def __getitem__(self, idx: Union[Series, _np.ndarray[bool]]) -> DataFrame: ...
    def __setitem__(self, idx: Union[Series, _np.ndarray[bool]], value: Series) -> None: ...
