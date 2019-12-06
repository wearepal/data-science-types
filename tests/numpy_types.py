"""Tests for numpy"""
from __future__ import annotations

import numpy as np

a: np.ndarray[np.float64] = np.array([3.0, 2.0])
a = a.astype(dtype=float)
b: np.ndarray[np.bool_] = a == a
c: np.ndarray[np.int64] = np.array([2, 3])

d: np.ndarray[np.float32] = np.std(a.astype(np.float32), axis=0, keepdims=True)
e: np.ndarray[np.float64] = np.std(c, axis=0, keepdims=True)

f: np.ndarray[np.int32] = np.array([2, 3], dtype=np.int32)

# ======================================= np.random.choice ========================================
g: int = np.random.choice(7)
h: np.ndarray[np.int64] = np.random.choice(7, size=1)
i: np.ndarray[np.int64] = np.random.choice(range(7), size=1)
j: np.ndarray[np.int16] = np.random.choice(np.array([3, 7], dtype=np.int16), size=3)

k: np.ndarray[np.str_] = np.array(["hello", "world"])
l: np.ndarray[np.bool_] = np.array([True, False, True])
