from typing import List, Tuple

import pytest

from homework2.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1))],
)
def test_major_and_minor_elem(inp: List, expected_result: Tuple[int, int]):
    assert (
        major_and_minor_elem(inp) == expected_result
    ), f"[major_and_minor_elem] Incorrect answer for input list: {inp}, correct answer is {expected_result}"
