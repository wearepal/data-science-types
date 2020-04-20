from pathlib import Path
from typing import (
    Any,
    ByteString,
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

# #  === Line2D kwargs ===
# agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
# alpha: Optional[float] = ...,
# animated: Optional[bool] = ...,
# antialiased: Optional[bool] = ...,
# aa: Optional[bool] = ...,  #  alias of antialiased
# clip_box: Optional[Bbox] = ...,
# clip_on: Optional[bool] = ...,
# clip_path: Optional[Callable[[Path, Transform], None]] = ...,
# color: Optional[str] = ...,
# c: Optional[str] = ...,  # alias of color
# contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
# dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
# dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
# dashes: Optional[[Sequence[float], Tuple[None, None]]] = ...,
# drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
# ds: Literal[
#     "default", "steps", "steps-pre", "steps-mid", "steps-post"
# ] = ...,  #  alias of drawstyle
# figure: Optional[Figure] = ...,
# fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
# gid: Optional[str] = ...,
# in_layout: Optional[bool] = ...,
# label: object = ...,
# linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
# ls: Optional[Literal["-", "--", "-.", ":", ""]] = ...,  #  alias of linestyle
# linewidth: Optional[float] = ...,
# lw: Optional[float] = ...,  # alias of linewidth
# marker: Optional[str] = ...,
# markeredgecolor: Optional[str] = ...,
# mec: Optional[str] = ...,  #  alias of markeredgecolor
# markeredgewidth: Optional[float] = ...,
# mew: Optional[float] = ...,
# markerfacecolor: Optional[str] = ...,
# mfc: Optional[str] = ...,  #  alias of markerfacecolor
# markerfacecoloralt: Optional[str] = ...,
# mfcalt: Optional[str] = ...,  # alias of markerfacecoloralt
# markersize: Optional[float] = ...,
# ms: Optional[float] = ...,  #  alias of markersize
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

# #  === Text kwargs ===
# agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
# alpha: Optional[float] = ...,
# animated: Optional[bool] = ...,
# antialiased: Optional[bool] = ...,
# bbox: Optional[Dict[str, Union[str, float]]] = ...,
# clip_box: Optional[Bbox] = ...,
# clip_on: Optional[bool] = ...,
# clip_path: Optional[Callable[[Path, Transform], None]] = ...,
# color: Optional[str] = ...,
# c: Optional[str] = ...,  #  alias of color
# contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
# figure: Optional[Figure] = ...,
# fontfamily: Optional[Union[str, List[str]]] = ...,
# family: Optional[Union[str, List[str]]] = ...,  #  alias of fontfamily
# fontproperties: Optional[FontProperties] = ...,
# font_properties: Optional[FontProperties] = ...,  #  alias of fontproperties
# fontsize: Optional[
#     Union[
#         Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
#     ]
# ] = ...,
# size: Optional[
#     Union[
#         Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
#     ]
# ] = ...,  # alias of fontsize
# fontstretch: Optional[
#     Union[
#         int,
#         Literal[
#             "ultra-condensed",
#             "extra-condensed",
#             "condensed",
#             "semi-condensed",
#             "normal",
#             "semi-expanded",
#             "expanded",
#             "extra-expanded",
#             "ultra-expanded",
#         ],
#     ]
# ] = ...,
# stretch: Optional[
#     Union[
#         int,
#         Literal[
#             "ultra-condensed",
#             "extra-condensed",
#             "condensed",
#             "semi-condensed",
#             "normal",
#             "semi-expanded",
#             "expanded",
#             "extra-expanded",
#             "ultra-expanded",
#         ],
#     ]
# ] = ...,  #  alias of fontstretch
# fontstyle: Optional[Literal["normal", "italic", "oblique"]] = ...,
# style: Optional[Literal["normal", "italic", "oblique"]] = ...,  #  alias of fontstyle
# fontvariant: Optional[Literal["normal", "small-caps"]] = ...,
# variant: Optional[Literal["normal", "small-caps"]] = ...,  #  alias of fontvariant
# fontweight: Optional[
#     Union[
#         float,
#         Literal[
#             "ultralight",
#             "light",
#             "normal",
#             "regular",
#             "book",
#             "medium",
#             "roman",
#             "semibold",
#             "demibold",
#             "demi",
#             "bold",
#             "heavy",
#             "extra bold",
#             "black",
#         ],
#     ]
# ] = ...,
# weight: Optional[
#     Union[
#         float,
#         Literal[
#             "ultralight",
#             "light",
#             "normal",
#             "regular",
#             "book",
#             "medium",
#             "roman",
#             "semibold",
#             "demibold",
#             "demi",
#             "bold",
#             "heavy",
#             "extra bold",
#             "black",
#         ],
#     ]
# ] = ...,  #  alias of fontweight
# gid: Optional[str] = ...,
# horizontalalignment: Literal["center", "right", "left"] = ...,
# ha: Literal["center", "right", "left"] = ...,  #  alias of horizontalalignment
# in_layout: Optional[bool] = ...,
# label: object = ...,
# linespacing: Optional[float] = ...,
# multialignment: Literal["left", "right", "center"] = ...,
# ma: Literal["left", "right", "center"] = ...,  #  alias of multialignment
# path_effect: Optional[AbstractPathEffect] = ...,
# picker: Optional[float] = ...,
# pickradius: float = ...,
# rasterized: Optional[bool] = ...,
# sketch_params: Dict[str, Optional[float]] = ...,
# snap: Optional[bool] = ...,
# url: Optional[str] = ...,
# usetext: Optional[bool] = ...,
# verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
# va: Literal[
#     "center", "top", "bottom", "baseline", "center_baseline"
# ] = ...,  #  alias of vertical alignment
# visible: Optional[bool] = ...,
# wrap: bool = ...,
# x: Optional[float] = ...,
# y: Optional[float] = ...,
# zorder: Optional[float] = ...

class Figure:
    def savefig(
        self,
        fname: Union[str, Path],
        dpi: Optional[int] = ...,
        quality: Optional[int] = ...,
        optimize: bool = ...,
        progressive: bool = ...,
        facecolor: Optional[str] = ...,
        edgecolor: Optional[str] = ...,
        orientation: Literal["landscape", "portrait"] = ...,
        papertype: str = ...,
        format: str = ...,
        transparent: bool = ...,
        bbox_inches: Optional[Union[Literal["tight"], Bbox]] = ...,
        pad_inches: Optional[int] = ...,
        bbox_extra_artists: Sequence[Artist] = ...,
        metadata: Union[Dict[str, Optional[str]], Dict[ByteString, ByteString]] = ...,
        #  TODO: expand pil kwargs
        pil_kwargs: Dict[str, Any] = ...,
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
    fmt: Optional[str] = ...,
    *,
    scalex: bool = ...,
    scaley: bool = ...,
    #  === Line2D kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    aa: Optional[bool] = ...,  #  alias of antialiased
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    c: Optional[str] = ...,  # alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
    dashes: Optional[Union[Sequence[float], Tuple[None, None]]] = ...,
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
    ds: Literal[
        "default", "steps", "steps-pre", "steps-mid", "steps-post"
    ] = ...,  #  alias of drawstyle
    figure: Optional[Figure] = ...,
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
    gid: Optional[str] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
    ls: Optional[Literal["-", "--", "-.", ":", ""]] = ...,  #  alias of linestyle
    linewidth: Optional[float] = ...,
    lw: Optional[float] = ...,  # alias of linewidth
    marker: Optional[str] = ...,
    markeredgecolor: Optional[str] = ...,
    mec: Optional[str] = ...,  #  alias of markeredgecolor
    markeredgewidth: Optional[float] = ...,
    mew: Optional[float] = ...,
    markerfacecolor: Optional[str] = ...,
    mfc: Optional[str] = ...,  #  alias of markerfacecolor
    markerfacecoloralt: Optional[str] = ...,
    mfcalt: Optional[str] = ...,  # alias of markerfacecoloralt
    markersize: Optional[float] = ...,
    ms: Optional[float] = ...,  #  alias of markersize
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
) -> None: ...
def show() -> None: ...
def savefig(
    fname: Union[str, Path],
    dpi: Optional[int] = ...,
    quality: Optional[int] = ...,
    optimize: bool = ...,
    progressive: bool = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    orientation: Literal["landscape", "portrait"] = ...,
    papertype: str = ...,
    format: str = ...,
    transparent: bool = ...,
    bbox_inches: Optional[Union[Literal["tight"], Bbox]] = ...,
    pad_inches: Optional[int] = ...,
    bbox_extra_artists: Sequence[Artist] = ...,
    metadata: Union[Dict[str, Optional[str]], Dict[ByteString, ByteString]] = ...,
    #  TODO: expand pil kwargs
    pil_kwargs: Dict[str, Any] = ...,
) -> None: ...
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
    c: Optional[str] = ...,  #  alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    family: Optional[Union[str, List[str]]] = ...,  #  alias of fontfamily
    fontproperties: Optional[FontProperties] = ...,
    font_properties: Optional[FontProperties] = ...,  #  alias of fontproperties
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    size: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,  # alias of fontsize
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
    stretch: Optional[
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
    ] = ...,  #  alias of fontstretch
    fontstyle: Optional[Literal["normal", "italic", "oblique"]] = ...,
    style: Optional[Literal["normal", "italic", "oblique"]] = ...,  #  alias of fontstyle
    fontvariant: Optional[Literal["normal", "small-caps"]] = ...,
    variant: Optional[Literal["normal", "small-caps"]] = ...,  #  alias of fontvariant
    fontweight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,
    weight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,  #  alias of fontweight
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    ha: Literal["center", "right", "left"] = ...,  #  alias of horizontalalignment
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    ma: Literal["left", "right", "center"] = ...,  #  alias of multialignment
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    va: Literal[
        "center", "top", "bottom", "baseline", "center_baseline"
    ] = ...,  #  alias of vertical alignment
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
    c: Optional[str] = ...,  #  alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    family: Optional[Union[str, List[str]]] = ...,  #  alias of fontfamily
    fontproperties: Optional[FontProperties] = ...,
    font_properties: Optional[FontProperties] = ...,  #  alias of fontproperties
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    size: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,  # alias of fontsize
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
    stretch: Optional[
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
    ] = ...,  #  alias of fontstretch
    fontstyle: Optional[Literal["normal", "italic", "oblique"]] = ...,
    style: Optional[Literal["normal", "italic", "oblique"]] = ...,  #  alias of fontstyle
    fontvariant: Optional[Literal["normal", "small-caps"]] = ...,
    variant: Optional[Literal["normal", "small-caps"]] = ...,  #  alias of fontvariant
    fontweight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,
    weight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,  #  alias of fontweight
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    ha: Literal["center", "right", "left"] = ...,  #  alias of horizontalalignment
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    ma: Literal["left", "right", "center"] = ...,  #  alias of multialignment
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    va: Literal[
        "center", "top", "bottom", "baseline", "center_baseline"
    ] = ...,  #  alias of vertical alignment
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
    c: Optional[str] = ...,  #  alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    family: Optional[Union[str, List[str]]] = ...,  #  alias of fontfamily
    fontproperties: Optional[FontProperties] = ...,
    font_properties: Optional[FontProperties] = ...,  #  alias of fontproperties
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    size: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,  # alias of fontsize
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
    stretch: Optional[
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
    ] = ...,  #  alias of fontstretch
    fontstyle: Optional[Literal["normal", "italic", "oblique"]] = ...,
    style: Optional[Literal["normal", "italic", "oblique"]] = ...,  #  alias of fontstyle
    fontvariant: Optional[Literal["normal", "small-caps"]] = ...,
    variant: Optional[Literal["normal", "small-caps"]] = ...,  #  alias of fontvariant
    fontweight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,
    weight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,  #  alias of fontweight
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    ha: Literal["center", "right", "left"] = ...,  #  alias of horizontalalignment
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    ma: Literal["left", "right", "center"] = ...,  #  alias of multialignment
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    va: Literal[
        "center", "top", "bottom", "baseline", "center_baseline"
    ] = ...,  #  alias of vertical alignment
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
    c: Optional[str] = ...,  #  alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[Tuple[bool, dict]]]] = ...,
    figure: Optional[Figure] = ...,
    fontfamily: Optional[Union[str, List[str]]] = ...,
    family: Optional[Union[str, List[str]]] = ...,  #  alias of fontfamily
    fontproperties: Optional[FontProperties] = ...,
    font_properties: Optional[FontProperties] = ...,  #  alias of fontproperties
    fontsize: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,
    size: Optional[
        Union[
            Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"], int
        ]
    ] = ...,  # alias of fontsize
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
    stretch: Optional[
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
    ] = ...,  #  alias of fontstretch
    fontstyle: Optional[Literal["normal", "italic", "oblique"]] = ...,
    style: Optional[Literal["normal", "italic", "oblique"]] = ...,  #  alias of fontstyle
    fontvariant: Optional[Literal["normal", "small-caps"]] = ...,
    variant: Optional[Literal["normal", "small-caps"]] = ...,  #  alias of fontvariant
    fontweight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,
    weight: Optional[
        Union[
            float,
            Literal[
                "ultralight",
                "light",
                "normal",
                "regular",
                "book",
                "medium",
                "roman",
                "semibold",
                "demibold",
                "demi",
                "bold",
                "heavy",
                "extra bold",
                "black",
            ],
        ]
    ] = ...,  #  alias of fontweight
    gid: Optional[str] = ...,
    horizontalalignment: Literal["center", "right", "left"] = ...,
    ha: Literal["center", "right", "left"] = ...,  #  alias of horizontalalignment
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linespacing: Optional[float] = ...,
    multialignment: Literal["left", "right", "center"] = ...,
    ma: Literal["left", "right", "center"] = ...,  #  alias of multialignment
    path_effect: Optional[AbstractPathEffect] = ...,
    picker: Optional[float] = ...,
    pickradius: float = ...,
    rasterized: Optional[bool] = ...,
    sketch_params: Dict[str, Optional[float]] = ...,
    snap: Optional[bool] = ...,
    url: Optional[str] = ...,
    usetext: Optional[bool] = ...,
    verticalalignment: Literal["center", "top", "bottom", "baseline", "center_baseline"] = ...,
    va: Literal[
        "center", "top", "bottom", "baseline", "center_baseline"
    ] = ...,  #  alias of vertical alignment
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
    #  === Line2D kwargs ===
    agg_filter: Callable[[_NumericArray, int], _NumericArray] = ...,
    alpha: Optional[float] = ...,
    animated: Optional[bool] = ...,
    antialiased: Optional[bool] = ...,
    aa: Optional[bool] = ...,  #  alias of antialiased
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    c: Optional[str] = ...,  # alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
    dashes: Optional[Union[Sequence[float], Tuple[None, None]]] = ...,
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
    ds: Literal[
        "default", "steps", "steps-pre", "steps-mid", "steps-post"
    ] = ...,  #  alias of drawstyle
    figure: Optional[Figure] = ...,
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
    gid: Optional[str] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
    ls: Optional[Literal["-", "--", "-.", ":", ""]] = ...,  #  alias of linestyle
    linewidth: Optional[float] = ...,
    lw: Optional[float] = ...,  # alias of linewidth
    marker: Optional[str] = ...,
    markeredgecolor: Optional[str] = ...,
    mec: Optional[str] = ...,  #  alias of markeredgecolor
    markeredgewidth: Optional[float] = ...,
    mew: Optional[float] = ...,
    markerfacecolor: Optional[str] = ...,
    mfc: Optional[str] = ...,  #  alias of markerfacecolor
    markerfacecoloralt: Optional[str] = ...,
    mfcalt: Optional[str] = ...,  # alias of markerfacecoloralt
    markersize: Optional[float] = ...,
    ms: Optional[float] = ...,  #  alias of markersize
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
    aa: Optional[bool] = ...,  #  alias of antialiased
    clip_box: Optional[Bbox] = ...,
    clip_on: Optional[bool] = ...,
    clip_path: Optional[Callable[[Path, Transform], None]] = ...,
    color: Optional[str] = ...,
    c: Optional[str] = ...,  # alias of color
    contains: Optional[Callable[[Artist, MouseEvent], Tuple[bool, dict]]] = ...,
    dash_capstyle: Optional[Literal["butt", "round", "projecting"]] = ...,
    dash_jointstyle: Optional[Literal["miter", "round", "bevel"]] = ...,
    dashes: Optional[Union[Sequence[float], Tuple[None, None]]] = ...,
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"] = ...,
    ds: Literal[
        "default", "steps", "steps-pre", "steps-mid", "steps-post"
    ] = ...,  #  alias of drawstyle
    figure: Optional[Figure] = ...,
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
    gid: Optional[str] = ...,
    in_layout: Optional[bool] = ...,
    label: object = ...,
    linestyle: Optional[Literal["-", "--", "-.", ":", ""]] = ...,
    ls: Optional[Literal["-", "--", "-.", ":", ""]] = ...,  #  alias of linestyle
    linewidth: Optional[float] = ...,
    lw: Optional[float] = ...,  # alias of linewidth
    marker: Optional[str] = ...,
    markeredgecolor: Optional[str] = ...,
    mec: Optional[str] = ...,  #  alias of markeredgecolor
    markeredgewidth: Optional[float] = ...,
    mew: Optional[float] = ...,
    markerfacecolor: Optional[str] = ...,
    mfc: Optional[str] = ...,  #  alias of markerfacecolor
    markerfacecoloralt: Optional[str] = ...,
    mfcalt: Optional[str] = ...,  # alias of markerfacecoloralt
    markersize: Optional[float] = ...,
    ms: Optional[float] = ...,  #  alias of markersize
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
