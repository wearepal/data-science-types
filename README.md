# Python type stubs for numpy, pandas and matplotlib

This is a [PEP-561][pep-561]-compliant stub-only package
which provides type information for [matplotlib][matplotlib], [numpy][numpy] and [pandas][pandas].
The [mypy][mypy] type checker can [recognize][mypy-docs] the types in these packages by installing this package:

```bash
pip install data-science-types
```

There is also minor support for Tensorflow and Tensorflow Probability.

## Examples

These are the kinds of things that can be checked:

### Array creation

```python
import numpy as np

arr1: np.ndarray[np.int64] = np.array([3, 7, 39, -3])  # OK
arr2: np.ndarray[np.int32] = np.array([3, 7, 39, -3])  # Type error
arr3: np.ndarray[np.int32] = np.array([3, 7, 39, -3], dtype=np.int32)  # OK
arr4: np.ndarray[float] = np.array([3, 7, 39, -3], dtype=float)  # Type error: the type of ndarray can not be just "float"
arr5: np.ndarray[np.float64] = np.array([3, 7, 39, -3], dtype=float)  # OK
```

### Operations

```python
import numpy as np

arr1: np.ndarray[np.int64] = np.array([3, 7, 39, -3])
arr2: np.ndarray[np.int64] = np.array([4, 12, 9, -1])

result1: np.ndarray[np.int64] = np.divide(arr1, arr2)  # Type error
result2: np.ndarray[np.float64] = np.divide(arr1, arr2)  # OK

compare: np.ndarray[np.bool_] = (arr1 == arr2)
```

### Reductions

```python
import numpy as np

arr: np.ndarray[np.float64] = np.array([[1.3, 0.7], [-43.0, 5.6]])

sum1: int = np.sum(arr)  # Type error
sum2: np.float64 = np.sum(arr)  # OK
sum3: float = np.sum(arr)  # Also OK: np.float64 is a subclass of float
sum4: np.ndarray[np.float64] = np.sum(arr, axis=0)  # OK

# the same works with np.max, np.min and np.prod
```

## Philosophy

The goal is not to recreate the class hierarchy exactly.
The goal is to have useful checks on our code.
Often the actual API in the libraries is more permissive than the type signatures in our stubs;
but this is (usually) a feature and not a bug.

[pep-561]: https://www.python.org/dev/peps/pep-0561/
[matplotlib]: https://matplotlib.org
[numpy]: https://numpy.org
[pandas]: https://pandas.pydata.org
[mypy]: http://www.mypy-lang.org/
[mypy-docs]: https://mypy.readthedocs.io/en/latest/installed_packages.html
