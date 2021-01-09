import unittest
from tornado.ioloop import IOLoop
from app import create_app
from settings import logger


if __name__ == '__main__':
    app = create_app()
    port = 8888
    logger.info(f'Listening on port {port} ...')
    app.listen(port)
    IOLoop.current().start()
