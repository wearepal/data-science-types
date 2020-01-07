from typing import Union, overload, Sequence
import numpy as _np

from .series import Series
from .frame import DataFrame
from .indexes import Index

class _iLocIndexer:
    @overload
    def __getitem__(self, idx: int) -> Series: ...
    @overload
    def __getitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[_np.int64], Index[int]]
    ) -> DataFrame: ...
    @overload
    def __setitem__(self, idx: int, value: Series) -> None: ...
    @overload
    def __setitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[_np.int64], Index[int]], value: DataFrame
    ) -> None: ...

class _LocIndexer:
    def __getitem__(self, idx: Union[Series, _np.ndarray[_np.bool_]]) -> DataFrame: ...
    def __setitem__(self, idx: Union[Series, _np.ndarray[_np.bool_]], value: Series) -> None: ...
