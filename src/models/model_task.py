from core.database import _execute
from utils.base_model import BaseModel

class Task(BaseModel):

    table_name = "task"

    def __init__(self, description, term, status = "Progress"):
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
        return super().uptaded()
    
    def deleted(self):
        return super().deleted()
    
    def mark_completed(self):
        self.status = "Completed"
        self.save()  

    def mark_pending(self):
        self.status = "Pending"
        self.save()

    def mark_progress(self):
        self.status = "Progress"
        self.save()
    
    @classmethod
    def all(self):
        query = (f"SELECT * FROM {self.table_name} WHERE deleted_at IS NULL")
        tasks = _execute(query)
        return tasks
    
    @classmethod
    def task(self, id):
        query = (f"SELECT id, description, term, status FROM {self.table_name} WHERE id= ?")
        task = _execute(query, (id))[0]
        task = Task(id=task[0], description=task[1], term=task[2], status=task[3])
        return task