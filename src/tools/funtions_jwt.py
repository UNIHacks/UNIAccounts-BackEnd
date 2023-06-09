######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 10/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# System Packages
from datetime import datetime, timedelta

# External Packages
from jwt import encode, decode, exceptions

# Local Packages
import ENVS


def expire_date(days: int):
    """Generates a date and from the current date plus the indicated days 

    Args:
        days (int):

    Returns:
        date: new Date
    """
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date


def write_token(data: dict):
    """Generates a token using the selected dict as a base

    Args:
        data (dict): Object that will be used to generate the token

    Returns:
        bytes: token generated
    """
    token = encode(payload={**data, "exp": expire_date(2)},
                   key=ENVS.SECRET_KEY_TOKEN, algorithm="HS256")
    return token.encode("UTF-8")


def validate_token(token: str):
    """Validate if a token still expires and if it was created by the application

    Args:
        token (str): Token To evaluate

    Returns:
        dict: response of func
    """
    try:
        return {"message": "Valid Token", "user": decode(token, key=ENVS.SECRET_KEY_TOKEN, algorithms=["HS256"])}
    except exceptions.DecodeError:
        response = {"message": "Invalid Token", 'user': ''}
        return response
    except exceptions.ExpiredSignatureError:
        response = {"message": "Token Expired", 'user': ''}
        return response