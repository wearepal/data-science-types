from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import numpy as _np
import pandas as _pd
from typing_extensions import Literal

from .artist import Artist, Line2D, LineCollection, Rectangle
from .axes import Axes as Axes
from .axes import SubplotBase, _LegendLocation
from .backend_bases import MouseEvent
from .collections import PolyCollection
from .font_manager import FontProperties
from .image import AxesImage
from .legend import Legend
from .patheffects import AbstractPathEffect
from .text import Text
from .transforms import Bbox, Transform

_T = TypeVar("_T")
_Data = Union[
    float,  # represents both int and float
    _np.ndarray[_np.int8],
    _np.ndarray[_np.int16],
    _np.ndarray[_np.int32],
    _np.ndarray[_np.int64],
    _np.ndarray[_np.float32],
    _np.ndarray[_np.float64],
    Sequence[int],
    Sequence[float],
]
_NumericArray = Union[
    _pd.Series[int],
    _pd.Series[float],
    _np.ndarray[_np.int8],
    _np.ndarray[_np.int16],
    _np.ndarray[_np.int32],
    _np.ndarray[_np.int64],
    _np.ndarray[_np.float32],
    _np.ndarray[_np.float64],
    Sequence[int],
    Sequence[float],
]
_StrArray = Union[_pd.Series[str], _np.ndarray[_np.str_], Sequence[str]]

# # ===  Line2D kwargs ===
# agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
# alpha: Optional[float] = ...,
# animated: Optional[bool] = ...,
# antialiased: Optional[bool] = ...,
# clip_box: Optional[Bbox] = ...,
# clip_on: Optional[bool] = ...,
# clip_path: Optional[Callable[[Path, Transform], None]] = ...,
# color: Optional[str] = ...,
# contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
# dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
# dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
# dashes: Optional[[Sequence[float], Tuple[None, None]]] = ...,
# drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
# figure: Optional[Figure] = ...,
# fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
# gid: Optional[str] = ...,
# in_layout: Optional[bool] = ...,
# label: object = ...,
# linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
# linewidth: Optional[float] = ...,
# marker: Optional[str] = ...,
# markeredgecolor: Optional[str] = ...,
# markerfacecolor: Optional[str] = ...,
# markerfacecoloralt: Optional[str] = ...,
# markersize: Optional[float] = ...,
# markevery: Optional[
#     Union[int, Tuple[int, int], slice, List[int], float, Tuple[float, float]]
# ] = ...,
# path_effect: Optional[AbstractPathEffect] = ...,
# picker: Optional[float] = ...,
# pickradius: float = ...,
# rasterized: Optional[bool] = ...,
# sketch_params: Dict[str, Optional[float]] = ...,
# snap: Optional[bool] = ...,
# solid_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
# url: Optional[str] = ...,
# visible: Optional[bool] = ...,
# xdata: Optional[_NumericArray] = ...,
# ydata: Optional[_NumericArray] = ...,
# zorder: Optional[float] = ...

