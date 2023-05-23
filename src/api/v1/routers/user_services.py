# External Packages
from flask import Blueprint, request

from tools.functions_authentication import valid_headers

from ..views.user_services import signup_service_route_POST

views_user_services = Blueprint("user_services", __name__)


@views_user_services.route("/api/v1/signup_service", methods=["POST"])
def signup_service():
    """SignUp EndPoint

    Returns:
        dict: JSON response
        int: status code of the request
    """

    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "POST":
        response = signup_service_route_POST(request=request)
        return response
