from importlib.metadata import version
from importlib.metadata import PackageNotFoundError

try:
    __version__ = version("python_aid")
except PackageNotFoundError:
    __version__ = "0.0.0"