"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable


def custom_range(iterable: Iterable, *args):
    iterable = list(iterable)

    if args is None:
        return iterable

    if len(args) == 1:
        return iterable[:iterable.index(args[0])]

    if len(args) == 2:
        return iterable[iterable.index(args[0]): iterable.index(args[1])]

    if len(args) == 3:
        return iterable[iterable.index(args[0]): iterable.index(args[1]): args[2]]
