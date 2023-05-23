# Local Packages
from http import HTTPStatus

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

import config.base as CONFIG
from tools.funtions_jwt import write_token

from ..schemas import UserServicesSchema
from ..services.user_services import UserServicesService
from ..services.users import UserService
from ..views.core import validate_token_route_GET


def signup_service_route_POST(request):

    response, status_code = validate_token_route_GET(request=request)

    if not response["Success"]:
        return response, status_code

    else:
        token_user_name = response["Data"]["user_name"]
        token_service_name = response["Data"]["service_name"]
        if not token_service_name == CONFIG.UNIACCOUNT_NAME:
            response = {
                "Success": False,
                "Message": "Insufficient Permissions",
                "Data": None,
            }
            return response, HTTPStatus.UNAUTHORIZED

    service = CONFIG.API_KEYS[request.headers.get("Service")]

    if service.name == CONFIG.UNIACCOUNT_NAME:
        response = {
            "Success": False,
            "Message": "Don't its posible created user_service uniaccount beacause already exist",
            "Data": None,
        }
        return response, HTTPStatus.BAD_REQUEST

    parameters_json = request.get_json()
    user_service = UserService()
    user_services_service = UserServicesService()
    user = user_service.get_user_by_user_name(user_name=token_user_name)
    user_services_schema = None

    if not service.mother_login:
        try:
            user_services_schema = UserServicesSchema(**parameters_json)
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append({"field": error["loc"][0], "message": error["msg"]})
            response = {
                "Success": False,
                "Message": "Data invalid for create user service",
                "Data": {"errors": errors},
            }
            return response, HTTPStatus.BAD_REQUEST
    try:
        user_service_name = user_services_service.create_user_service(
            service=service, user_mother=user, user_service=user_services_schema
        )
    except IntegrityError as e:
        response = {
            "Success": False,
            "Message": "Error for create user service",
            "Data": {"errors": str(e)},
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    response = {
        "Success": True,
        "Message": "Success signup, user service create",
        "Data": {
            "user_name": user_service_name,
            "service_name": service.name,
        },
    }
    return response, HTTPStatus.CREATED
