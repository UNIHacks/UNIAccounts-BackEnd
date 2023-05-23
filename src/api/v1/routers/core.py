# External Packages
from flask import Blueprint, request

import config.base as CONFIG
from tools.functions_authentication import valid_headers

from ..views.core import signin_route_PUT, validate_token_route_GET

views_core = Blueprint("core", __name__)


@views_core.route("/", methods=["GET"])
def index():
    """Respond with the API documentation

    Returns:
        str: API Documentation
    """
    api_docs = open(f"templates/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()


@views_core.route("/api/v1/signin", methods=["PUT"])
def signin():
    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "PUT":
        response = signin_route_PUT(request=request)
        return response


@views_core.route("/api/v1/validate_token", methods=["GET"])
def validate_token():
    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "GET":
        response = validate_token_route_GET(request=request)
        return response


@views_core.route("/test", methods=["GET"])
def test():
    """Test Route

    Returns:
        str:
    """
    return "Hello World!!!"
