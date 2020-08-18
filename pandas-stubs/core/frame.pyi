from pathlib import Path
from typing import (
    Any,
    Tuple,
    List,
    Union,
    Callable,
    Dict,
    Mapping,
    NamedTuple,
    Optional,
    Type,
    TypeVar,
    overload,
    Iterator,
    Sequence,
    Generator,
    Iterable,
    Hashable,
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

_AxisType = Literal["columns", "index", 0, 1]

_ErrorType = Literal["raise", "ignore"]

_ListLike = Union[Series, Index, _np.ndarray, Sequence]

_ColSubsetType = Union[Series, DataFrame, List[_str], _str, _np.ndarray[_np.str_]]

_FunctionLike = Union[_str, Callable]

_TypeLike = Union[_str, _np.dtype, Type[_np.generic], Type[float], Type[_str]]

_Label = Optional[Hashable]

_Renamer = Union[Mapping[_Label, Any], Callable[[_Label], _Label]]

class DataFrame:
    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[_str, _ListLike]]] = ...,
        columns: Optional[_ListLike] = ...,
        index: Optional[_ListLike] = ...,
        dtype: Optional[_TypeLike] = ...,
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
    def __getattr__(self, name: _str) -> Series: ...
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
    @property
    def empty(self) -> bool: ...
    #
    # methods
    @overload
    def any(
        self, axis: Optional[_AxisType] = ..., bool_only: Optional[bool] = ..., skipna: bool = ...
    ) -> Series: ...
    @overload
    def any(
        self,
        level: int,
        axis: Optional[_AxisType] = ...,
        bool_only: Optional[bool] = ...,
        skipna: bool = ...,
    ) -> DataFrame: ...
    def append(
        self, s: Union[DataFrame, Dict[_str, Any]], ignore_index: bool = ..., sort: bool = ...
    ) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series: ...
    @overload
    def apply(self, f: Callable[..., _ListLike], axis: _AxisType = ...) -> DataFrame: ...
    def astype(
        self,
        dtype: Union[_TypeLike, Dict[Hashable, _TypeLike]],
        copy: bool = ...,
        errors: _ErrorType = ...,
    ) -> DataFrame: ...
    def copy(self, deep: bool = ...) -> DataFrame: ...
    def corr(self, method: Optional[_str] = ..., min_periods: Optional[int] = ...) -> DataFrame: ...
    def count(self) -> Series: ...
    @overload
    def drop(self, labels: Union[List[_str], Index], axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def drop(self, *, index: Union[List[_str], Index]) -> DataFrame: ...
    @overload
    def drop(self, *, columns: Union[_str, List[_str], Index]) -> DataFrame: ...
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
    def groupby(
        self,
        by: Union[
            _str,
            Tuple[_str, ...],
            List[_str],
            List[Tuple[_str, _str]],
            List[Tuple[_str, _str, _str]],
        ],
        level: Union[int, _str] = ...,
        as_index: bool = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: bool = ...,
        observed: bool = ...,
    ) -> DataFrameGroupBy: ...
    @overload
    def groupby(
        self,
        by: Union[Series[_str], Dict[_str, _str], Callable],
        axis: _AxisType = ...,
        level: Union[int, _str] = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: bool = ...,
        observed: bool = ...,
    ) -> DataFrameGroupBy: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def idxmax(self, axis: _AxisType = ...) -> Series: ...
    def idxmin(self, axis: _AxisType = ...) -> Series: ...
    def insert(
        self, loc: int, column: _str, value: _ListLike, allow_duplicates: bool = ...,
    ) -> None: ...
    def isin(self, values: Union[Iterable, Series, DataFrame, Dict]) -> DataFrame: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def iterrows(self) -> Iterator[Tuple[_Label, Series]]: ...
    @overload
    def itertuples(self, name: Literal[None], index: bool = ...) -> Iterator[Tuple[Any, ...]]: ...
    @overload
    def itertuples(self, name: _str, index: bool = ...,) -> Iterator[NamedTuple]: ...
    @overload
    def itertuples(self, index: bool = ...) -> Iterator[NamedTuple]: ...
    def max(self) -> Series: ...
    def mean(self) -> Series: ...
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
    # rename specifying mapper= and axis=
    @overload
    def rename(self, mapper: _Renamer, inplace: Literal[True], axis: _AxisType = ...,) -> None: ...
    @overload
    def rename(
        self, mapper: _Renamer, inplace: Literal[False], axis: _AxisType = ...,
    ) -> DataFrame: ...
    @overload
    def rename(self, mapper: _Renamer, axis: _AxisType = ...,) -> DataFrame: ...
    @overload
    # rename specifying columns=
    def rename(self, *, columns: _Renamer, inplace: Literal[True]) -> None: ...
    @overload
    def rename(self, *, columns: _Renamer, inplace: Literal[False]) -> DataFrame: ...
    @overload
    def rename(self, *, columns: _Renamer) -> DataFrame: ...
    # rename specifying index=
    @overload
    def rename(self, *, index: _Renamer, inplace: Literal[True]) -> None: ...
    @overload
    def rename(self, *, index: _Renamer, inplace: Literal[False]) -> DataFrame: ...
    @overload
    def rename(self, *, index: _Renamer) -> DataFrame: ...
    def replace(
        self, a: Union[_np.dtype, _str], b: Union[_np.dtype, float, _str], regex: bool = ...
    ) -> DataFrame: ...
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
    def sort_index(self, axis: _AxisType) -> DataFrame: ...
    @overload
    def sort_values(
        self,
        by: Union[_str, List[_str]],
        inplace: Literal[True],
        axis: _AxisType = ...,
        ascending: bool = ...,
    ) -> None: ...
    @overload
    def sort_values(
        self,
        by: Union[_str, List[_str]],
        inplace: Optional[Literal[False]] = ...,
        axis: _AxisType = ...,
        ascending: bool = ...,
    ) -> DataFrame: ...
    def std(self) -> Series: ...
    def sum(self, axis: _AxisType = ...) -> Series: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def to_csv(
        self,
        path_or_buf: Optional[Union[Path, _str]] = ...,
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Optional[Hashable]]] = ...,
        header: Union[bool, List[_str]] = ...,
        index: bool = ...,
        index_label: Optional[Union[bool, _str, Sequence[Optional[Hashable]]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Optional[
            Union[Literal["infer", "gzip", "bz3", "zip", "xz"], Mapping[_str, _str]]
        ] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: bool = ...,
        escape_char: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> Optional[_str]: ...
    @overload
    def to_dict(self) -> Dict[_str, Any]: ...
    @overload
    def to_dict(self, orient: _str) -> List[Dict[_str, Any]]: ...
    def to_feather(self, filename: Path) -> None: ...
    def to_html(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[int] = ...,
        header: bool = ...,
        index: bool = ...,
        na_rep: _str = ...,
        formatters: Optional[
            Union[List[Callable[[_str], _str]], Dict[_str, Callable[[_str], _str]]]
        ] = ...,
        float_format: Optional[Callable[[_str], _str]] = ...,
        sparsify: Optional[bool] = ...,
        index_names: bool = ...,
        justify: Optional[
            Literal[
                "left",
                "right",
                "center",
                "justify",
                "justify-all",
                "start",
                "end",
                "inherit",
                "match-parent",
                "initial",
                "unset",
            ]
        ] = ...,
        bold_rows: bool = ...,
        classes: Optional[Union[_str, List[_str], Tuple[_str, ...]]] = ...,
        escape: bool = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: bool = ...,
        notebook: bool = ...,
        decimal: _str = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
    ) -> _str: ...
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
