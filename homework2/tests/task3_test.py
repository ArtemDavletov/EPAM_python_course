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
        ),
        (
            [
                [1, 3],
                [1, 4],
                [1, 5],
                [1, 6],
            ],
            [[1], [3, 4, 5, 6]],
        ),
        (
            [
                [1, 3],
                [1, 4],
                [1, 5],
                [1, 6],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
            ],
            [[1, 2], [3, 4, 5, 6]],
        ),
        (
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
            [[1, 2], [3, 4], [5, 6]],
        ),
    ],
)
def test_combinations(expected_result: List[List[int]], args: List[List[int]]):
    assert combinations(*args) == expected_result, f"Incorrect answer for input list: {args}"
