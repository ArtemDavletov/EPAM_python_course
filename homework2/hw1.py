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
    with open(file_path) as file:
        lines = []
        for line in file:
            lines += line.strip().split()

    return sorted(lines, key=lambda x: len(x) and len(Counter(x)), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path) as file:
        chars: dict = Counter(file)
        return min(chars.items(), key=(lambda key: chars[key]))


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path) as file:
        lines: List[List[str]] = [line.strip().split() for line in file]
        punct: set = set(string.punctuation)
        counter: int = 0

        for line in lines:
            for el in line:
                if el in punct:
                    counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path) as file:
        lines: List[List[str]] = [line.strip().split() for line in file]
        ascii_letters: set = set(string.ascii_letters)
        counter: int = 0

        for line in lines:
            for el in line:
                if el not in ascii_letters:
                    counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path) as file:
        lines: List[List[str]] = [line.strip().split() for line in file]
        ascii_letters: set = set(string.ascii_letters)
        non_ascii_characters: dict = dict()

        for line in lines:
            for el in line:
                if el not in ascii_letters:
                    if el in non_ascii_characters:
                        non_ascii_characters[el] += 1
                    else:
                        non_ascii_characters[el] = 1

    return max(non_ascii_characters.items(), key=(lambda key: non_ascii_characters[key]))
