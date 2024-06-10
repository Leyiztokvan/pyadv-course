"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-course")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "leyiztokvan"
__email__ = "first.last@example.com"

# add this line to access modules and submodules from my python package (for e.g. the algos submodule)
from . import algos