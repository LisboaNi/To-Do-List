from core.database import _execute
from models.model_task import Task

query = Task.create_table()
_execute(query)