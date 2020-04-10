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
_Str = TypeVar("_Str", str, covariant=True)
_Int = TypeVar("_Int", int, covariant=True)
_Float = TypeVar("_Float", float, covariant=True)
_Bool = TypeVar("_Bool", bool, covariant=True)
_Numeric = TypeVar("_Numeric", _Int, _Float)
_Data = Union[_Numeric, _np.ndarray[_Numeric], Sequence[_Numeric]]
_ArrayLike = Union[_pd.Series[_T], _np.ndarray[_T], Sequence[_T]]

class Figure:
    def savefig(
        self,
        fname: Union[_Str, Path],
        dpi: _Int = ...,
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
        t: _Str,
        x: _Numeric = ...,
        y: _Numeric = ...,
        horizontalalignment: Literal["center", "left", "right"] = ...,
        fontsize: Optional[_Int] = ...,
    ) -> None: ...
    def add_subplot(
        self,
        nrows: _Int,
        ncols: _Int,
        index: _Int,
        polar: _Bool = ...,
        sharex: Axes = ...,
        sharey: Axes = ...,
        label: _Str = ...,
    ) -> SubplotBase: ...
    def legend(self, *args: Any, **kwargs: Any) -> Legend: ...

@overload
def subplots(
    *,
    sharex: _Bool = ...,
    sharey: _Bool = ...,
    squeeze: Literal[True] = ...,
    dpi: _Int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, Axes]: ...
@overload
def subplots(
    nrows: _Int,
    sharex: _Bool = ...,
    sharey: _Bool = ...,
    squeeze: Literal[True] = ...,
    dpi: _Int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    *,
    ncols: _Int,
    sharex: _Bool = ...,
    sharey: _Bool = ...,
    squeeze: Literal[True] = ...,
    dpi: _Int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    nrows: _Int,
    ncols: _Int,
    sharex: _Bool = ...,
    sharey: _Bool = ...,
    squeeze: Literal[True] = ...,
    dpi: _Int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
@overload
def subplots(
    nrows: _Int = ...,
    ncols: _Int = ...,
    *,
    squeeze: Literal[False],
    sharex: _Bool = ...,
    sharey: _Bool = ...,
    dpi: _Int = ...,
    figsize: Tuple[_Numeric, _Numeric] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
def figure(
    num: Optional[Union[_Int, _Str]] = ...,
    figsize: Optional[Tuple[_Numeric, _Numeric]] = ...,
    dpi: Optional[_Int] = ...,
    facecolor: Optional[_Str] = ...,
    edgecolor: Optional[_Str] = ...,
    frameon: _Bool = ...,
    FigureClass: Type[Figure] = ...,
    clear: _Bool = ...,
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
    self,
    x: _Data,
    y: _Data,
    *,
    color: Optional[_Str] = ...,
    label: _Str = ...,
    linestyle: Literal["-", "--", "-.", ":", ""] = ...,
    marker: _Str = ...,
    markerfacecolor: _Str = ...,
    markersize: _Numeric = ...,
    scalex: _Bool = ...,
    scaley: _Bool = ...,
    zorder: _Numeric = ...,
) -> None: ...
def show() -> None: ...
def xlim(
    left: _Numeric = ...,
    right: _Numeric = ...,
    emit: _Bool = ...,
    auto: Optional[_Bool] = ...,
    xmin: _Numeric = ...,
    xmax: _Numeric = ...,
) -> Tuple[_Numeric, _Numeric]: ...
def ylim(
    bottom: _Numeric = ...,
    top: _Numeric = ...,
    emit: _Bool = ...,
    auto: Optional[_Bool] = ...,
    ymin: _Numeric = ...,
    ymax: _Numeric = ...,
) -> Tuple[_Numeric, _Numeric]: ...
def xticks(
    ticks: Optional[_ArrayLike[_Numeric]] = ..., labels: Optional[_ArrayLike[_Str]] = ..., **kwargs
) -> Tuple[List[_Numeric], List[_Str]]: ...
def yticks(
    ticks: Optional[_ArrayLike[_Numeric]] = ..., labels: Optional[_ArrayLike[_Str]] = ..., **kwargs
) -> Tuple[List[_Numeric], List[_Str]]: ...
def xlabel(
    ylabel: _Str,
    fontdict: Optional[Dict[_Str, Union[_Str, _Int]]] = ...,
    labelpad: Optional[_Numeric] = ...,
    **kwargs: Any,
) -> _Str: ...
def ylabel(
    ylabel: _Str,
    fontdict: Optional[Dict[_Str, Union[_Str, _Int]]] = ...,
    labelpad: Optional[_Numeric] = ...,
    **kwargs: Any,
) -> _Str: ...
def fill_between(
    x: _ArrayLike[_Numeric],
    y1: _ArrayLike[_Numeric],
    y2: _ArrayLike[_Numeric] = ...,
    where: Optional[List[_Bool]] = ...,
    interpolate: _Bool = ...,
    step: Optional[Literal["pre", "post", "mid"]] = ...,
    *,
    data: Optional[_Data] = ...,
    **kwargs: Any,
) -> PolyCollection: ...
def axhline(y: _Numeric = ..., xmin: _Numeric = ..., xmax: _Numeric = ...) -> Line2d: ...
def axvline(x: _Numeric = ..., ymin: _Numeric = ..., ymax: _Numeric = ...) -> Line2d: ...
