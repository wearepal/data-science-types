# Mypy type stubs for NumPy, pandas, and Matplotlib

[![Join the chat at https://gitter.im/data-science-types/community](https://badges.gitter.im/data-science-types/community.svg)](https://gitter.im/data-science-types/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is a [PEP-561][pep-561]-compliant stub-only package
which provides type information for [matplotlib][matplotlib], [numpy][numpy] and [pandas][pandas].
The [mypy][mypy] type checker (or pytype or PyCharm) can [recognize][mypy-docs] the types in these packages by installing this package.

### NOTE: This is a work in progress

Many functions are already typed, but a *lot* is still missing (NumPy and pandas are *huge* libraries).
Chances are, you will see a message from Mypy claiming that a function does not exist when it does exist.
If you encounter missing functions, we would be delighted for you to send a PR.
If you are unsure of how to type a function, we can discuss it.

## Installing

You can get this package from PyPI:

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

```bash
pip install -e '.[dev]'
```

This will also install NumPy, pandas, and Matplotlib to be able to run the tests.

### Running CI locally (recommended)

We include a script for running the CI checks that are triggered when a PR is opened.
To test these out locally, you need to install the type stubs in your environment.
Typically, you would do this with

```bash
pip install -e .
```

Then use the `check_all.sh` script to run all tests:

```bash
./check_all.sh
```

Below we describe how to run the various checks individually,
but `check_all.sh` should be easier to use.

### Checking compliance with Mypy

The settings for Mypy are specified in the `mypy.ini` file in the repository.
Just running

```bash
mypy tests
```

from the base directory should take these settings into account.
We enforce 0 Mypy errors.

### Formatting with black

We use [Black][black] to format the stub files.
First, install `black` and then run

```bash
black .
```
from the base directory.

### Pytest

```bash
python -m pytest -vv tests/
```

### Flake8

```bash
flake8 *-stubs
```

## License

[Apache 2.0](LICENSE)


[pep-561]: https://www.python.org/dev/peps/pep-0561/
[matplotlib]: https://matplotlib.org
[numpy]: https://numpy.org
[pandas]: https://pandas.pydata.org
[mypy]: http://www.mypy-lang.org/
[mypy-docs]: https://mypy.readthedocs.io/en/latest/installed_packages.html
[black]: https://github.com/psf/black
