"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from contextlib import ExitStack
from pathlib import Path
from typing import Iterator, List, Union


def translate_file_to_list(file):
    return list(map(int, file.read().strip().split("\n")))


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(file)) for file in file_list]
        # Can expand list comprehension into "for loop" with exception FileNotFoundError and ignoring non-existing files
        # yield from merge_sorted_lists(*map(lambda x: list(map(int, x.read().split("\n"))), files))

        yield from merge_sorted_lists(*map(translate_file_to_list, files))  # More readable and testable


def merge_sorted_lists(*lists) -> List[int]:
    reversed_lists: List[List[int]] = list(map(lambda x: list(reversed(x)), lists))
    result = []

    while [] in reversed_lists:
        reversed_lists.remove([])

    while reversed_lists:
        list_with_min_val = min(reversed_lists, key=lambda x: x[-1])
        result.append(list_with_min_val.pop())

        if not list_with_min_val:
            reversed_lists.remove(list_with_min_val)

    return result


# print(list(merge_sorted_files(["file1.txt", "file2.txt", "file3.txt"])))

# from collections import deque
#
# def merge_sorted_two_lists(first_list: List[int], second_list: List[int]):
#     result = []
#     first_list = deque(first_list)
#     second_list = deque(second_list)
#
#     while first_list and second_list:
#         if first_list[0] >= second_list[0]:
#             result.append(second_list.popleft())
#         else:
#             result.append(first_list.popleft())
#
#     return result + list(first_list) + list(second_list)
#
#
# def merge_sorted_two_lists_faster(first_list: List[int], second_list: List[int]):
#     reversed_first_list = list(reversed(first_list))
#     reversed_second_list = list(reversed(second_list))
#
#     result = []
#     while reversed_first_list and reversed_second_list:
#         if reversed_first_list[-1] >= reversed_second_list[-1]:
#             result.append(reversed_second_list.pop())
#         else:
#             result.append(reversed_first_list.pop())
#
#     reversed_first_list.reverse()
#     reversed_second_list.reverse()
#
#     return result + reversed_first_list + reversed_second_list
#
#
# f_list = []
# s_list = []
#
# for i in range(10):
#     if i % 2 == 0:
#         f_list.append(i)
#     else:
#         s_list.append(i)
#
# print(merge_sorted_lists(f_list, s_list, [10, 11, 12], [1, 10, 100]))
#
#
# import time
#
# f_list = []
# s_list = []
#
# for i in range(10**7):
#     if i % 2 == 0:
#         f_list.append(i)
#     else:
#         s_list.append(i)
#
# print("Lists is done")
#
# start_time = time.time()
#
# merge_sorted_two_lists(f_list, s_list)
# print(time.time() - start_time)
#
# start_time = time.time()
#
# merge_sorted_two_lists_faster(f_list, s_list)
# print(time.time() - start_time)
