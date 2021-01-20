import settings
from passlib.context import CryptContext


if settings:
    from settings import ALGORITHM_SCHEMES
else:
    ALGORITHM_SCHEMES = [
        "django_argon2",
        "django_pbkdf2_sha256",
        "django_pbkdf2_sha1",
        "md5_crypt",
        "django_bcrypt_sha256"
    ]


hash_context = CryptContext(
    schemes=ALGORITHM_SCHEMES,
    default=ALGORITHM_SCHEMES[0]
)


def hash_password(password):
    """
    Doesn't work to set the kwds settings, but i don't know why

    encrypted_salt = hash_context.hash(PASSWORD_SALT)

    settings = {
        'rounds': ALGORITHM_ROUNDS,
        'salt': encrypted_salt
    }
    password = hash_context.using(**settings).hash(password)
    """

    encrypted_password = hash_context.hash(password)

    return encrypted_password


def verify_password(password, encrypted_password):
    password_is_valid = hash_context.verify(
        password.encode('utf-8').decode('utf-8'),
        encrypted_password
    )

    return password_is_valid
