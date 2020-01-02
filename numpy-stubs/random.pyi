from numpy import int8
from typing import Union, Optional, overload, List, Iterable, Callable, TypeVar, Tuple

from ._core import (
    _ShapeType,
    ndarray,
    float64,
    int64,
    _Float,
    _Num,
    _DType,
    _Int,
    _DTypeObj,
    _FloatObj,
    _IntObj,
)

_T = TypeVar("_T")
@overload
def choice(a: _IntObj) -> _IntObj: ...
@overload
def choice(a: int, size: int) -> ndarray[int64]: ...
@overload
def choice(a: _Int, size: int) -> ndarray[_Int]: ...
@overload
def choice(
    a: List[_T], p: Union[List[_FloatObj], ndarray[_Float]] = ..., replace: bool = ...
) -> _T: ...
@overload
def choice(
    a: range, size: _IntObj, replace: bool = ..., p: Union[List[_FloatObj], ndarray[_Float]] = ...
) -> ndarray[int64]: ...
@overload
def choice(
    a: range, *, replace: bool = ..., p: Union[List[_FloatObj], ndarray[_Float]] = ...
) -> int64: ...
@overload
def choice(
    a: ndarray[_DType],
    size: _IntObj,
    replace: bool = ...,
    p: Union[List[_FloatObj], ndarray[_Float]] = ...,
) -> ndarray[_DType]: ...
@overload
def choice(
    a: ndarray[_DType], *, replace: bool = ..., p: Union[List[_FloatObj], ndarray[_Float]] = ...
) -> _DType: ...
def dirichlet(alpha: ndarray[_DType], size: _IntObj = ...) -> ndarray[_DType]: ...
def geometric(p: float, size: _IntObj) -> ndarray[float64]: ...
def normal(loc: float, scale: float, size: Union[int, Tuple[int, ...]]) -> ndarray[_Float]: ...
@overload
def permutation(size: int) -> ndarray[int64]: ...
@overload
def permutation(size: Iterable[_DType]) -> ndarray[_DType]: ...
def randn(*args: int) -> ndarray[_Float]: ...
@overload
def randint(low: int, high: int = ...) -> int64: ...
@overload
def randint(low: int, size: int, high: int = ...) -> ndarray[int64]: ...
def seed(s: int) -> None: ...
def shuffle(x: ndarray) -> None: ...
@overload
def uniform() -> float64: ...
@overload
def uniform(size: _ShapeType) -> ndarray: ...
@overload
def uniform(low: float, high: float, size: _ShapeType) -> ndarray: ...

class RandomState:
    def __init__(self, seed: int = ...): ...
    def multivariate_normal(
        self, mean: ndarray[_Num] = ..., cov: ndarray[_Num] = ..., size: Optional[_ShapeType] = ...
    ) -> ndarray[_Num]: ...
    def normal(
        self,
        loc: Union[float, ndarray[_Num]] = ...,
        scale: Union[float, ndarray[_Num]] = ...,
        size: Optional[_ShapeType] = ...,
    ) -> ndarray[_Num]: ...
    def permutation(self, size: int) -> ndarray[int64]: ...
    def shuffle(self, x: ndarray) -> None: ...
    def uniform(self, size: _ShapeType) -> ndarray: ...
