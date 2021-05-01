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
from typing import Generator, Iterable, Iterator, List, Union


def lines_from_file_generator(file) -> Iterable:
    yield from (int(line) for line in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(file)) for file in file_list]

        yield from merge_sorted_lists_gen(list(map(lines_from_file_generator, files)))


def merge_sorted_lists_gen(generators) -> Generator[int, None, None]:
    iteration = []
    for gen in generators:
        try:
            iteration.append(next(gen))
        except StopIteration:
            generators.remove(gen)

    while generators:
        min_val = min(iteration)
        min_index = iteration.index(min_val)

        yield min_val
        try:
            iteration[min_index] = next(generators[min_index])
        except StopIteration:
            iteration.remove(min_val)
            generators.remove(generators[min_index])
