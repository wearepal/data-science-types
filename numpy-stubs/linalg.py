from typing import Tuple

from numpy import ndarray, _Int, float64, _DType


def slogdet(x: ndarray[_DType]) -> Tuple[_Int, ndarray[float64]]:
    ...
