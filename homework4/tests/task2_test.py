import pytest
import requests_mock

from homework4.task_2_mock_input import count_dots_on_i


@pytest.mark.parametrize(["text", "expected_value"], [("<i></i>", 2), ("", 0), ("i", 1), ("iiiii", 5)])
def test_positive_count_dots_on_i(text, expected_value: int):
    url = "http://mocked-address.com"

    with requests_mock.Mocker() as m:
        m.get(url, text=text)

        assert count_dots_on_i(url) == expected_value


@pytest.mark.parametrize("text", [123, None])
def test_negative_count_dots_on_i(text):
    url = "http://mocked-address.com"

    with pytest.raises(ValueError):
        count_dots_on_i(url)
