from unittest.mock import Mock

from homework5.save_original_info import print_result


def set_custom_sum_mock():
    custom_sum = Mock(return_value=10)
    custom_sum.__doc__ = """Docstring"""
    custom_sum.__name__ = "custom_sum"
    return custom_sum


def test_custom_sum_doc():
    custom_sum = set_custom_sum_mock()
    decorated_custom_sum = print_result(custom_sum)

    assert decorated_custom_sum.__doc__ == custom_sum.__doc__


def test_custom_sum_name():
    custom_sum = set_custom_sum_mock()
    decorated_custom_sum = print_result(custom_sum)

    assert decorated_custom_sum.__name__ == custom_sum.__name__ == "custom_sum"


def test_custom_sum_original_func():
    custom_sum = set_custom_sum_mock()
    decorated_custom_sum = print_result(custom_sum)

    assert decorated_custom_sum.__original_func() == custom_sum() == 10


def test_custom_sum_stdout(capsys):
    custom_sum = set_custom_sum_mock()
    decorated_custom_sum = print_result(custom_sum)
    result = str(decorated_custom_sum(1, 2, 3))

    captured = capsys.readouterr()
    stdout = str(captured.out).strip()

    assert result == stdout
