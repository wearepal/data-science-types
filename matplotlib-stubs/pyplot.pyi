from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union, overload

import numpy as _np
import pandas as _pd
from typing_extensions import Literal

from .artist import Artist, Line2D, LineCollection, Rectangle
from .axes import Axes as Axes
from .axes import SubplotBase, _LegendLocation
from .collections import PolyCollection
from .image import AxesImage
from .legend import Legend
from .text import Text

_T = TypeVar("_T")
_Numeric = TypeVar("_Numeric", int, float)
_Data = Union[_Numeric, _np.ndarray[_Numeric], Sequence[_Numeric]]
_NumericArray = Union[_pd.Series[_Numeric], _np.ndarray[_Numeric], Sequence[_Numeric]]
_StrArray = Union[_pd.Series[str], _np.ndarray[_np.str_], Sequence[str]]

class Figure:
    def savefig(
        self,
        fname: Union[str, Path],
        dpi: int = ...,
        bbox_extra_artists: Sequence[Artist] = ...,
        bbox_inches: Optional[Literal["tight"]] = ...,
    ) -> None: ...
    def tight_layout(
        self,
        pad: Optional[_Numeric] = ...,
        h_pad: Optional[_Numeric] = ...,
        w_pad: Optional[_Numeric] = ...,
    ) -> None: ...
    def suptitle(
        self,
        t: str,
        x: _Numeric = ...,
        y: _Numeric = ...,
        horizontalalignment: Literal["center", "left", "right"] = ...,
        fontsize: Optional[int] = ...,
    ) -> None: ...
    def add_subplot(
        self,
        nrows: int,
        ncols: int,
        index: int,
        polar: bool = ...,
        sharex: Axes = ...,
        sharey: Axes = ...,
        label: str = ...,
    ) -> SubplotBase: ...
    def legend(self, *args: Any, **kwargs: Any) -> Legend: ...

@overload
def subplots(
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, Axes]: ...
@overload
def subplots(
    nrows: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    *,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    nrows: int,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    squeeze: Literal[False],
    sharex: bool = ...,
    sharey: bool = ...,
    dpi: int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
def figure(
    num: Optional[Union[int, str]] = ...,
    figsize: Optional[Tuple[_Numeric, _Numeric]] = ...,
    dpi: Optional[int] = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    frameon: bool = ...,
    FigureClass: Type[Figure] = ...,
    clear: bool = ...,
) -> Figure: ...
def subplots_adjust(
    left: Optional[_Numeric] = ...,
    bottom: Optional[_Numeric] = ...,
    right: Optional[_Numeric] = ...,
    top: Optional[_Numeric] = ...,
    wspace: Optional[_Numeric] = ...,
    hspace: Optional[_Numeric] = ...,
) -> None: ...
def close(fig: Union[Figure, Literal["all"]]) -> None: ...
def clf() -> None: ...
def plot(
    x: _Data,
    y: _Data,
    *,
    color: Optional[str] = ...,
    label: str = ...,
    linestyle: Literal["-", "--", "-.", ":", ""] = ...,
    marker: str = ...,
    markerfacecolor: str = ...,
    markersize: _Numeric = ...,
    scalex: bool = ...,
    scaley: bool = ...,
    zorder: _Numeric = ...,
) -> None: ...
def show() -> None: ...
def xlim(
    left: _Numeric = ...,
    right: _Numeric = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    xmin: _Numeric = ...,
    xmax: _Numeric = ...,
) -> Tuple[_Numeric, _Numeric]: ...
def ylim(
    bottom: _Numeric = ...,
    top: _Numeric = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    ymin: _Numeric = ...,
    ymax: _Numeric = ...,
) -> Tuple[_Numeric, _Numeric]: ...
def xticks(
    ticks: Optional[_NumericArray] = ...,
    labels: Optional[_StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    **kwargs: Any,
) -> Tuple[List[_Numeric], List[str]]: ...
def yticks(
    ticks: Optional[_NumericArray] = ...,
    labels: Optional[_StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    **kwargs: Any,
) -> Tuple[List[_Numeric], List[str]]: ...
def xlabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[_Numeric] = ...,
    **kwargs: Any,
) -> str: ...
def ylabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[_Numeric] = ...,
    **kwargs: Any,
) -> str: ...
def fill_between(
    x: _NumericArray,
    y1: _NumericArray,
    y2: _NumericArray = ...,
    where: Optional[List[bool]] = ...,
    interpolate: bool = ...,
    step: Optional[Literal["pre", "post", "mid"]] = ...,
    *,
    data: Optional[_Data] = ...,
    **kwargs: Any,
) -> PolyCollection: ...
def axhline(y: _Numeric = ..., xmin: _Numeric = ..., xmax: _Numeric = ...) -> Line2D: ...
def axvline(x: _Numeric = ..., ymin: _Numeric = ..., ymax: _Numeric = ...) -> Line2D: ...
