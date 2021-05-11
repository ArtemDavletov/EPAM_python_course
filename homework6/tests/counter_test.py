from homework6.counter import instances_counter


def test_get_empty_instances():
    class Test:
        pass

    decorated_class = instances_counter(Test)
    assert decorated_class.get_created_instances() == 0


def test_reset_instances():
    class Test:
        pass

    decorated_class = instances_counter(Test)
    _ = decorated_class(), decorated_class(), decorated_class()
    assert decorated_class.reset_instances_counter() == 3


def test_get_instances():
    class Test:
        pass

    decorated_class = instances_counter(Test)
    mock, _, _ = decorated_class(), decorated_class(), decorated_class()
    assert mock.get_created_instances() == 3


def test_get_instances_for_many_classes():
    class Test:
        pass

    class Test2:
        pass

    decorated_class = instances_counter(Test)
    decorated_class2 = instances_counter(Test2)

    mock, _, _ = decorated_class(), decorated_class(), decorated_class()
    mock2, _ = decorated_class2(), decorated_class2()

    assert mock.get_created_instances() == 3
    assert mock2.get_created_instances() == 2


def test_instances_after_reset():
    class Test:
        pass

    decorated_class = instances_counter(Test)
    _ = decorated_class(), decorated_class(), decorated_class()
    decorated_class.reset_instances_counter()
    assert decorated_class.get_created_instances() == 0
