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
    if args is None:
        return iterable

    if len(args) == 1:
        answer = []

        i = 0
        while args[i] != args[0]:
            answer.append(args[i])

            i += 1

        return answer

    if len(args) == 2:
        answer = []
        flag = False

        i = 0
        while args[i] != args[1]:
            if args[i] == args[0]:
                flag = True

            if flag:
                answer.append(args[i])

            i += 1

        return answer

    if len(args) == 3:
        answer = []
        flag = False

        if args[2] < 0:
            iterable = list(reversed(iterable))
            args[2] *= -1

        i = 0
        while args[i] != args[1] and i < len(iterable):
            if args[i] == args[0]:
                flag = True

            if flag:
                answer.append(args[i])

            i += args[2]

        return answer
