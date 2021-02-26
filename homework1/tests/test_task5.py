from typing import List, Tuple

import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-10, -10, -10, 1000, -10, -10, -10, -10, -10, -10], 3, 1000),
        ([-10, -10, -10, 1000], 3, 1000),
        ([-10, -10, -10, 1000], 4, 1000),
        ([1000, -10, -10, -10], 4, 1000),
    ],
)
def test_find_maximal_subarray_sum(
    nums: List[int], k: int, expected_result: Tuple[int, int]
):
    assert (
        find_maximal_subarray_sum(nums=nums, k=k) == expected_result
    ), f"Incorrect answer for numbers: {nums}, when k={k}"
