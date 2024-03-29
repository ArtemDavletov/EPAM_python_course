"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
from contextlib import contextmanager


@contextmanager
def supressor(exception):
    try:
        yield
    except exception:
        ...  # Catch behaviour


class SupressorClass:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type == self.exception


with supressor(IndexError):
    [][2]

with SupressorClass(IndexError):
    [][2]
