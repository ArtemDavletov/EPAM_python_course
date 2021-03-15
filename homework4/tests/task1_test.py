import os
from random import choice, randint, uniform
from string import ascii_letters

import pytest

from homework4.task_1_read_file import read_magic_number


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(uniform(1, 3), True), (uniform(3.1, 10000), False), (uniform(-10000, 1), False)],
)
def test_positive_read_magic_number(number: float, expected_result: bool):
    file = open("test.txt", "w")
    file.write(str(number))
    file.close()

    assert read_magic_number("test.txt") == expected_result
    os.remove("test.txt")


@pytest.mark.parametrize(
    "length",
    [randint(-10000, 10000)],
)
def test_negative_read_magic_number(length: int):
    file = open("test.txt", "w")
    file.write("".join(choice(ascii_letters) for _ in range(length)))
    file.close()

    with pytest.raises(ValueError):
        read_magic_number("test.txt")
    os.remove("test.txt")
