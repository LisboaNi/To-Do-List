from tornado.web import RequestHandler
from datetime import datetime

from models.model_task import Task
from utils.get_error import get_task

class All(RequestHandler):

    def get(self):
        tasks = Task.all()
        self.render('task/index.html', tasks = tasks)

class Created(RequestHandler):

    def get(self):
        self.render('task/create.html')
    
    def post(self):
        description = self.get_argument('description', None)
        term = self.get_argument('term', None)

        task = Task(description=description, term=term)
        task.save()

        self.redirect('/')

class Updated(RequestHandler):

    def get(self, id):
        task = get_task(id) 
        self.render('task/update.html', task=task)
    
    def post(self, id):
        task = get_task(id)

        description = self.get_argument('description', task.description)
        term = self.get_argument('term', task.term)
        status = self.get_argument('status', task.status)

        task.description = description
        task.term = term
        task.status = status
        task.save()

        self.redirect('/')

class Deleted(RequestHandler):

    def get(self, id):
        task = get_task(id)   
        task.deleted()
    
        self.redirect('/')

class Term(RequestHandler):

    def get(self, id):
        task = get_task(id) 
        
        if self.term < datetime.now():
            task.mark_pending()