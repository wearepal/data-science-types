from pathlib import Path
from typing import (
    Any,
    Tuple,
    List,
    Union,
    Callable,
    Dict,
    Optional,
    Type,
    TypeVar,
    overload,
    Iterator,
    Sequence,
    Generator,
    Iterable,
)
from typing_extensions import Literal
import matplotlib
import numpy as _np

from .groupby.generic import DataFrameGroupBy, SeriesGroupBy
from .indexes import Index
from .indexing import _iLocIndexerFrame, _LocIndexerFrame, _AtIndexerFrame
from .series import Series, _DTypeNp
from .strings import StringMethods

_str = str  # needed because DataFrame has a property called "str"...

_AxisType = Literal["columns", "index"]

_ErrorType = Literal['raise', 'ignore']

_ListLike = Union[Series, Index, _np.ndarray, Sequence]

_DType = TypeVar("_DType", bound=_np.dtype)

_ColSubsetType = Union[Series, 'DataFrame', List[_str], _str, _np.ndarray[_np.str_]]

class DataFrame:
    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[_str, _np.ndarray]]] = ...,
        columns: Optional[_ListLike] = ...,
        index: Optional[_ListLike] = ...,
        dtype: Optional[Type[_np.dtype]] = ...,
    ): ...
    #
    # magic methods
    def __eq__(self, other: Union[float, Series, DataFrame]) -> DataFrame: ...  # type: ignore
    def __ne__(self, other: Union[float, Series, DataFrame]) -> DataFrame: ...  # type: ignore
    @overload
    def __getitem__(self, idx: _str) -> Series: ...
    @overload
    def __getitem__(
        self, idx: Union[Series, DataFrame, List[_str], Index[_str], _np.ndarray[_np.str_]]
    ) -> DataFrame: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __le__(self, other: float) -> DataFrame: ...
    def __lt__(self, other: float) -> DataFrame: ...
    def __ge__(self, other: float) -> DataFrame: ...
    def __gt__(self, other: float) -> DataFrame: ...
    def __mul__(self, other: float) -> DataFrame: ...
    def __floordiv__(self, other: float) -> DataFrame: ...
    def __and__(self, other: DataFrame) -> DataFrame: ...
    def __add__(self, other: float) -> DataFrame: ...
    def __or__(self, other: DataFrame) -> DataFrame: ...
    #
    # properties
    @property
    def columns(self) -> Index[_str]: ...
    @columns.setter  # setter needs to be right next to getter; otherwise mypy complains
    def columns(self, cols: Union[List[_str], Index[_str]]) -> None: ...
    @property
    def dtypes(self) -> Series: ...
    @property
    def iloc(self) -> _iLocIndexerFrame: ...
    @property
    def index(self) -> Index[int]: ...
    @index.setter
    def index(self, idx: Index) -> None: ...
    @property
    def loc(self) -> _LocIndexerFrame: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    @property
    def str(self) -> StringMethods: ...
    @property
    def T(self) -> DataFrame: ...
    # this function is deprecated:
    @property
    def values(self) -> _np.ndarray: ...
    #
    # methods
    def append(
        self, s: Union[DataFrame, Dict[_str, Any]], ignore_index: bool = ..., sort: bool = ...
    ) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series: ...
    @overload
    def apply(self, f: Callable[..., _ListLike], axis: _AxisType = ...) -> DataFrame: ...
    def astype(
        self,
        dtype: Union[_str, Type[_np.dtype], Dict[_str, Type[_np.dtype]]],
        copy: bool = ...,
        errors: _ErrorType = ...,
    ) -> DataFrame: ...
    def copy(self, deep: bool = ...) -> DataFrame: ...
    def corr(self, method: Optional[_str] = ..., min_periods: Optional[int] = ...) -> DataFrame: ...
    def count(self) -> Series: ...
    def drop(self, index: Union[List[_str], Index], axis: _AxisType = ...) -> DataFrame: ...
    def drop_duplicates(self, keep: Union[_str, bool] = ...) -> DataFrame: ...
    @overload
    def dropna(
        self,
        inplace: Literal[False] = ...,
        axis: int = ...,
        how: _str = ...,
        subset: _ColSubsetType = ...,
    ) -> DataFrame: ...
    @overload
    def dropna(
        self, inplace: Literal[True], axis: int = ..., how: _str = ..., subset: _ColSubsetType = ...
    ) -> None: ...
    @overload
    def fillna(
        self,
        value: Union[float, Dict, Series, DataFrame, _str] = ...,
        method: _str = ...,
        axis: Union[_str, int] = ...,
        inplace: Literal[False] = ...,
        limit: int = ...,
        downcast: Dict = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        inplace: Literal[True],
        value: Union[float, Dict, Series, DataFrame, _str] = ...,
        method: _str = ...,
        axis: Union[_str, int] = ...,
        limit: int = ...,
        downcast: Dict = ...,
    ) -> None: ...
    @overload
    def groupby(self, by: List[_str]) -> DataFrameGroupBy: ...
    @overload
    def groupby(self, by: _str) -> SeriesGroupBy: ...
    def head(self, n: int) -> DataFrame: ...
    def idxmax(self, axis: _AxisType) -> Series: ...
    def isin(self, values: Union[Iterable, Series, DataFrame, Dict]) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def iterrows(self) -> Generator[Series, Series, Series]: ...
    def max(self) -> Series: ...
    def mean(self) -> DataFrame: ...
    def min(self) -> Series: ...
    def mode(self, axis: _AxisType = ...) -> DataFrame: ...
    def median(
        self, axis: int = ..., skipna: bool = ..., level: Union[int, _str] = ...
    ) -> Union[DataFrame, Series]: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    def nunique(self) -> Series: ...
    def plot(self, kind: _str, yerr: DataFrame) -> matplotlib.axes.Axes: ...
    def query(self, expr: _str) -> DataFrame: ...
    def reindex(self, index: Index) -> DataFrame: ...
    @overload
    def rename(self, mapper: Callable, axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def rename(self, columns: Dict[_str, _str]) -> DataFrame: ...
    def replace(self, a: float, b: float) -> DataFrame: ...
    @overload
    def reset_index(self, drop: bool = ...) -> DataFrame: ...
    @overload
    def reset_index(self, inplace: Literal[True], drop: bool = ...) -> None: ...
    @overload
    def sample(self, frac: float, random_state: int = ..., replace: bool = ...) -> DataFrame: ...
    @overload
    def sample(self, n: int, random_state: int = ..., replace: bool = ...) -> DataFrame: ...
    @overload
    def sample(self, n: int, random_state: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def sample(self, axis: _str, frac: float) -> DataFrame: ...
    def set_index(self, index: Union[_str, List[_str]]) -> DataFrame: ...
    @overload
    def sort_values(
        self, by: List[_str], inplace: Literal[True], axis: _AxisType = ..., ascending: bool = ...
    ) -> None: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        inplace: Optional[Literal[False]] = ...,
        axis: _AxisType = ...,
        ascending: bool = ...,
    ) -> DataFrame: ...
    def std(self) -> DataFrame: ...
    @overload
    def sum(self) -> Series: ...
    @overload
    def sum(self, axis: _AxisType) -> Series: ...
    def to_csv(self, filename: Union[Path, _str], index: bool = ...) -> None: ...
    @overload
    def to_dict(self) -> Dict[_str, Any]: ...
    @overload
    def to_dict(self, orient: _str) -> List[Dict[_str, Any]]: ...
    def to_feather(self, filename: Path) -> None: ...
    def to_html(self) -> _str: ...
    @overload
    def to_numpy(self) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Type[_DTypeNp]) -> _np.ndarray[_DTypeNp]: ...
    def unique(self) -> DataFrame: ...
    def update(self, other: Union[DataFrame, Series]) -> None: ...
    def where(self, cond: Union[Series, DataFrame, _np.ndarray]) -> DataFrame: ...
    @property
    def at(self) -> _AtIndexerFrame: ...

# Local Variables:
# blacken-line-length: 100
# blacken-allow-py36: t
# blacken-skip-string-normalization: t
# End:
