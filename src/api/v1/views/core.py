# Local Packages
from http import HTTPStatus

from pydantic import ValidationError
from werkzeug.security import check_password_hash

import config.base as CONFIG
from tools.funtions_jwt import validate_token, write_token

from ..schemas import UserSigninSchema
from ..services.user_services import UserServicesService
from ..services.users import UserService


def signin_route_PUT(request):

    service = CONFIG.API_KEYS[request.headers.get("Service")]
    parameters_json = request.get_json()

    try:
        user_signin_schema = UserSigninSchema(**parameters_json)
    except ValidationError as e:
        errors = []
        for error in e.errors():
            errors.append({"field": error["loc"][0], "message": error["msg"]})
        response = {
            "Success": False,
            "Message": "Data invalid for create user",
            "Data": {"errors": errors},
        }
        return response, HTTPStatus.BAD_REQUEST

    if service.mother_login:
        user_service = UserService()
        user = user_service.get_user_by_user_name(
            user_name=user_signin_schema.user_name
        )
    else:
        user_service = UserServicesService()
        user = user_service.get_user_by_user_name(
            user_name=user_signin_schema.user_name
        )

    if user:
        user_mother_id = str(user.id) if service.mother_login else str(user.user_id)
        is_valid_password = check_password_hash(
            user.password, user_signin_schema.password
        )
        if is_valid_password:
            token_jwt = write_token(
                data={
                    "user_name": user_signin_schema.user_name,
                    "service_name": service.name,
                    "user_mother_id": user_mother_id,
                },
                minutes_until_expire=service.jwt_exp,
            )
            response = {
                "Success": True,
                "Message": "Sigin success",
                "Data": {"token_jwt": token_jwt},
            }
            return response, HTTPStatus.OK
        else:
            response = {
                "Success": False,
                "Message": "User name or password incorrect",
                "Data": {},
            }
            return response, HTTPStatus.UNAUTHORIZED
    else:
        response = {
            "Success": False,
            "Message": f"Don't exist any register on DB with user_name={user_signin_schema.user_name}",
            "Data": {},
        }
        return response, HTTPStatus.NOT_FOUND


def validate_token_route_GET(request):
    try:
        authorization = request.headers["Authorization"].split()
        name_token = authorization[0]
        token = authorization[1]
        if name_token != CONFIG.TOKEN_TYPE:
            raise IndexError()
    except IndexError:
        response = {
            "Success": False,
            "Message": "The token don't exist in headers or token don't have a representation correct",
            "Data": None,
        }
        return response, HTTPStatus.BAD_REQUEST

    token_is_valid, response = validate_token(token=token)

    if token_is_valid:
        message = "Success token"
        data = response
        status_code = HTTPStatus.OK
    else:
        message = response
        data = None
        status_code = HTTPStatus.BAD_REQUEST

    response = {
        "Success": token_is_valid,
        "Message": message,
        "Data": data,
    }
    return response, status_code
