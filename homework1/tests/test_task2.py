from typing import Sequence

import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
            True,
        ),
        ([0, 1, 1, 2, 3, 5], True),
        ([0, 1, 1], True),
        ([0, 1], True),
        ([0], True),
        ([], False),
        ([1], False),
        ([1, 1], False),
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 33], False),
    ],
)
def test_check_fibonacci(data: Sequence[int], expected_result: bool):
    assert (
        check_fibonacci(data=data) == expected_result
    ), f"Incorrect answer for input sequence: {data}"
