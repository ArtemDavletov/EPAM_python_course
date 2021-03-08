import pytest

from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars, get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)


@pytest.mark.trylast
def test_get_longest_diverse_words(file_path: str = "tests/data.txt"):
    assert get_longest_diverse_words(file_path) == [
        "Bev\\u00f6lkerungsabschub,",
        "unmi\\u00dfverst\\u00e4ndliche",
        "Werkst\\u00e4ttenlandschaft",
        "Machtbewu\\u00dftsein,",
        "Selbstverst\\u00e4ndlich",
        "Entz\\u00fcndbarkeit.",
        "Werkst\\u00e4ttenlandschaft",
        "r\\u00e9sistance-Bewegungen,",
        "Zahlenverh\\u00e4ltnis-",
        "\\u00fcberw\\u00e4ltigend",
    ], f"[get_longest_diverse_words] Incorrect answer for file: {file_path}"


@pytest.mark.trylast
def test_get_rarest_char(file_path: str = "tests/data.txt"):
    assert get_rarest_char(file_path) == "E", f"[get_rarest_char] Correct answer for file {file_path} is 'E'"


@pytest.mark.trylast
def test_count_punctuation_chars(file_path: str = "tests/data.txt"):
    assert (
        count_punctuation_chars(file_path) == 8277
    ), f"[count_punctuation_chars] Correct answer for file {file_path} is 8277"


@pytest.mark.trylast
def test_count_non_ascii_chars(file_path: str = "tests/data.txt"):
    assert (
        count_non_ascii_chars(file_path) == 54661
    ), f"[count_non_ascii_chars] Correct answer for file {file_path} is 54661"


@pytest.mark.trylast
def test_get_most_common_non_ascii_char(file_path: str = "tests/data.txt"):
    assert (
        get_most_common_non_ascii_char(file_path) == " "
    ), f"[get_most_common_non_ascii_char] Correct answer for file {file_path} is ' '"
