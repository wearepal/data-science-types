from typing import Tuple, List, Union, IO, Optional, Any, overload
from typing_extensions import Literal
from pathlib import Path
import numpy as _np

from pandas.core.frame import DataFrame

from pandas.core.series import Series

_AxisType = Literal["columns", "index"]

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
def merge(left: DataFrame, right: DataFrame, left_on: str, right_on: str, how: str) -> DataFrame: ...
@overload
def merge(left: DataFrame, right: DataFrame, left_on: List[str], right_on: List[str], how: str) -> DataFrame: ...
def read_csv(
    filepath_or_buffer: Union[str, Path],
    sep: str = ...,
    header: Optional[int] = ...,
    index_col: Optional[int] = ...,
    delim_whitespace: bool = ...,
    names: Optional[List[str]] = ...,
    dtype: Optional[Any] = ...,
) -> DataFrame: ...
def read_feather(p: Union[Path, IO]) -> DataFrame: ...
def unique(values: Series) -> _np.ndarray: ...
