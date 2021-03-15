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
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            lines += line.strip().split()

    return sorted(lines, key=lambda x: (len(x), len(Counter(x))), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as file:
        chars: dict = Counter("".join(file))
        return min(chars.items(), key=(lambda key: chars[key]))[0]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="utf-8") as file:
        punct: set = set(string.punctuation)
        counter: int = 0

        for line in file:
            for el in line:
                if el in punct:
                    counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="utf-8") as file:
        # file.read().decode("UTF-8")
        ascii_chars: set = set(chr(i) for i in range(128))
        counter: int = 0

        for line in file:
            for el in "".join(line.split()).encode("UTF-8"):
                if el not in ascii_chars:
                    counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as file:
        ascii_chars: set = set(chr(i) for i in range(128))
        non_ascii_characters: dict = dict()

        for line in file:
            for el in line:
                if el not in ascii_chars:
                    if el in non_ascii_characters:
                        non_ascii_characters[el] += 1
                    else:
                        non_ascii_characters[el] = 1

    return max(non_ascii_characters.items(), key=(lambda key: non_ascii_characters[key[0]]))[0]


count_non_ascii_chars("tests/data.txt")
