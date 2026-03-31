import jwt

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
