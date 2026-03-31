import jwt
import bcrypt

from core.config import settings


def encode(
    payload: dict,
    key: str = settings.authentication.private_key_path.read_text(),
    algorithm: str = settings.authentication.algorithm,
):
    encoded = jwt.encode(
        payload,
        key,
        algorithm=algorithm,
    )
    return encoded


def decode(
    token: str | bytes,
    key: str = settings.authentication.public_key_path.read_text(),
    algorithm: str = settings.authentication.algorithm,
):
    decoded = jwt.decode(
        token,
        key,
        algorithms=[algorithm],
    )
    return decoded


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
