from random import randint

import pytest

from homework3.task01.task01 import cache


@pytest.mark.parametrize(
    "times",
    [2, 5, 10],
)
def test_cache(times: int):
    @cache(times=times)
    def f():
        return randint(0, 10000)

    f_prev = f()

    for i in range(times):
        f_curr = f()
        assert f_curr is f_prev
        f_prev = f_curr

    f_curr = f()
    assert not (f_prev is f_curr)
