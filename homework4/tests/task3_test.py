from random import choice, randint
from string import ascii_letters

import pytest
from _pytest.capture import capsys

from homework4.task_3_get_print_output import my_precious_logger


@pytest.mark.parametrize(["text"], ["error: " + "".join(choice(ascii_letters) for _ in range(randint(0, 10)))])
@pytest.fixture
def test_error_my_precious_logger(text: str):
    my_precious_logger(text)
    assert capsys == text


@pytest.mark.parametrize("text", ["".join(choice(ascii_letters) for _ in range(randint(0, 10)))])
@pytest.fixture
def test_success_my_precious_logger(text: str):
    my_precious_logger(text)
    assert capsys == text
