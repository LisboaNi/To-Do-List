import os
from tornado import ioloop, httpserver
from tornado.web import Application

from controllers.controller_task import All, Created, Updated, Deleted

class RunApp(Application):

    def __init__(self):
        handlers = [
            ('/', All),
            ('/task/create', Created),
            (r'/task/update/(\d+)', Updated),
            (r'/task/update/(\d+)/status/(\w+)', Updated),
            (r'/task/delete/(\d+)', Deleted),
        ]

        settings = dict (
            debug = True,
            template_path = 'views',
            static_path =  'static'
        )

        super().__init__(handlers, **settings)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(port)

    print("[Server] Server running successfully")
    print("[Server] Port: http://localhost:5000/")

    try:
        ioloop.IOLoop.current().start()

    except KeyboardInterrupt:
        print("[Server] Server stopped")
