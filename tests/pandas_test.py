from typing import TypeVar, Type, Tuple, Any, Optional, Hashable

import pandas as pd
import numpy as np

T = TypeVar("T", pd.DataFrame, pd.Series)


def assert_type(v: T, t: Type[T]) -> None:
    assert isinstance(v, t)


a: pd.DataFrame = pd.DataFrame([[1, 2, 3], [1, 2, 3]], columns=["a", "b", "c"])
df: pd.DataFrame = pd.DataFrame(
    [[1.0, 2.0], [4.0, 5.0], [7.0, 8.0]],
    index=["cobra", "viper", "sidewinder"],
    columns=["max_speed", "shield"],
)
fd: pd.DataFrame = pd.DataFrame(
    [[1.0, 2.0], [4.0, 5.0], [7.0, 8.0]], columns=["max_speed", "shield"]
)
s: "pd.Series[float]" = df["shield"].copy()
iris = pd.DataFrame(
    {
        "sepal_length": [5.1, 4.9, 4.7, 7.0, 6.4, 6.9, 6.3, 5.8, 7.1],
        "sepal_width": [3.5, 3.0, 3.2, 3.2, 3.2, 3.1, 3.3, 2.7, 3.0],
        "petal_length": [1.4, 1.4, 1.3, 4.7, 4.5, 4.9, 6.0, 5.1, 5.9],
        "petal_width": [0.2, 0.2, 0.2, 1.4, 1.5, 1.5, 2.5, 1.9, 2.1],
        "species": [
            "setosa",
            "setosa",
            "setosa",
            "versicolor",
            "versicolor",
            "versicolor",
            "virginica",
            "virginica",
            "virginica",
        ],
    }
)


def test_getitem() -> None:
    b: pd.Series = a["a"]
    c: pd.DataFrame = a[["a", "b"]]
    d: pd.DataFrame = a[np.array(["a", "b"])]
    e: pd.DataFrame = a[pd.Series(["a", "b"])]
    f: pd.DataFrame = a[pd.Index(["a", "b"])]


def test_frame_loc() -> None:
    b: pd.DataFrame = df.loc[s > 6]
    c: float = df.loc["cobra", "shield"]
    d: pd.DataFrame = df.loc[df["shield"] > 6, ["max_speed"]]
    e: pd.DataFrame = df.loc[["cobra", "viper"]]
    assert_type(e, pd.DataFrame)
    df.loc[["viper", "sidewinder"], ["shield"]] = 50.0
    df.loc["cobra"] = 10.0
    df.loc[["cobra", "viper"]] = df

    fd.loc[[0, 1], "shield"] = 4.0


def test_series_loc() -> None:
    b: float = s.loc["cobra"]
    c: pd.Series = s.loc[s > 6]
    s.loc["cobra"] = 3.0
    s.loc[["cobra", "viper"]] = 3.0


# this test doesn't work on python 3.6 somehow

# def test_indexing_with_df() -> None:
#     b: pd.DataFrame = df[s.to_frame().isin([df])]
#     assert_type(b, pd.DataFrame)


def test_frame_iloc() -> None:
    b: pd.Series = df.iloc[0]
    c: float = df.iloc[0, 0]
    d: pd.DataFrame = df.iloc[[0, 0]]
    e: pd.DataFrame = df.iloc[:2]
    f: pd.DataFrame = df.iloc[[0, 1], [0, 1]]
    g: pd.DataFrame = df.iloc[1:3, 0:3]
    h: pd.Series = df.iloc[:, 1]
    i: pd.Series = df.iloc[1, :]
    assert_type(i, pd.Series)
    df.iloc[0] = s
    df.iloc[0, 0] = 3.0
    df.iloc[[0, 0]] = df
    df.iloc[:2] = df
    df.iloc[[0, 1], [0, 1]] = df
    df.iloc[1:3, 0:3] = df
    df.iloc[:, 1] = s
    df.iloc[1, :] = s


def test_series_iloc() -> None:
    b: float = s.iloc[0]
    c: pd.Series[float] = s.iloc[[0, 1]]
    d: pd.Series[float] = s.iloc[:2]


def test_index() -> None:
    index: pd.Index = pd.Index([1, 2, 3], name="my_index", copy=False, tupleize_cols=False)


def test_multiindex() -> None:
    tuples = [("bar", "one"), ("bar", "two"), ("baz", "one")]
    index: pd.MultiIndex = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])


def test_iris() -> None:
    sepal_length = iris.groupby("species")["sepal_length"]
    arr: np.ndarray = sepal_length.unique()[0]
    assert isinstance(arr, np.ndarray)
    d: pd.DataFrame = iris.groupby("species", as_index=False).max()
    assert_type(d, pd.DataFrame)
    e: pd.DataFrame = iris.groupby(
        {"sepal_length": "length", "petal_length": "length"}, axis=1
    ).agg(lambda x: x.mean(axis="columns"))
    assert_type(e, pd.DataFrame)
    f: pd.Series = e["length"]
    assert_type(f, pd.Series)


def test_rename() -> None:
    df: Optional[pd.DataFrame]
    df = a.rename(columns={"a": "a_renamed"}, inplace=False)
    df.columns  # b is not None


def test_itertuples() -> None:
    for_variable: Tuple[Any, ...]
    for for_variable in a.itertuples(name=None):
        pass


def test_iterrows() -> None:
    for_variable: Tuple[Optional[Hashable], pd.Series]
    for for_variable in a.iterrows():
        pass


def test_frame_sort_values() -> None:
    a.sort_values(by="a")
    a.sort_values(by="a", inplace=True)


def test_int_indices() -> None:
    df = pd.DataFrame([["a"]])
    assert "a" == df.at[0, 0]
