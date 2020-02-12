from typing import Sequence
import pandas as pd
import numpy as np

a: pd.DataFrame = pd.DataFrame([[1, 2, 3], [1, 2, 3]], columns=["a", "b", "c"])


def test_getitem() -> None:
    b: pd.Series = a["a"]
    c: pd.DataFrame = a[["a", "b"]]
    d: pd.DataFrame = a[("a", "b")]
    e: pd.DataFrame = a[np.array(["a", "b"])]
    f: pd.DataFrame = a[pd.Series(["a", "b"])]
    g: pd.DataFrame = a[pd.Index(["a", "b"])]
