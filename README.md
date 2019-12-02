# Python type stubs for machine learning

This is a [PEP-561][pep-561]-compliant stub-only package
which provides type information for [matplotlib][matplotlib], [numpy][numpy] and [pandas][pandas].
The [mypy][mypy] type checker can [recognize][mypy-docs] the types in these packages by installing this package:

```bash
pip install git+https://github.com/predictive-analytics-lab/machine-learning-types@v0.1.3
```

There is also minor support for Tensorflow and Tensorflow Probability.

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
