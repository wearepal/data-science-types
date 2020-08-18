from typing import Tuple, Union, overload
from typing_extensions import Literal

from numpy import ndarray, _Int, float64, _Scalar

def slogdet(
    a: ndarray[_Scalar],
) -> Union[Tuple[float64, float64], Tuple[ndarray[float64], ndarray[float64]]]: ...
@overload
def svd(
    a: ndarray[_Scalar],
    full_matrices: bool = ...,
    compute_uv: Literal[True] = ...,
    hermitian: bool = ...,
) -> Tuple[ndarray[_Scalar], ndarray[_Scalar], ndarray[_Scalar]]: ...
@overload
def svd(
    a: ndarray[_Scalar],
    *,
    compute_uv: Literal[False],
    full_matrices: bool = ...,
    hermitian: bool = ...,
) -> ndarray[_Scalar]: ...
