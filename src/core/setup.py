from core.database import _execute

class Setup:
    table_name = None

    @classmethod
    def setup(cls):
        if not cls.table_name:
            raise ValueError("Define the table in the template!")

        from core.database import _execute
        query = cls.create_table()
        _execute(query)

        print(f"[SETUP]'{cls.table_name}' table created/updated successfully")