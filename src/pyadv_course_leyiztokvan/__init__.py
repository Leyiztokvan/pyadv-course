"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-course")
except PackageNotFoundError:
    __version__ = "0.1.1"
__author__ = "leyiztokvan"
__email__ = "leyiztokvan@gmail.com"
