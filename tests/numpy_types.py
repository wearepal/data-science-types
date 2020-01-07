"""Tests for numpy"""
from __future__ import annotations

from typing import Sequence

import numpy as np

# these variables are available to all other functions
a: np.ndarray[np.float64] = np.array([3.0, 2.0])
a = a.astype(dtype=float)
b: np.ndarray[np.bool_] = a == a
c: np.ndarray[np.int64] = np.array([[2, 3], [3, 4]])
d: np.ndarray[np.int32] = np.array([[2, 3], [3, 4]], dtype=np.int32)
e: np.ndarray[np.float32] = a.astype(np.float32)


def test_mean_std() -> None:
    f: np.ndarray[np.float32] = np.std(e, axis=0, keepdims=True)
    g: np.ndarray[np.float64] = np.std(c, axis=0, keepdims=True)
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
    g: np.ndarray[np.int64] = np.random.choice(7, size=1)
    h: np.ndarray[np.int64] = np.random.choice(range(7), size=1)
    i: np.ndarray[np.int16] = np.random.choice(np.array([3, 7], dtype=np.int16), size=3)


def test_non_numeric() -> None:
    f: np.ndarray[np.str_] = np.array(["hello", "world"])
    g: np.ndarray[np.bool_] = np.array([True, False, True])


def test_division() -> None:
    f1: np.ndarray[np.float64] = d / c
    g1: np.ndarray[np.float32] = e / e
    h1: np.ndarray[np.float64] = e / c

    f2: np.ndarray[np.float64] = np.divide(d, c)
    g2: np.ndarray[np.float32] = np.divide(e, e)
    h2: np.ndarray[np.float64] = np.divide(e, c)
    i2: np.float64 = np.divide(60, 5)
    j2: np.ndarray[np.float64] = np.divide((60, 5, 6), 5)
    k2: np.ndarray[np.float64] = np.divide(c, 5)


def test_astype() -> None:
    f1: np.ndarray[np.float64] = e.astype(float)
    g1: np.ndarray[np.float64] = e.astype(np.float64)
    h1: np.ndarray[np.bool_] = c.astype(bool)
    i1: np.ndarray[np.int64] = d.astype(int)
    j1: np.ndarray[np.int64] = d.astype(np.int64)
    k1: np.ndarray[np.int32] = e.astype(np.int32)
    l1: np.ndarray[np.str_] = c.astype(str)

    f2: np.ndarray[np.float64] = np.astype(e, float)
    g2: np.ndarray[np.float64] = np.astype(e, np.float64)
    h2: np.ndarray[np.bool_] = np.astype(c, bool)
    i2: np.ndarray[np.int64] = np.astype(d, int)
    j2: np.ndarray[np.int64] = np.astype(d, np.int64)
    k2: np.ndarray[np.int32] = np.astype(e, np.int32)
    l2: np.ndarray[np.str_] = np.astype(c, str)


def test_tolist() -> None:
    # tolist() actually returns a list, but we have to type it as Sequence because they're covariant
    f: Sequence[int] = c.tolist()
    g: Sequence[float] = e.tolist()


def test_reducing_funcs() -> None:
    """The behavior of these functions depends on whether an axis is specified"""
    sum1: np.int32 = np.sum(d)
    sum2: np.int32 = np.sum(d, axis=None)
    sum3: np.ndarray[np.int32] = np.sum(d, axis=0)

    max1: np.int32 = np.max(d)
    max2: np.int32 = np.max(d, axis=None)
    max3: np.ndarray[np.int32] = np.max(d, axis=0)

    min1: np.int32 = np.min(d)
    min2: np.int32 = np.min(d, axis=None)
    min3: np.ndarray[np.int32] = np.min(d, axis=0)

    prod1: np.int32 = np.prod(d)
    prod2: np.int32 = np.prod(d, axis=None)
    prod3: np.ndarray[np.int32] = np.prod(d, axis=0)


def test_repeat() -> None:
    f: np.ndarray[np.int16] = np.repeat(np.int16(5), 3)
    g: np.ndarray[np.int64] = np.repeat(5, 3)
