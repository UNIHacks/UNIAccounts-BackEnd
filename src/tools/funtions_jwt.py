# System Packages
from datetime import datetime, timedelta

# External Packages
from jwt import decode, encode, exceptions

# Local Packages
import config.base as CONFIG


def expire_date(minutes: int):
    """Generates a date and from the current date plus the indicated minutes

    Args:
        minutes (int): The number of minutes until the token should expire

    Returns:
        datetime: The expiration date of the token
    """
    now = datetime.utcnow()  # Obtén la hora actual en UTC
    expiration_date = now + timedelta(minutes=minutes)
    return expiration_date


def write_token(data: dict, minutes_until_expire: int = 120):
    token = encode(
        payload={**data, "exp": expire_date(minutes_until_expire)},
        key=CONFIG.SECRET_KEY_TOKEN,
        algorithm="HS256",
    )
    return token


def validate_token(token: str):
    """Validate if a token still expires and if it was created by the application

    Args:
        token (str): Token To evaluate

    Returns:
        dict: response of func
    """

    token_is_valid = False
    response = None
    try:
        response = decode(token, key=CONFIG.SECRET_KEY_TOKEN, algorithms=["HS256"])
        token_is_valid = True
    except exceptions.DecodeError:
        response = "Invalid Token"
    except exceptions.ExpiredSignatureError:
        response = "Token Expired"
    return token_is_valid, response
