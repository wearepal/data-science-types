from typing import (
    Tuple,
    List,
    Union,
    IO,
    Optional,
)
from typing_extensions import Literal
from pathlib import Path as _Path
import numpy as _np

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
def read_csv(p: _Path) -> DataFrame: ...
def read_feather(p: Union[_Path, IO]) -> DataFrame: ...
