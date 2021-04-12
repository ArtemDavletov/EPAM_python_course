import os
from pathlib import Path
from random import randint
from typing import List, Tuple

import pytest

from homework9.hw1 import lines_from_file_generator, merge_sorted_lists


def prepare_file(filename: str = "test.txt") -> Tuple[Path, List[int]]:
    file_path = Path(__file__).parent / filename
    list_data = []
    num = randint(0, 100)

    file = open(file_path, "w+")
    try:
        for i in range(num):
            val = randint(100, 1000)
            file.write(f"{val} \n")
            list_data.append(val)
    finally:
        file.close()

    return file_path, list_data


def test_translate_file_to_list():
    file_path, list_data = prepare_file()
    try:
        with open(file_path) as file:
            assert list(lines_from_file_generator(file)) == list_data
    finally:
        os.remove(file_path)


@pytest.mark.parametrize(
    ["lists", "expected_result"],
    [
        ([[]], []),
        ([[], [], [], []], []),
        ([[1], [], [], []], [1]),
        ([[1], [1], [1], [1]], [1, 1, 1, 1]),
    ],
)
def test_merge_sorted_lists(lists, expected_result):
    assert merge_sorted_lists(*lists) == expected_result
