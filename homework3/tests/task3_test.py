from typing import Tuple

import pytest

from homework3.task03.task03 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["keywords", "expected_result"],
    [(dict(name="polly", type="bird"), [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}])],
)
def test_make_filter(keywords: dict, expected_result: list):
    assert (
        make_filter(**keywords).apply(sample_data) == expected_result
    ), f"Correct answer for this data is {expected_result}"


@pytest.mark.parametrize(
    ["functions", "data", "expected_result"],
    [((lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)), range(5), [2, 4])],
)
def test_filter(functions: Tuple, data, expected_result: list):
    positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    assert positive_even.apply(data=data) == expected_result, f"Correct answer for this data is {expected_result}"
