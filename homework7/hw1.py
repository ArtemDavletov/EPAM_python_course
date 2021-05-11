"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def walk_throw_iterable(iterable: Iterable, element: Any):
    occurrences = 0

    for el in iterable:
        if el == element:
            occurrences += 1
        elif isinstance(el, dict):
            occurrences += find_occurrences(el, element)
        elif not isinstance(el, str) and isinstance(el, Iterable):
            occurrences += walk_throw_iterable(el, element)
    return occurrences


def find_occurrences(tree: dict, element: Any) -> int:
    occurrences = 0

    for _, val in tree.items():
        if val == element:
            occurrences += 1
        elif isinstance(val, dict):
            occurrences += find_occurrences(val, element)
        elif not isinstance(val, str) and isinstance(val, Iterable):
            occurrences += walk_throw_iterable(val, element)

    return occurrences


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
