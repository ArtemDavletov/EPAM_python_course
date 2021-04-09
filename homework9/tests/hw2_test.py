import pytest

from homework9.hw2 import SupressorClass, supressor


@pytest.mark.parametrize(
    ["sup", "err", "expression"],
    [
        (supressor, IndexError, "[][2]"),
        (supressor, KeyError, 'dict()["key"]'),
        (SupressorClass, IndexError, "[][2]"),
        (SupressorClass, KeyError, 'dict()["key"]'),
    ],
)
def test_supressor_success(sup, err, expression):
    with sup(err):
        eval(expression)
