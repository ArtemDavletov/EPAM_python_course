from random import randint

import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["radius", "number"],
    [(1000, 1000), (10000, 1000)],
)
def test_find_maximum_and_minimum(radius: int, number: int, file_name: str = "tests/test_data/task3_test.txt"):
    min_val = 0
    max_val = 0

    i = 1
    with open(file_name, "r+") as file:
        file.truncate(0)
        values = []
        while i < number:
            val = randint(-1 * radius, radius)

            if val < min_val:
                min_val = val

            if val > max_val:
                max_val = val

            values.append(str(val))

            if i % 10 == 0:
                file.write(" ".join(values) + "\n")
                values = []

            i += 1

    assert find_maximum_and_minimum(file_name=file_name) == (
        min_val,
        max_val,
    ), f"Incorrect answer for file: {file_name}"
