"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from pathlib import Path
from typing import List


def get_longest_diverse_words(file_path: Path) -> List[str]:
    def collect_words(lines) -> set:
        return {el for line in lines for el in line.strip().split()}

    with open(file_path, "r", encoding="unicode-escape") as file:
        words = collect_words(file)

    return sorted(words, key=lambda x: (len(x), len(set(x))), reverse=True)[:10]


def get_rarest_char(file_path: Path) -> str:
    with open(file_path, encoding="unicode-escape") as file:
        chars: Counter = Counter(char for line in file for char in line)
        return min(chars.items(), key=(lambda key: chars[key]))[0]


def count_punctuation_chars(file_path: Path) -> int:
    with open(file_path, encoding="unicode-escape") as file:
        # punctuation characters aren't in the order https://u.to/P4QpGw
        punct: set = set(string.punctuation)
        return sum(el in punct for line in file for el in line)


def count_non_ascii_chars(file_path: Path) -> int:
    with open(file_path, encoding="unicode-escape") as file:
        # Also I found method .isascii() for strings, so we also can write with it
        # return sum(not el.isascii() for line in file for el in line)
        return sum(ord(el) >= 128 for line in file for el in line)


def get_most_common_non_ascii_char(file_path: Path) -> str:
    with open(file_path, encoding="unicode-escape") as file:
        # I like this solution 😊
        return Counter(el for line in file for el in line if not el.isascii()).most_common(n=1)[0][0]
