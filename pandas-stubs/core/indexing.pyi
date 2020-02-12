from typing import Union, overload, Sequence, Tuple, List, TypeVar, Generic, Collection
import numpy as _np

from .series import Series
from .frame import DataFrame
from .indexes import Index

_Container = TypeVar("_Container", Series, DataFrame)

class _iLocIndexer(Generic[_Container]):
    @overload
    def __getitem__(self, idx: int) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[slice, _np.ndarray[_np.int64], Index[int]]) -> _Container: ...
    @overload
    def __getitem__(self, idx: Tuple[slice, int]) -> Series: ...
    @overload
    def __setitem__(self, idx: int, value: Union[Series, str]) -> None: ...
    @overload
    def __setitem__(
        self, idx: Union[slice, Sequence[int], _np.ndarray[_np.int64], Index[int]], value: DataFrame
    ) -> None: ...
    @overload
    def __setitem__(
        self,
        idx: Tuple[
            Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int], int, Index[int]],
            Union[str, _np.str_],
        ],
        value: Union[float, _np.ndarray],
    ) -> None: ...
    @overload
    def __setitem__(self, idx: Tuple[Index[int]], value: str) -> None: ...

class _LocIndexer(Generic[_Container]):
    @overload
    def __getitem__(
        self, idx: Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int], List[int], int]
    ) -> _Container: ...
    @overload
    def __getitem__(
        self,
        idx: Tuple[Union[slice, int], Union[bool, _np.str_, Series, _np.ndarray[_np.bool_], Index]],
    ) -> _Container: ...
    @overload
    def __setitem__(
        self,
        idx: Tuple[
            Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int], int, Index[int]],
            Union[str, _np.str_],
        ],
        value: Union[float, _np.ndarray],
    ) -> None: ...
    @overload
    def __setitem__(
        self, idx: Union[Series, _np.ndarray[_np.bool_], _np.ndarray[_np._Int]], value: Series
    ) -> None: ...
