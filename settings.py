from decouple import config


DATABASE_NAME = config('DATABASE_NAME', default='pay')
DATABASE_URI = config('DATABASE_URI', default='mongodb://localhost:27017')

JWT_SECRET = config(
    'JWT_SECRET',
    default='SOMESECRET'
)

ALGORITHM_SCHEMES = [
    "django_argon2",
    "django_pbkdf2_sha256",
    "django_pbkdf2_sha1",
    "md5_crypt",
    "django_bcrypt_sha256"
]

ALGORITHM_ROUNDS = 12

ACCESS_TOKEN_EXPIRITY_TIME = config('ACCESS_TOKEN_EXPIRITY_TIME', default=(60 * 60))
