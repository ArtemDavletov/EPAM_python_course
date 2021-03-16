from collections import Counter
from unittest.mock import MagicMock

import pytest


class ResponseMock:
    text: str

    def __init__(self, text: str):
        self.text = text


class RequestsMock:
    ...


def count_dots_on_i_mock(url: str) -> int:
    try:
        requests = RequestsMock()
        requests.get = MagicMock(return_value=ResponseMock(text=url))
        return Counter(requests.get(url).text)["i"]
    except Exception:
        raise ValueError(f"Unreachable {url}")


@pytest.mark.parametrize(["text", "expected_value"], [("<i></i>", 2), ("", 0), ("i", 1), ("iiiii", 5)])
def test_positive_count_dots_on_i(text, expected_value: int):
    assert count_dots_on_i_mock(text) == expected_value


@pytest.mark.parametrize("text", [123, ResponseMock])
def test_negative_count_dots_on_i(text):
    with pytest.raises(ValueError):
        count_dots_on_i_mock(text)
