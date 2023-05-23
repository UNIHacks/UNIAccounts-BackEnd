# External Packages
from flask import Blueprint, request

from tools.functions_authentication import valid_headers

from ..views.users import signup_route_POST

views_users = Blueprint("users", __name__)


@views_users.route("/api/v1/signup", methods=["POST"])
def signup():
    """SignUp EndPoint

    Returns:
        dict: JSON response
        int: status code of the request
    """

    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "POST":
        response = signup_route_POST(parameters_json=request.get_json())
        return response