# # === Text kwargs ===
# agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
# alpha: Optional[float] = ...,
# animated: Optional[bool] = ...,
# antialiased: Optional[bool] = ...,
# bbox: Optional[Dict[str, Union[str, float]]] = ...,
# clip_box: Optional[Bbox] = ...,
# clip_on: Optional[bool] = ...,
# clip_path: Optional[Callable[[Path, Transform], None]] = ...,
# color: Optional[str] = ...,
# contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
# figure: Optional[Figure] = ...,
# fontfamily: Optional[Union[str, List[str]]] = ...,
# fontproperties: Optional[FontProperties] = ...,
# fontsize: Optional[Union[Literal['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'], int]] = ...,
# fontstretch: Optional[Union[int, Literal['ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded']]] = ...,
# gid: Optional[str] = ...,
# horizontalalignment: Literal["center", "right", "left"] = ...,
# in_layout: Optional[bool] = ...,
# label: object = ...,
# linespacing: Optional[float] = ...,
# multialignment: Literal["left", "right", "center"] = ...,
# path_effect: Optional[AbstractPathEffect] = ...,
# picker: Optional[float] = ...,
# pickradius: float = ...,
# rasterized: Optional[bool] = ...,
# sketch_params: Dict[str, Optional[float]] = ...,
# snap: Optional[bool] = ...,
# url: Optional[str] = ...,
# usetext: Optional[bool] = ...,
# verticalalignment: Literal['center', 'top', 'bottom', 'baseline', 'center_baseline'] = ...,
# visible: Optional[bool] = ...,
# wrap: bool = ...,
# x: Optional[float] = ...,
# y: Optional[float] = ...,
# zorder: Optional[float] = ...,
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
        pad: Optional[float] = ...,
        h_pad: Optional[float] = ...,
        w_pad: Optional[float] = ...,
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
def plot(
    x: _Data,
    y: _Data,
    *,
    color: Optional[str] = ...,
    label: str = ...,
    linestyle: Literal["-", "--", "-.", ":", ""] = ...,
    marker: str = ...,
    markerfacecolor: str = ...,
    markersize: float = ...,
    scalex: bool = ...,
    scaley: bool = ...,
    zorder: float = ...,
) -> None: ...
def show() -> None: ...
def xlim(
    left: float = ...,
    right: float = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    xmin: float = ...,
    xmax: float = ...,
) -> Tuple[float, float]: ...
def ylim(
    bottom: float = ...,
    top: float = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    ymin: float = ...,
    ymax: float = ...,
) -> Tuple[float, float]: ...
def xticks(
    ticks: Optional[_NumericArray] = ...,
    labels: Optional[_StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    #  === Text kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    bbox: Optional[Dict[str, Union[str, float]]] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    fontproperties: Optional[FontProperties] = ...,
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    fontstretch: Optional[
        Union[
            int,
            Literal[
                "ultra-condensed",
                "extra-condensed",
                "condensed",
                "semi-condensed",
                "normal",
                "semi-expanded",
                "expanded",
                "extra-expanded",
                "ultra-expanded",
            ],
        ]
    ] = ...,
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    visible: Optional[bool] = ...,
    wrap: bool = ...,
    x: Optional[float] = ...,
    y: Optional[float] = ...,
    zorder: Optional[float] = ...,
) -> Tuple[List[float], List[str]]: ...
def yticks(
    ticks: Optional[_NumericArray] = ...,
    labels: Optional[_StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    #  === Text kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    bbox: Optional[Dict[str, Union[str, float]]] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    fontproperties: Optional[FontProperties] = ...,
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    fontstretch: Optional[
        Union[
            int,
            Literal[
                "ultra-condensed",
                "extra-condensed",
                "condensed",
                "semi-condensed",
                "normal",
                "semi-expanded",
                "expanded",
                "extra-expanded",
                "ultra-expanded",
            ],
        ]
    ] = ...,
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    visible: Optional[bool] = ...,
    wrap: bool = ...,
    x: Optional[float] = ...,
    y: Optional[float] = ...,
    zorder: Optional[float] = ...,
) -> Tuple[List[float], List[str]]: ...
def xlabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
    #  === Text kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    bbox: Optional[Dict[str, Union[str, float]]] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    fontproperties: Optional[FontProperties] = ...,
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    fontstretch: Optional[
        Union[
            int,
            Literal[
                "ultra-condensed",
                "extra-condensed",
                "condensed",
                "semi-condensed",
                "normal",
                "semi-expanded",
                "expanded",
                "extra-expanded",
                "ultra-expanded",
            ],
        ]
    ] = ...,
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    visible: Optional[bool] = ...,
    wrap: bool = ...,
    x: Optional[float] = ...,
    y: Optional[float] = ...,
    zorder: Optional[float] = ...,
) -> str: ...
def ylabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
    #  === Text kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    bbox: Optional[Dict[str, Union[str, float]]] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    fontproperties: Optional[FontProperties] = ...,
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    fontstretch: Optional[
        Union[
            int,
            Literal[
                "ultra-condensed",
                "extra-condensed",
                "condensed",
                "semi-condensed",
                "normal",
                "semi-expanded",
                "expanded",
                "extra-expanded",
                "ultra-expanded",
            ],
        ]
    ] = ...,
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    visible: Optional[bool] = ...,
    wrap: bool = ...,
    x: Optional[float] = ...,
    y: Optional[float] = ...,
    zorder: Optional[float] = ...,
) -> str: ...
def fill_between(
    x: _NumericArray,
    y1: Union[_NumericArray, float],
    y2: Union[_NumericArray, float] = ...,
    where: Optional[List[bool]] = ...,
    interpolate: bool = ...,
    step: Optional[Literal["pre", "post", "mid"]] = ...,
    *,
    data: Optional[_Data] = ...,
    #  TODO: Replace kwargs with PolygonCollection kwargs
    **kwargs: Any,
) -> PolyCollection: ...
def axhline(
    y: float = ...,
    xmin: float = ...,
    xmax: float = ...,
    #  ===  Line2D kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
    dashes: Optional[Union[Sequence[float], Tuple[None, None]]] = ...,
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
    figure: Optional[Figure] = ...,
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
    gid: Optional[str] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
    linewidth: Optional[float] = ...,
    marker: Optional[str] = ...,
    markeredgecolor: Optional[str] = ...,
    markerfacecolor: Optional[str] = ...,
    markerfacecoloralt: Optional[str] = ...,
    markersize: Optional[float] = ...,
    markevery: Optional[
        Union[int, Tuple[int, int], slice, List[int], float, Tuple[float, float]]
    ] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    solid_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    url: Optional[str] = ...,
    visible: Optional[bool] = ...,
    xdata: Optional[_NumericArray] = ...,
    ydata: Optional[_NumericArray] = ...,
    zorder: Optional[float] = ...,
) -> Line2D: ...
def axvline(
    x: float = ...,
    ymin: float = ...,
    ymax: float = ...,
    #  === Line2D kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
    dashes: Optional[Union[Sequence[float], Tuple[None, None]]] = ...,
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
    figure: Optional[Figure] = ...,
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
    gid: Optional[str] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
    linewidth: Optional[float] = ...,
    marker: Optional[str] = ...,
    markeredgecolor: Optional[str] = ...,
    markerfacecolor: Optional[str] = ...,
    markerfacecoloralt: Optional[str] = ...,
    markersize: Optional[float] = ...,
    markevery: Optional[
        Union[int, Tuple[int, int], slice, List[int], float, Tuple[float, float]]
    ] = ...,
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    solid_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    url: Optional[str] = ...,
    visible: Optional[bool] = ...,
    xdata: Optional[_NumericArray] = ...,
    ydata: Optional[_NumericArray] = ...,
    zorder: Optional[float] = ...,
) -> Line2D: ...
