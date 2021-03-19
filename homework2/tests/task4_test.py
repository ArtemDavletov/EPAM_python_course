from random import randint
from unittest.mock import MagicMock

import pytest

from homework2.hw4 import cache


@pytest.mark.trylast
def test_cache_func():
    some = (randint(0, 1000), randint(0, 1000))
    func = MagicMock()
    cache_func = cache(func)
    cache_func(*some)
    cache_func(*some)
    func.assert_called_once()
