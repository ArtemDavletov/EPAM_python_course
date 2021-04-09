import os
import random
import string
from pathlib import Path
from typing import Tuple

import pytest

from homework9.hw3 import universal_file_counter

DIR_PATH = Path(__file__).parent


def random_string(n=5):
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def prepare_file(filename: str = "test.txt") -> Tuple[Path, int]:
    file_path = Path(__file__).parent / filename
    num = random.randint(0, 100)

    file = open(file_path, "w+")
    try:
        for i in range(num):
            file.write(f"{random_string()} {random_string()}\n")
    finally:
        file.close()

    return file_path, num


@pytest.mark.trylast
def test_universal_file_counter():
    file_path, num = prepare_file()
    try:
        result = universal_file_counter(file_path.parent, "txt")
        assert result == num
    finally:
        os.remove(file_path)


@pytest.mark.trylast
def test_universal_file_counter_with_tokenizer():
    file_path, num = prepare_file()
    try:
        result = universal_file_counter(file_path.parent, "txt", str.split)
        assert result == num * 2
    finally:
        os.remove(file_path)


def test_universal_file_counter_with_non_existing_file():
    assert universal_file_counter(DIR_PATH, "txt") == 0


def test_universal_file_counter_with_non_existing_file_extension():
    assert universal_file_counter(DIR_PATH, " ") == 0
