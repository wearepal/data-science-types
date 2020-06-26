# Mypy type stubs for numpy, pandas and matplotlib

This is a [PEP-561][pep-561]-compliant stub-only package
which provides type information for [matplotlib][matplotlib], [numpy][numpy] and [pandas][pandas].
The [mypy][mypy] type checker (or pytype or PyCharm) can [recognize][mypy-docs] the types in these packages by installing this package.

### NOTE: This is a work in progress

Lots of functions are already typed, but a *lot* is still missing (numpy and pandas are *huge* libraries).
Chances are you will see a message from Mypy claiming that a function does not exist when it actually does exist.
If you encounter missing functions, we would be very happy for you to send a PR.
If you are unsure of how to type a function, we can discuss it.

## Installing

You can get this package from PyPi:

```bash
pip install data-science-types
```

To get the most up-to-date version, install it directly from GitHub:

```bash
pip install git+https://github.com/predictive-analytics-lab/data-science-types
```

Or clone the repository somewhere and do `pip install -e .`.

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

The goal is not to recreate the APIs exactly.
The main goal is to have *useful* checks on our code.
Often the actual APIs in the libraries is more permissive than the type signatures in our stubs;
but this is (usually) a feature and not a bug.

## Contributing

We always welcome contributions.
All pull requests are subject to CI checks.
We check for compliance with Mypy and that the file formatting conforms to our Black specification.

You can install these dev dependencies via
```
pip install -e .[dev]
```

### Checking compliance with Mypy
The settings for Mypy are specified in the `mypy.ini` file in the repository.
Just running
```
mypy tests
```
from the base directory should take these settings into account.
We enforce 0 mypy errors.

### Formatting with black
We use [Black][black] to format the stub files.
First install `black` and then run

```
black -l 100 -t py36 -S .
```

from the base directory.

## License

[GPL 3](LICENSE)


[pep-561]: https://www.python.org/dev/peps/pep-0561/
[matplotlib]: https://matplotlib.org
[numpy]: https://numpy.org
[pandas]: https://pandas.pydata.org
[mypy]: http://www.mypy-lang.org/
[mypy-docs]: https://mypy.readthedocs.io/en/latest/installed_packages.html
[black]: https://github.com/psf/black
