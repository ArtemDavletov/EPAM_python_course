import pytest

from homework9.hw2 import SupressorClass, supressor

ALL_ERRORS = [
    AssertionError,
    AttributeError,
    EOFError,
    FloatingPointError,
    GeneratorExit,
    ImportError,
    IndexError,
    KeyError,
    KeyboardInterrupt,
    MemoryError,
    NameError,
    NotImplementedError,
    OSError,
    OverflowError,
    ReferenceError,
    RuntimeError,
    StopIteration,
    SyntaxError,
    IndentationError,
    TabError,
    SystemError,
    SystemExit,
    TypeError,
    UnboundLocalError,
    UnicodeError,
    ValueError,
    ZeroDivisionError,
]


@pytest.mark.parametrize(
    "err",
    ALL_ERRORS,
)
def test_supressor_success(err):
    with supressor(err):
        raise err


@pytest.mark.parametrize(
    "err",
    ALL_ERRORS,
)
def test_supressor_class_success(err):
    with SupressorClass(err):
        raise err
