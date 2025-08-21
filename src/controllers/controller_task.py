from tornado.web import RequestHandler
from datetime import datetime

from models.model_task import Task
from utils.get_error import get_task

class All(RequestHandler):

    def get(self):
        tasks = Task.all()

        for i, task in enumerate(tasks):
            date_obj = datetime.strptime(task[2], "%Y-%m-%d").date()
            tasks[i] = (task[0], task[1], date_obj, task[3])

        self.render('task/index.html', tasks = tasks, now=datetime.now().date())

class Created(RequestHandler):

    def get(self):
        self.render('task/form.html', task=None)
    
    def post(self):
        description = self.get_argument('description', None)
        term = self.get_argument('term', None)

        task = Task(description=description, term=term)
        task.save()

        self.redirect('/')

class Updated(RequestHandler):

    def get(self, id, status=None):
        task = get_task(id) 
        if status:
            if status in ["Progress", "Completed", "Pending"]:
                task.status = status
                task.updated()
            
            self.redirect('/')
        else:
            self.render('task/form.html', task=task)
    
    def post(self, id):
        task = get_task(id)

        description = self.get_argument('description', task.description)
        term = self.get_argument('term', task.term)
        status = self.get_argument('status', task.status)

        task.description = description
        task.term = term
        task.status = status
        task.updated()

        self.redirect('/')

class Deleted(RequestHandler):

    def get(self, id):
        task = get_task(id)   
        task.deleted()
    
        self.redirect('/')