"""Public API of numpy"""
from . import testing, random

# manual import wasn't working for some reason but * import does work, so...
from ._core import *
