import os
import sys

from decouple import AutoConfig

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

LIST_PATH_TO_ADD = [BASE_DIR]
sys.path.extend(LIST_PATH_TO_ADD)


# IMPORT ENVIRONMENT VARIABLES
PATH_FILE_ENV = os.path.join(BASE_DIR, "config")
config = AutoConfig(search_path=PATH_FILE_ENV)


ENVIRONMENT = config("ENVIRONMENT")
SECRET_KEY_TOKEN = config("SECRET_KEY_TOKEN")
API_KEYS = None
API_VERSION = "v1"
UNIACCOUNT_NAME = "uniaccount"
TOKEN_TYPE = "JWT"

SERVICE_PERMISSIONS = {
    "UNICA_STORE": [
        "signup_route_POST",
        "signin_route_PUT",
        "signin_route_GET",
        "signout_route_PUT",
    ],
    "UNICA_MANAGER_ACCOUNTS": [
        "signup_route_POST",
        "signin_route_PUT",
        "signin_route_GET",
        "signout_route_PUT",
    ],
}

PORT = 5000

DEBUG = True

HOST = "0.0.0.0"


if ENVIRONMENT == "local":
    from config.local import *
elif ENVIRONMENT == "development":
    from config.development import *
elif ENVIRONMENT == "production":
    from config.production import *
else:
    raise ValueError("Debes especificar una variable de entorno ENVIRONMENT valida.")


SMTP_HOST = 'smtp.office365.com'
SMTP_PORT = 587
SMTP_USER = config("SMTP_USER")
SMTP_PASSWORD = config("SMTP_PASSWORD")