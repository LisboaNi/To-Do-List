from core.database import _execute
from utils.base_model import BaseModel

class Task(BaseModel):

    table_name = "task"

    def __init__(self, description, term, status="Progress"):
        super().__init__()

        self.description = description
        self.term = term
        self.status = status
    
    fields = {
        "description": "TEXT NOT NULL",
        "term": "TIMESTAMP NOT NULL",
        "status": "TEXT NOT NULL"
    }

    def save(self):
        query = (f"INSERT INTO {self.table_name} (description, term, status) VALUES (?,?,?)")
        _execute(query, (self.description, self.term, self.status))
    
    def deleted(self):
        return super().deleted()
    
    def updated(self):
        query = (f"UPDATE {self.table_name} SET description=?, term=?, status=? WHERE id=?")
        _execute(query, (self.description, self.term, self.status, self.id))
        return super().updated()
    
    def mark_pending(self):
        self.status = "Pending"
        self.save()
    
    @classmethod
    def all(self):
        query = (f"SELECT id, description, term, status, created_at, updated_at FROM {self.table_name} WHERE deleted_at IS NULL")
        tasks = _execute(query)
        return tasks
    
    @classmethod
    def task(self, id):
        query = (f"SELECT id, description, term, status FROM {self.table_name} WHERE id= ?")
        row = _execute(query, (id))[0]
        task = Task(description=row[1], term=row[2], status=row[3])
        task.id = row[0]
        return task

Task.setup()