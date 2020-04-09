from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union, overload

import numpy as _np
from typing_extensions import Literal

from .artist import Artist, Line2D, LineCollection, Rectangle
from .axes import Axes as Axes
from .axes import SubplotBase, _LegendLocation
from .collections import PolyCollection
from .image import AxesImage
from .legend import Legend
from .text import Text

_Float = TypeVar("_Float", _np.float32, _np.float64)
_Data = Union[float, _np.ndarray[_Float], Sequence[float]]

class Figure:
    def savefig(
        self,
        fname: Union[str, Path],
        dpi: int = ...,
        bbox_extra_artists: Sequence[Artist] = ...,
        bbox_inches: Optional[Literal["tight"]] = ...,
    ) -> None: ...
    def tight_layout(
        self, pad: Optional[float] = ..., h_pad: Optional[float] = ..., w_pad: Optional[float] = ...
    ) -> None: ...
    def suptitle(
        self,
        t: str,
        x: float = ...,
        y: float = ...,
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
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, Axes]: ...
@overload
def subplots(
    nrows: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    *,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    nrows: int,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
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
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
def figure(
    num: Optional[Union[int, str]] = ...,
    figsize: Optional[Tuple[float, float]] = ...,
    dpi: Optional[int] = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    frameon: bool = ...,
    FigureClass: Type[Figure] = ...,
    clear: bool = ...,
) -> Figure: ...
def subplots_adjust(
    left: Optional[float] = ...,
    bottom: Optional[float] = ...,
    right: Optional[float] = ...,
    top: Optional[float] = ...,
    wspace: Optional[float] = ...,
    hspace: Optional[float] = ...,
) -> None: ...
def close(fig: Union[Figure, Literal["all"]]) -> None: ...
def clf() -> None: ...
def plot(*args: Any, scalex: bool = ..., scaley: bool = ..., data: Optional[_Data] = ..., **kwargs: Any) -> Line2D:
def show() -> None: ...
def xlim(*args: Any, **kwargs: Any) -> Tuple[float, float]: ...
def ylim(*args: Any, **kwargs: Any) -> Tuple[float, float]: ...
def xticks(
    ticks: Optional[List[float]] = ..., labels: Optional[List[str]] = ..., **kwargs
) -> Tuple[List[float], List[str]]: ...
def yticks(
    ticks: Optional[List[float]] = ..., labels: Optional[List[str]] = ..., **kwargs
) -> Tuple[List[float], List[str]]: ...
def xlabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
    **kwargs: Any,
) -> str: ...
def ylabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
    **kwargs: Any,
) -> str: ...
def fill_between(
    x: Union[list, _np.ndarray],
    y1: Union[list, _np.ndarray],
    y2: Optional[Union[list, _np.ndarray]] = ...,
    where: Optional[List[bool]] = ...,
    interpolate: bool = ...,
    step: Optional[Literal["pre", "post", "mid"]] = ...,
    *,
    data: Optional[_Data] = ...,
    **kwargs: Any,
) -> PolyCollection: ...
def axhline(y: Optional[float] = ..., xmin: Optional[float] = ..., xmax: Optional[float] = ...) -> Line2d: ...
def axvline(x: Optional[float] = ..., ymin: Optional[float] = ..., ymax: Optional[float] = ...) -> Line2d: ...
