from pathlib import Path

TEST_DATA_PATH = Path(__file__).parent / "task1.txt"


class KeyValueStorage:
    def __init__(self, path):
        with open(path, "r") as file:
            for line in file:
                key, val = line.rstrip("\n").split("=", 1)
                try:
                    val = int(val)
                except ValueError:
                    ...
                self.__setattr__(key, val)

    def __getitem__(self, item):
        if item not in self.__dict__:
            raise AttributeError
        return self.__dict__[item]


storage = KeyValueStorage(TEST_DATA_PATH)
print(storage.__dict__)
print(storage["name"])
