from pathlib import Path
from typing import Union, Sequence, Tuple, List, Optional, overload, TypeVar, Type, Any
from typing_extensions import Literal

import numpy as _np

from .artist import Artist, Line2D, LineCollection, Rectangle
from .axes import Axes as Axes, _LegendLocation
from .legend import Legend
from .image import AxesImage
from .text import Text

_Float = TypeVar("_Float", _np.float32, _np.float64)
_Data = Union[float, _np.ndarray[_Float], Sequence[float]]

class Figure:
    def savefig(
        self,
        fname: Path,
        dpi: int = ...,
        bbox_extra_artists: Sequence[Artist] = ...,
        bbox_inches: Optional[Literal["tight"]] = ...,
    ) -> None: ...
    def tight_layout(
        self, pad: Optional[float] = ..., h_pad: Optional[float] = ..., w_pad: Optional[float] = ...
    ) -> None: ...

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
@overload
def figure(
    num: Optional[Union[int, str]] = ...,
    figsize: Optional[List[float, float]] = ...,
    dpi: Optional[int] = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    frameon: Optional[bool] = ...,
    FigureClass: Type[Figure] = ...,
    clear: Optional[bool] = ...,
    **kwargs: Optional[Any]) -> Figure:
@overload
def subplots_adjust(
    left: Optional[float] = ...,
    bottom: Optional[float] = ...,
    right: Optional[float] = ...,
    top: Optional[float] = ...,
    wspace: Optional[float] = ...,
    hspace: Optional[float] = ...
) -> None:
def close(fig: Union[Figure, Literal["all"]]) -> None: ...
def clf() -> None: ...
def show() -> None: ...
