from __future__ import annotations

import pandas as pd
import numpy as np

a: pd.DataFrame = pd.DataFrame([[1, 2, 3], [1, 2, 3]], columns=["a", "b", "c"])
df: pd.DataFrame = pd.DataFrame(
    [[1.0, 2.0], [4.0, 5.0], [7.0, 8.0]],
    index=["cobra", "viper", "sidewinder"],
    columns=["max_speed", "shield"],
)
s: pd.Series[float] = df["shield"].copy()


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
    df.loc[["viper", "sidewinder"], ["shield"]] = 50.0
    df.loc["cobra"] = 10.0


def test_series_loc() -> None:
    b: float = s.loc["cobra"]
    c: pd.Series = s.loc[s > 6]
    s.loc["cobra"] = 3.0
    s.loc[["cobra", "viper"]] = 3.0


def test_indexing_with_df() -> None:
    b: pd.DataFrame = df[s.to_frame().isin([df])]


def test_frame_iloc() -> None:
    b: pd.Series = df.iloc[0]
    c: float = df.iloc[0, 0]
    d: pd.DataFrame = df.iloc[[0, 0]]
    e: pd.DataFrame = df.iloc[:2]
    f: pd.DataFrame = df.iloc[[0, 1], [0, 1]]
    g: pd.DataFrame = df.iloc[1:3, 0:3]
    h: pd.Series = df.iloc[:, 1]
    i: pd.Series = df.iloc[1, :]
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
