from typing import Union, overload, Sequence, Tuple, List
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
    def __getitem__(self, idx: Tuple[slice, Union[bool, int]]) -> DataFrame: ...
    @overload
    def __setitem__(self, idx: int, value: Union[Series, str]) -> None: ...
    @overload
    def __setitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[_np.int64], Index[int]], value: DataFrame
    ) -> None: ...
    @overload
    def __setitem__(self, idx: Tuple[slice, Union[bool, int]], value: DataFrame) -> None: ...

class _LocIndexer:
    @overload
    def __getitem__(self, idx: Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int], List[int], int]) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: Tuple[Union[slice, int], Union[bool, _np.str_, Series, _np.ndarray[_np.bool_], Index]]) -> DataFrame: ...
    @overload
    def __setitem__(self, idx: Tuple[Union[Series, _np.ndarray[_np.bool_], _np.ndarray[int], int], Union[str, _np.str_]], value: Union[float, _np.ndarray]) -> None: ...
    @overload
    def __setitem__(self, idx: Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int]], value: Series) -> None: ...
