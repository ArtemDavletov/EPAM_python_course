from pathlib import Path

import pytest

from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars, get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)

TEST_DATA_PATH = Path(__file__).parent / "data.txt"


@pytest.mark.trylast
def test_get_longest_diverse_words(file_path: Path = TEST_DATA_PATH):
    assert get_longest_diverse_words(file_path) == [
        "unmi\\u00dfverst\\u00e4ndliche",
        "r\\u00e9sistance-Bewegungen,",
        "Wiederbelebungs\\u00fcbungen",
        "unver\\u00e4u\\u00dferlichen,",
        "\\u00bbWaldg\\u00e4nger\\u00ab",
        "Werkst\\u00e4ttenlandschaft",
        "Werkst\\u00e4ttenlandschaft",
        "Br\\u00fcckenschl\\u00e4gen;",
        "Souver\\u00e4nit\\u00e4tsan-",
        "Meinungs\\u00e4u\\u00dferung",
    ], f"[get_longest_diverse_words] Incorrect answer for file: {file_path}"


@pytest.mark.trylast
def test_get_rarest_char(file_path: Path = TEST_DATA_PATH):
    assert get_rarest_char(file_path) == "E", f"[get_rarest_char] Correct answer for file {file_path} is 'E'"


@pytest.mark.trylast
def test_count_punctuation_chars(file_path: Path = TEST_DATA_PATH):
    assert (
            count_punctuation_chars(file_path) == 8277
    ), f"[count_punctuation_chars] Correct answer for file {file_path} is 8277"


@pytest.mark.trylast
def test_count_non_ascii_chars(file_path: Path = TEST_DATA_PATH):
    assert (
            count_non_ascii_chars(file_path) == 168762
    ), f"[count_non_ascii_chars] Correct answer for file {file_path} is 54661"


@pytest.mark.trylast
def test_get_most_common_non_ascii_char(file_path: Path = TEST_DATA_PATH):
    assert (
            get_most_common_non_ascii_char(file_path) == "e"
    ), f"[get_most_common_non_ascii_char] Correct answer for file {file_path} is ' '"
