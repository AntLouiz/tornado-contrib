import unittest
from tornado.ioloop import IOLoop
from app import create_app


if __name__ == '__main__':
    app = create_app()
    port = 8888
    app.listen(port)
    IOLoop.current().start()
