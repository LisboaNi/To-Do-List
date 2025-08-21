import sqlite3

def _execute(query, params=None):
    db_path = './sqlite3'
    connection = sqlite3.connect(db_path)
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