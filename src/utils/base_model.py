from core.database import _execute
from datetime import datetime
from typing import Optional

class BaseModel:

    table_name = None

    def __init__(self):
        self.id = id
        self.created_at = datetime.now()
        self.uptaded_at = datetime.now()
        self.deleted_at = Optional[datetime] = None
    
    base_fields = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "updated_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        "deleted_at": "TIMESTAMP NULL"
    }

    @classmethod
    def create_table(cls):
        if not cls.table_name:
            raise ValueError("Define the table in the template!")

        all_fields = {**cls.base_fields, **cls.fields}
        columns = ", ".join([f"{name} {type_}" for name, type_ in all_fields.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({columns});"
        return query

    def uptaded(self):
        if not self.table_name:
            raise ValueError("Define the table in the template!")
        
        self.uptaded_at = datetime.now()
        
        query = (f'UPDATE {self.table_name} SET uptaded_at= ? WHERE id=?')
        _execute(query, self.uptaded_at, self.id)


    def deleted(self):
        if not self.table_name:
            raise ValueError("Define the table in the template!")

        self.deleted_at = datetime.now() 

        query = f"UPDATE {self.table_name} SET deleted_at = ? WHERE id = ?"
        _execute(query, (self.deleted_at, self.id))