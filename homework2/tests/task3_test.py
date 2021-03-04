from typing import List

import pytest

from homework2.hw3 import combinations


@pytest.mark.parametrize(
    ["expected_result", "args"],
    [
        (
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
            [[1, 2], [3, 4]],
        )
    ],
)
def test_combinations(expected_result: List[List[int]], args: List[List[int]]):
    assert combinations(*args) == expected_result, f"Incorrect answer for input list: {args}"
