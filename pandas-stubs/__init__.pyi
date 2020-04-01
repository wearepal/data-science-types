"""Pandas public API"""
from typing import Tuple, List, Union, IO, Optional, Any, overload, Callable, Dict, Sequence
from typing_extensions import Literal
from pathlib import Path
import numpy as _np
from . import testing
from .core.frame import DataFrame as DataFrame
from .core.frame import _AxisType
from .core.series import Series as Series
from .core.indexes import Index as Index, MultiIndex as MultiIndex

def concat(
    dataframes: List[DataFrame],
    axis: _AxisType = ...,
    sort: Optional[bool] = ...,
    ignore_index: bool = ...,
) -> DataFrame: ...
def cut(arr: _np.ndarray, bins: int) -> Tuple[Union[Series, _np.ndarray], _np.ndarray]: ...
def get_dummies(df: Union[DataFrame, Series]) -> DataFrame: ...
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
    filepath_or_buffer: Union[str, Path],
    sep: str = ...,
    header: Optional[int] = ...,
    index_col: Optional[Union[str, int, List[str], Tuple[str, ...], Sequence[int], bool]] = ...,
    delim_whitespace: bool = ...,
    names: Optional[List[str]] = ...,
    dtype: Optional[Any] = ...,
    usecols: Optional[Union[List, Callable]] = ...,
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
def unique(values: Series) -> _np.ndarray: ...
