from pathlib import Path

import pytest

from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars, get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)

TEST_DATA_PATH = Path(__file__).parent / "data.txt"


@pytest.mark.trylast
def test_get_longest_diverse_words(file_path: Path = TEST_DATA_PATH):
    assert set(get_longest_diverse_words(file_path)) == {
        "Bevölkerungsabschub,",
        "Kollektivschuldiger,",
        "résistance-Bewegungen,",
        "Schicksalsfiguren;",
        "unmißverständliche",
        "politisch-strategischen",
        "Entscheidungsschlacht.",
        "Werkstättenlandschaft",
        "Gewissenserforschung,",
        "Seinsverdichtungen,",
    }, f"[get_longest_diverse_words] Incorrect answer for file: {file_path}"


@pytest.mark.trylast
def test_get_rarest_char(file_path: Path = TEST_DATA_PATH):
    assert get_rarest_char(file_path) == ")", f"[get_rarest_char] Correct answer for file {file_path} is ')'"


@pytest.mark.trylast
def test_count_punctuation_chars(file_path: Path = TEST_DATA_PATH):
    assert (
        count_punctuation_chars(file_path) == 5305
    ), f"[count_punctuation_chars] Correct answer for file {file_path} is 8277"


@pytest.mark.trylast
def test_count_non_ascii_chars(file_path: Path = TEST_DATA_PATH):
    assert (
        count_non_ascii_chars(file_path) == 2972
    ), f"[count_non_ascii_chars] Correct answer for file {file_path} is 54661"


@pytest.mark.trylast
def test_get_most_common_non_ascii_char(file_path: Path = TEST_DATA_PATH):
    assert (
        get_most_common_non_ascii_char(file_path) == "ä"
    ), f"[get_most_common_non_ascii_char] Correct answer for file {file_path} is 'ä'"
