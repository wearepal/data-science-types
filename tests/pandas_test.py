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

    max_speed = df.loc[:, "max_speed"]
    shield = df.loc[:, ["shield"]]


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


def test_isna() -> None:
    b1: bool = pd.isna("dog")
    b3: bool = pd.isna(np.nan)
    array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    bool_array: np.ndarray[np.bool_] = pd.isna(array)


def test_isnull() -> None:
    b1: bool = pd.isnull("dog")
    b3: bool = pd.isnull(np.nan)
    array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    bool_array: np.ndarray[np.bool_] = pd.isnull(array)
    b4: bool = pd.isnull(None)
    b5: bool = pd.isnull(float("nan"))
    df1: pd.DataFrame = pd.isnull(pd.DataFrame([]))
    s1: pd.Series = pd.isnull(pd.Series([]))


def test_dataframe_isna_isnull() -> None:
    df1: pd.DataFrame = pd.isna(df)
    df2: pd.DataFrame = df.isna()
    df3: pd.DataFrame = pd.isnull(df)
    df4: pd.DataFrame = df.isnull()


def test_series_isna_isnull() -> None:
    df1: pd.Series[bool] = pd.isna(s)
    df2: pd.Series[bool] = s.isna()
    df3: pd.Series[bool] = pd.isnull(s)
    df4: pd.Series[bool] = s.isnull()


def test_index_isna_isnull() -> None:
    df1: np.ndarray[np.bool_] = pd.isna(df.index)
    df2: np.ndarray[np.bool_] = df.index.isna()
    df3: np.ndarray[np.bool_] = pd.isnull(df.index)
    df4: np.ndarray[np.bool_] = df.index.isnull()


def test_frame_sort_values() -> None:
    a.sort_values(by="a")
    a.sort_values(by="a", inplace=True)


def test_int_indices() -> None:
    df = pd.DataFrame([["a"]])
    assert df.at[0, 0] == "a"


def test_intdtypes() -> None:
    pd.Int8Dtype()
    pd.Int16Dtype()
    pd.Int32Dtype()
    pd.Int64Dtype()
    pd.UInt8Dtype()
    pd.UInt16Dtype()
    pd.UInt32Dtype()
    pd.UInt64Dtype()


def test_frame_drop() -> None:
    df = pd.DataFrame([["1", 2], ["3", 4]], columns=["a", "b"], index=["1", "3"])
    df.drop(["1"], inplace=False)
    df.drop("1", inplace=False)
    df.drop(["b"], axis=1, inplace=False)
    df.drop("b", axis=1, inplace=False)
    df.drop("1")


def test_frame_rank() -> None:
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df.rank(method="min")
    df.rank(method="dense", axis=1)
    df.rank(method="max", numeric_only=False)
    df.rank(method="first", na_option="keep")
    df.rank(method="first", ascending=False)
    df.rank(method="first", pct=False)
    df.rank(1, "dense", True, "top", True, True)


def test_frame_filter() -> None:
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df.filter(["a"])
    df.filter(like="a")
    df.filter(regex="a")
    df.filter(["b"], axis=0)
    df.filter(like="b", axis=0)
    df.filter(regex="b", axis=0)


def test_frame_apply() -> None:
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df.apply(lambda row: row["a"] * 2, axis=1).values


def test_frame_merge() -> None:
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a", "c"])
    df.merge(df2, on="a")

    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a", "c"])
    df.merge(df2, on="a", how="inner")

    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a", "c"])
    df.merge(df2, on="a", how="inner", suffixes=["", "_right"])

    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a1", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a2", "c"])
    df.merge(df2, left_on="a1", right_on="a2")

    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a1", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a2", "c"])
    df.merge(df2, left_on="a1", right_on="a2", how="inner")

    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a1", "b"])
    df2 = pd.DataFrame([[1, 2], [5, 6]], columns=["a2", "c"])
    df.merge(df2, left_on="a1", right_on="a2", how="inner", suffixes=["", "_right"])


def test_frame_reindex() -> None:
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df.reindex(["a_", "b_"])


def test_frame_replace() -> None:
    df = pd.DataFrame([["1", "2"], ["3", "4"]], columns=["a", "b"])
    df.replace(r"1", 1, regex=True, inplace=True)


# Uncomment once either pyarrow or fastparquet supports Python 3.9
# def test_to_parquet_and_read_parquet(tmp_path: Path) -> None:
#     filename = str(tmp_path / "data.parq")
#     df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
#     df.to_parquet(filename, engine="auto", compression=None, index=True, partition_cols=["a"])
#     df: pd.DataFrame = pd.read_parquet(filename, engine="auto", columns=["a", "b"], use_nullable_dtypes=False)


def test_series_rank() -> None:
    s = pd.Series([0, 1])
    s.rank(method="min")
    s.rank(method="dense", axis=0)
    s.rank(method="max", numeric_only=False)
    s.rank(method="first", na_option="keep")
    s.rank(method="first", ascending=False)
    s.rank(method="first", pct=False)
    s.rank(0, "dense", True, "top", True, True)
