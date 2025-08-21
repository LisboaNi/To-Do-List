from tornado.web import HTTPError

from models.model_task import Task

def get_task(id):
    task = Task.task(id)
    if not task:
        raise HTTPError(404, "Task not found")
    return task
