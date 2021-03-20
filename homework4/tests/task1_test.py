import os
import random
from random import choice, randint, uniform
from string import ascii_letters

import pytest

from homework4.task_1_read_file import read_magic_number


def fill_in_file(number: float) -> None:
    file = open("test.txt", "w")
    file.write(str(number))
    file.close()


def test_positive_read_magic_number_positive_result():
    number = uniform(1, 3)
    try:
        fill_in_file(number)
        assert read_magic_number("test.txt") is True
    finally:
        os.remove("test.txt")


def test_positive_read_magic_number_negative_result():
    number = random.choice((uniform(3.1, 10000), uniform(-10000, 1)))
    try:
        fill_in_file(number)
        assert read_magic_number("test.txt") is False
    finally:
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
