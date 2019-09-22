"""Pandas public API"""
from . import testing
from .core.frame import DataFrame as DataFrame
from .core.series import Series as Series
from .core.indexes import Index as Index

# manual import wasn't working for some reason but * import does work, so...
from ._core import *
