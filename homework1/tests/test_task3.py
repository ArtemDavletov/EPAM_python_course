from typing import Tuple

import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("tests/test_data/task3_test1.txt", (-1000, 1000)),
        ("tests/test_data/task3_test2.txt", (-15, 14)),
        ("tests/test_data/task3_test3.txt", (0, 0)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    assert (
        find_maximum_and_minimum(file_name=file_name) == expected_result
    ), f"Incorrect answer for file: {file_name}"
