"""Pandas public API"""
from typing import (
    Tuple,
    List,
    Union,
    IO,
    Optional,
    Any,
    overload,
    Callable,
    Dict,
    Sequence,
    Type,
    Mapping,
)
from typing_extensions import Literal
from pathlib import Path
import numpy as _np
from . import testing
from .core.frame import DataFrame as DataFrame, _ListLike
from .core.frame import _AxisType
from .core.series import Series as Series
from .core.indexes import Index as Index, MultiIndex as MultiIndex

def concat(
    dataframes: Union[Sequence[DataFrame], Mapping[str, DataFrame]],
    axis: _AxisType = ...,
    sort: Optional[bool] = ...,
    ignore_index: bool = ...,
) -> DataFrame: ...
def cut(arr: _np.ndarray, bins: int) -> Tuple[Union[Series, _np.ndarray], _np.ndarray]: ...
def get_dummies(df: Union[DataFrame, Series], columns: Optional[_ListLike] = ...) -> DataFrame: ...
def isnull(df: Union[DataFrame, Series]) -> _np.ndarray: ...
@overload
def merge(left: DataFrame, right: DataFrame, on: str = ...) -> DataFrame: ...
@overload
def merge(
    left: DataFrame, right: DataFrame, left_on: str, right_on: str, how: str
) -> DataFrame: ...
@overload
def merge(
    left: DataFrame, right: DataFrame, left_on: List[str], right_on: List[str], how: str
) -> DataFrame: ...
def read_csv(
    filepath_or_buffer: Union[str, Path, IO],
    sep: str = ...,
    delimiter: Optional[str] = ...,  # only an alias to sep
    header: Optional[Union[int, List[int], Literal["infer"]]] = ...,
    names: Optional[List[str]] = ...,
    index_col: Optional[Union[str, int, List[str], Tuple[str, ...], Sequence[int], bool]] = ...,
    usecols: Optional[Union[List[str], List[int], Callable]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[Type, str, Mapping[str, Union[str, Type]]]] = ...,
    engine: Optional[Union[Literal["c"], Literal["python"]]] = ...,
    converters: Dict[Union[str, int], Callable] = ...,
    true_values: Optional[List] = ...,
    false_values: Optional[List] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[int, _ListLike, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values: Optional[Union[str, List[str]]] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_line: bool = ...,
    parse_dates: Union[bool, List[int], List[str], List[List[int]], Dict[str, List[int]]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz3", "zip", "xz"]] = ...,
    thousands: Optional[str] = ...,
    decimal: Optional[str] = ...,
    lineterminator: Optional[str] = ...,
    quotechar: Optional[str] = ...,
    quoting: Optional[Literal[0, 1, 2, 3]] = ...,
    doublequote: bool = ...,
    escapechar: Optional[str] = ...,
    comment: Optional[str] = ...,
    encoding: Optional[str] = ...,
    dialect: Any = ...,  # TODO str or csv.Dialect Optional
    error_bad_lines: bool = ...,
    warn_bad_lines: bool = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
) -> DataFrame: ...
def read_sql(
    sql: Union[str, Any],
    con: Union[str, Any] = ...,
    index_col: Optional[Union[str, List[str]]] = ...,
    coerce_float: bool = ...,
    params: Optional[Union[List[str], Tuple[str, ...], Dict[str, str]]] = ...,
    parse_dates: Optional[Union[List[str], Dict[str, str], Dict[str, Dict[str, Any]]]] = ...,
    columns: List[str] = ...,
    chunksize: int = ...,
) -> DataFrame: ...
def read_feather(p: Union[Path, IO]) -> DataFrame: ...
def read_json(
    path_or_buf: str = ...,
    orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
    typ: Literal["frame", "series"] = ...,
    dtype: Optional[Union[bool, Dict[str, str]]] = ...,
    convert_axes: Optional[bool] = ...,
    convert_dates: Optional[Union[bool, List[str]]] = ...,
    keep_default_dates: Optional[bool] = ...,
    numpy: Optional[bool] = ...,
    precise_float: Optional[bool] = ...,
    date_unit: Optional[str] = ...,
    encoding: str = ...,
    lines: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz3", "zip", "xz"]] = ...,
    nrows: Optional[int] = ...,
) -> Union[DataFrame, Series]: ...
def to_numeric(
    arg: Union[int, float, List, Tuple, _np.ndarray, Series],
    errors: Literal["ignore", "raise", "coerce"] = ...,
    downcast: Literal["integer", "signed", "unsigned", "float"] = ...,
) -> Union[Series, _np.ndarray]: ...
def unique(values: Series) -> _np.ndarray: ...
