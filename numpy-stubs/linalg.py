from typing import Tuple, Union

from numpy import ndarray, _Int, float64, _DType


def slogdet(
    a: ndarray[_DType],
) -> Union[Tuple[float64, float64], Tuple[ndarray[float64], ndarray[float64]]]:
    ...
