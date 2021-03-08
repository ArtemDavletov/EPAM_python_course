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
    answer = []

    if args is None:
        return iterable

    if len(args) == 1:
        for i in range(iterable.index(args[0])):
            answer.append(iterable[i])

        return answer

    if len(args) == 2:
        step = 1

    if len(args) == 3:
        step = args[2]

    for i in range(iterable.index(args[0]), iterable.index(args[1]), step):
        answer.append(iterable[i])

    return answer
