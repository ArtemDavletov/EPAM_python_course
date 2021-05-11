import pytest

from homework7.hw2 import simplify_input_string


@pytest.mark.parametrize(
    ["string", "simplified_string"],
    [
        ("ab#c", "ac"),
        ("#####c", "c"),
        ("###", ""),
        ("ccc", "ccc"),
        ("", ""),
    ],
)
def test_simplify_input_string(string: str, simplified_string: str):
    assert simplify_input_string(string) == simplified_string
