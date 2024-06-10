"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-course")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "leyiztokvan"
__email__ = "leyiztokvan@gmail.com"
