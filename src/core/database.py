import sqlite3

import os
import sqlite3

DB_PATH = os.environ.get("DB_PATH", "./data/sqlite3.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def _execute(query, params=None):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    result = None

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
    except Exception as err:
        print(f'Error executing query: {err}')

    connection.close()

    return result