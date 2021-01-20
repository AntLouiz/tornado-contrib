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


JWT_SECRET = config('JWT_SECRET', '123')
ACCESS_TOKEN_EXPIRITY_TIME = config('ACCESS_TOKEN_EXPIRITY_TIME', 60*5)
ALGORITHM_SCHEMES = [
    "django_argon2",
    "django_pbkdf2_sha256",
    "django_pbkdf2_sha1",
    "md5_crypt",
    "django_bcrypt_sha256"
]
