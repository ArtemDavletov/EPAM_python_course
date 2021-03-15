from typing import Any, Tuple
from unittest.mock import MagicMock

import pytest

from homework2.hw4 import cache


@pytest.mark.parametrize("some", [(100, 200), (1, 1), (0, 1)])
def test_cache_func(some: Tuple[Any, Any]):
    func = MagicMock()
    cache_func = cache(func)
    cache_func(*some)
    func.assert_called_once()

    func = MagicMock()
    cache_func = cache(func)
    func = MagicMock()
    cache_func(*some)
    func.assert_not_called()
