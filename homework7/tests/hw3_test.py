from typing import List, Union

import pytest

from homework7.hw3 import check_columns, check_diagonals, check_rows, is_finished


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["x", "x", "x"], ["o", "o", "-"], ["-", "-", "-"]], False),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], False),
        ([["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]], True),
    ],
)
def test_is_finished(board: List[List], expected_result: bool):
    assert is_finished(board) == expected_result


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["x", "x", "x"], ["o", "o", "-"], ["-", "-", "-"]], False),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], False),
        ([["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]], False),
        ([["o", "x", "x"], ["o", "o", "x"], ["x", "x", "o"]], "o"),
        ([["o", "x", "x"], ["o", "x", "x"], ["x", "x", "o"]], "x"),
    ],
)
def test_check_diagonals(board: List[List], expected_result: Union[str, bool]):
    assert check_diagonals(board) == expected_result


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["x", "x", "x"], ["o", "o", "-"], ["-", "-", "-"]], "x"),
        ([["-", "-", "x"], ["x", "x", "-"], ["o", "o", "o"]], "o"),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], False),
        ([["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]], False),
        ([["o", "x", "x"], ["o", "o", "x"], ["x", "x", "o"]], False),
        ([["o", "x", "x"], ["o", "x", "x"], ["x", "x", "o"]], False),
    ],
)
def test_check_rows(board: List[List], expected_result: Union[str, bool]):
    assert check_rows(board) == expected_result


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["x", "x", "x"], ["o", "o", "-"], ["-", "-", "-"]], False),
        ([["-", "-", "x"], ["x", "x", "-"], ["o", "o", "o"]], False),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], False),
        ([["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]], False),
        ([["o", "x", "x"], ["o", "o", "x"], ["x", "x", "o"]], False),
        ([["o", "x", "x"], ["o", "x", "x"], ["x", "x", "o"]], "x"),
        ([["o", "x", "o"], ["x", "o", "o"], ["x", "x", "o"]], "o"),
        ([["x", "x", "o"], ["-", "-", "o"], ["x", "x", "o"]], "o"),
    ],
)
def test_check_columns(board: List[List], expected_result: Union[str, bool]):
    assert check_columns(board) == expected_result
