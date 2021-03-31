from typing import Any, Iterable

import pytest

from homework7.hw1 import example_tree, find_occurrences, walk_throw_iterable


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [(example_tree, "RED", 6), ({"foo": ["foo", "boo", "buzz", {"foo": "foo"}]}, "foo", 2), ({}, "foo", 0)],
)
def test_find_occurrences_tree(tree: dict, element: Any, expected_result: int):
    assert find_occurrences(tree, element) == expected_result


@pytest.mark.parametrize(
    ["iterable", "element", "expected_result"],
    [
        (["RED", "_RED_", ("RED", "BLUE")], "RED", 2),
        (["RED", "_RED_", ("RED", "BLUE", {"RED": "RED"})], "RED", 3),
        ((), "foo", 0),
    ],
)
def test_find_occurrences_iter(iterable: Iterable, element: Any, expected_result: int):
    assert walk_throw_iterable(iterable, element) == expected_result
