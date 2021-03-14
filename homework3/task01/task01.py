from functools import wraps
from typing import Callable


def cache(times: int):
    cacher = dict()

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper():
            if func.__name__ not in cacher:
                cacher[func.__name__] = [func(), times]
            else:
                if cacher[func.__name__][1] == 0:
                    del cacher[func.__name__]
                    return func()
                cacher[func.__name__][1] -= 1

            return cacher[func.__name__][0]

        return wrapper

    return decorator


@cache(times=2)
def f():
    return input("? ")
