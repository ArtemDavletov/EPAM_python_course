from typing import List

import pytest

from homework4.task_5_optional import fizzbuzz


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (0, []),
        (5, ["1", "2", "fizz", "4", "buzz"]),
        (15, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizz buzz"]),
    ],
)
def test_fizzbuzz(number: int, expected_result: List[str]):
    assert list(fizzbuzz(number)) == expected_result
