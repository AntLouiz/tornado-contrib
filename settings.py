import sys
import logging
import os.path
from decouple import config


BASE_DIR = os.path.dirname(__file__)
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

DEBUG = config('DEBUG', default=True)

level = logging.INFO

if DEBUG:
    level = logging.DEBUG

logging.basicConfig(filename=os.path.join(LOGS_DIR, 'app.log'), filemode='a', level=level)
logger = logging.getLogger()

logging.getLogger('asyncio').setLevel(logging.WARNING)
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stdout_handler)

DATABASE_URI = 'mongodb://localhost:27017'
DATABASE_NAME = 'core'
