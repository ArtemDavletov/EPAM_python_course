from unittest.mock import MagicMock

from homework11.hw2 import Order


def test_final_price_once():
    morning_discount = MagicMock(return_value=0)
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 100


def test_final_price_twice():
    morning_discount = MagicMock(return_value=50)
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    elder_discount = MagicMock(return_value=90)
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
