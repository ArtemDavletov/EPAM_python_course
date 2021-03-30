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


def test_instances_after_reset():
    class Test:
        pass

    decorated_class = instances_counter(Test)
    _ = decorated_class(), decorated_class(), decorated_class()
    decorated_class.reset_instances_counter()
    assert decorated_class.get_created_instances() == 0
