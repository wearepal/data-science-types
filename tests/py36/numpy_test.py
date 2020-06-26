"""Tests for numpy"""

from typing import List, Sequence, TypeVar, Type

import numpy as np

DType = TypeVar(
    "DType", np.bool_, np.float32, np.float64, np.int8, np.int16, np.int32, np.int64, np.str_
)


def assert_dtype(array: np.ndarray["DType"], dtype: "Type[DType]") -> None:
    assert array.dtype.type is dtype


# these variables are available to all other functions
a: np.ndarray["np.float64"] = np.array([3.0, 2.0])
a = a.astype(dtype=float)
b: np.ndarray["np.bool_"] = a == a
c: np.ndarray["np.int64"] = np.array([[2, 3], [3, 4]])
d: np.ndarray["np.int32"] = np.array([[1, -2], [3, 5]], dtype=np.int32)
e: np.ndarray["np.float32"] = a.astype(np.float32)


def test_mean_std() -> None:
    f: np.ndarray["np.float32"] = np.std(e, axis=0, keepdims=True)
    g: np.ndarray["np.float64"] = np.std(c, axis=0, keepdims=True)
    h1: np.float64 = np.mean(c)
    i1: float = np.mean(c)
    j1: np.float32 = np.mean(e)
    k1: float = np.mean(e)
    l1: np.float64 = np.mean(b)
    # member method
    h2: np.float64 = c.mean()
    i2: float = c.mean()
    j2: np.float32 = e.mean()
    k2: float = e.mean()
    l2: np.float64 = b.mean()


def test_random_choice() -> None:
    f: int = np.random.choice(7)
    g: np.ndarray["np.int64"] = np.random.choice(7, size=1)
    h: np.ndarray["np.int64"] = np.random.choice(range(7), size=1)
    i: np.ndarray["np.int16"] = np.random.choice(np.array([3, 7], dtype=np.int16), size=3)
    assert_dtype(i, np.int16)


def test_non_numeric() -> None:
    f: np.ndarray["np.str_"] = np.array(["hello", "world"])
    g: np.ndarray["np.bool_"] = np.array([True, False, True])


def test_division() -> None:
    f1: np.ndarray["np.float64"] = d / c
    g1: np.ndarray["np.float32"] = e / e
    h1: np.ndarray["np.float64"] = e / c

    f2: np.ndarray["np.float64"] = np.divide(d, c)
    g2: np.ndarray["np.float32"] = np.divide(e, e)
    h2: np.ndarray["np.float64"] = np.divide(e, c)
    i2: np.float64 = np.divide(60, 5)
    j2: np.ndarray["np.float64"] = np.divide((60, 5, 6), 5)
    k2: np.ndarray["np.float64"] = np.divide(c, 5)


def test_astype() -> None:
    f1: np.ndarray["np.float64"] = e.astype(float)
    g1: np.ndarray["np.float64"] = e.astype(np.float64)
    h1: np.ndarray["np.bool_"] = c.astype(bool)
    i1: np.ndarray["np.int64"] = d.astype(int)
    j1: np.ndarray["np.int64"] = d.astype(np.int64)
    k1: np.ndarray["np.int32"] = e.astype(np.int32)
    l1: np.ndarray["np.str_"] = c.astype(str)

    f2: np.ndarray["np.float64"] = np.asarray(e, float)
    g2: np.ndarray["np.float64"] = np.asarray(e, np.float64)
    h2: np.ndarray["np.bool_"] = np.asarray(c, bool)
    i2: np.ndarray["np.int64"] = np.asarray(d, int)
    j2: np.ndarray["np.int64"] = np.asarray(d, np.int64)
    k2: np.ndarray["np.int32"] = np.asarray(e, np.int32)
    l2: np.ndarray["np.str_"] = np.asarray(c, str)


def test_tolist() -> None:
    # tolist() actually returns a list, but we have to type it as Sequence because they're covariant
    f: Sequence["int"] = c.tolist()
    g: Sequence["float"] = e.tolist()


def test_reducing_funcs() -> None:
    """The behavior of these functions depends on whether an axis is specified"""
    sum1: np.int32 = np.sum(d)
    sum2: np.int32 = np.sum(d, axis=None)
    sum3: np.ndarray["np.int32"] = np.sum(d, axis=0)

    max1: np.int32 = np.max(d)
    max2: np.int32 = np.max(d, axis=None)
    max3: np.ndarray["np.int32"] = np.max(d, axis=0)

    min1: np.int32 = np.min(d)
    min2: np.int32 = np.min(d, axis=None)
    min3: np.ndarray["np.int32"] = np.min(d, axis=0)

    prod1: np.int32 = np.prod(d)
    prod2: np.int32 = np.prod(d, axis=None)
    prod3: np.ndarray["np.int32"] = np.prod(d, axis=0)


def test_repeat() -> None:
    f: np.ndarray["np.int16"] = np.repeat(np.int16(5), 3)
    g: np.ndarray["np.int64"] = np.repeat(5, 3)


def test_concatenate() -> None:
    d2: np.ndarray["np.int32"] = np.concatenate([d, d], axis=1)
    d3: np.ndarray["np.int32"] = np.concatenate((d, d), axis=0)
    scalar: np.float32 = np.float32(3.0)
    assert isinstance(scalar, np.float32)


def test_at_least_2d() -> None:
    arr: np.ndarray["np.float64"] = np.atleast_2d(3.0)
    assert isinstance(arr, np.ndarray)
    assert_dtype(arr, np.float64)

    a: List[np.ndarray["np.int64"]] = np.atleast_2d(1, [1, 2], [[1, 2]], 1)
    assert isinstance(a, list)


def test_where() -> None:
    f: np.ndarray["np.int64"] = np.where(c == 2, c, d)
    g: np.ndarray["np.int64"] = np.where(True, c, d)
    h1: np.ndarray["np.int64"] = np.where(True, 2, 3)
    h2: np.ndarray["np.float64"] = np.where(True, 2.0, 3)
    i: np.ndarray["np.int64"] = np.where(c == 2, c, 3)
    j: np.ndarray["np.int32"] = np.where(c == 2, 2, d)
