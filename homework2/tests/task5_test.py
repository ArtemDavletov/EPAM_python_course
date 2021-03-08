import string
from typing import Iterable, List

import pytest

from homework2.hw5 import custom_range


@pytest.mark.parametrize(
    ["iterable", "expected_result", "args"],
    [
        (string.ascii_lowercase, ["a", "b", "c", "d", "e", "f"], ["g"]),
        (string.ascii_lowercase, ["g", "h", "i", "j", "k", "l", "m", "n", "o"], ["g", "p"]),
        (string.ascii_lowercase, ["p", "n", "l", "j", "h"], ["p", "g", -2]),
        (string.ascii_lowercase, [], ["z", "a"]),
    ],
)
def test_get_most_common_non_ascii_char(iterable: Iterable, expected_result, args: List):
    assert custom_range(iterable, *args) == expected_result, "Incorrect answer for input data: iterable"
