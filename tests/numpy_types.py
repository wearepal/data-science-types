"""Tests for numpy"""
import numpy as np

a: np.ndarray[np.float64] = np.array([3.0, 2.0])
b: np.ndarray[np.bool_] = a == a
c: np.ndarray[np.int64] = np.array([2, 3])

d: np.ndarray[np.float32] = np.std(a.astype(np.float32), axis=0, keepdims=True)
e: np.ndarray[np.float64] = np.std(c, axis=0, keepdims=True)
