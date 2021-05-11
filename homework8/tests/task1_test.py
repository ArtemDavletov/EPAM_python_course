from homework8.task1.task1 import TEST_DATA_PATH, KeyValueStorage


def test_key_value_storage():
    storage = KeyValueStorage(TEST_DATA_PATH)
    assert storage.__dict__ == {"name": "kek", "last_name": "top", "power": 9001, "song": "shadilay", "sss": 555}


def test_key_value_storage_get_item():
    storage = KeyValueStorage(TEST_DATA_PATH)
    assert storage.name == storage["name"] == "kek"


def test_key_value_storage_get_item_int():
    storage = KeyValueStorage(TEST_DATA_PATH)
    assert storage.sss == storage["sss"] == 555
