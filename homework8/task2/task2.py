import sqlite3
from pathlib import Path

TEST_DB_PATH = Path(__file__).parent / "example.sqlite"


class TableData:
    def __init__(self, database_name, table_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

        self.tablenames = tuple(map(lambda x: x[1], self.cursor.execute(f"PRAGMA table_info({table_name})").fetchall()))

    def __len__(self):
        self.cursor.execute(f"SELECT COUNT(name) FROM {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        try:
            self.cursor.execute(f'SELECT * FROM {self.table_name} WHERE {self.table_name}.name == "{item}"')
            return self.cursor.fetchone()
        except sqlite3.OperationalError as e:
            raise AttributeError from e

    def __contains__(self, item):
        return (
            item
            in self.cursor.execute(
                f'SELECT * FROM {self.table_name} WHERE {self.table_name}.name == "{item}"'
            ).fetchone()
        )

    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for i in self.cursor.fetchall():
            yield dict(zip(self.tablenames, i))


presidents = TableData(database_name=TEST_DB_PATH, table_name="presidents")

print(len(presidents))
print(presidents["Yeltsin"])
print("Yeltsin" in presidents)

for president in presidents:
    print(president["name"])
