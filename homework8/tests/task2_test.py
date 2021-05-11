from homework8.task2.task2 import TEST_DB_PATH, TableData


def test_len():
    presidents = TableData(database_name=TEST_DB_PATH, table_name="presidents")
    assert len(presidents) == 3


def test_get_item():
    presidents = TableData(database_name=TEST_DB_PATH, table_name="presidents")
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains():
    presidents = TableData(database_name=TEST_DB_PATH, table_name="presidents")
    assert ("Yeltsin" in presidents) is True


def test_iterable():
    presidents = TableData(database_name=TEST_DB_PATH, table_name="presidents")
    for president in presidents:
        assert president["name"] in ("Yeltsin", "Trump", "Big Man Tyrone")
