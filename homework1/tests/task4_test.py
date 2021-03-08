from typing import List

import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1], [1], [1], [1], 0),
        ([1, 2], [-2, -1], [0, 100, 1000], [-1000, -100, 0], 6),
    ],
)
def test_check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int):
    assert (
        check_sum_of_four(a=a, b=b, c=c, d=d) == expected_result
    ), f"Incorrect answer for input values a={a}, b={b}, c={c}, d={d}"
