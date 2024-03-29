"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional

DIR_PATH = Path(__file__).parent


def count_len(tokens):
    try:
        if isinstance(tokens, str):
            return 1
        return len(tokens)
    except TypeError:
        return 1


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0

    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            with open(dir_path / file) as file_read:
                if tokenizer is None:
                    counter += len(file_read.readlines())
                else:
                    counter += sum(count_len(tokenizer(line)) for line in file_read.readlines())

    return counter
