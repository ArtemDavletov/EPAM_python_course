from typing import Any, Tuple

import pytest

from homework2.hw4 import cache


@pytest.mark.parametrize("some", [(100, 200), (1, 1), (0, 1)])
def test_get_most_common_non_ascii_char(some: Tuple[Any, Any]):
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2, "Cache function is incorrect"
