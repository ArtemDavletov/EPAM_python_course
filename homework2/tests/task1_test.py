import pytest

from homework2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.trylast
def test_get_longest_diverse_words(file_path: str = "tests/data.txt"):
    assert get_longest_diverse_words(file_path) == [
        "schw\\u00e4chen,ihrebl\\u00f6\\u00dfen,ihreentz\\u00fcndbarkeit.erverf\\u00fcgt",
        "raubsichsichernwill.l\\u00e4ngst\\u00fcbers\\u00e4ttigt,fri\\u00dfterimmerneu-",
        "diemanf\\u00fcrr\\u00fcckst\\u00e4ndigh\\u00e4lt.dasgeh\\u00f6rtindaskapitelder",
        "\\u00bbl'homme,dansl'\\u00e9tatactueldelasoci\\u00e9t\\u00e9,mepara\\u00eetplus",
        "da\\u00dferdiema\\u00dfederf\\u00fcreinek\\u00fcnftigeepocheg\\u00fcltigenfrei-",
        "ferner,da\\u00dff\\u00fcrstenfehlenundda\\u00dfdiem\\u00e4chtigenalle\\u00fcber",
        "zugew\\u00f6hnen,da\\u00dfwiderstand\\u00fcberhauptm\\u00f6glichist\\u2014ist",
        "diefallensind.zun\\u00e4chstw\\u00e4rennocheinigemi\\u00dfverst\\u00e4ndnis-",
        "nenderkolo\\u00dfgef\\u00e4hrdetist.manmu\\u00dfn\\u00e4mlichwissen,da\\u00df",
        "ihmanheimf\\u00e4llt,vergr\\u00f6\\u00dfertdashinterland.ermu\\u00dfzugleich",
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
        count_non_ascii_chars(file_path) == 0
    ), f"[count_non_ascii_chars] Correct answer for file {file_path} is 54661"


@pytest.mark.trylast
def test_get_most_common_non_ascii_char(file_path: str = "tests/data.txt"):
    assert (
        get_most_common_non_ascii_char(file_path) == " "
    ), f"[get_most_common_non_ascii_char] Correct answer for file {file_path} is ' '"
