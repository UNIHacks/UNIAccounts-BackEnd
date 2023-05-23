# Local Packages
from http import HTTPStatus

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from ..schemas import UserSchema
from ..services.users import UserService


def signup_route_POST(parameters_json: dict):
    """EndPoint /signup with method HTTP POST, Create new User in DataBase

    Args:
        parameters_json (dict): User data
    Returns:
        dict: response of the operation in the DataBase
    """

    try:
        user_schema = UserSchema(**parameters_json)
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

    user_service = UserService()
    try:
        user_service.create_user(user_data=user_schema)
    except IntegrityError as e:
        response = {
            "Success": False,
            "Message": "Error for create user",
            "Data": {"errors": str(e)},
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    response = {
        "Success": True,
        "Message": "Success signup, user create",
        "Data": {
            "name": user_schema.name,
            "last_name": user_schema.last_name,
            "email": user_schema.email,
            "user_name": user_schema.user_name,
            "phone_number": user_schema.phone_number,
            "date_of_birth": user_schema.date_of_birth,
            "role": user_schema.role,
        },
    }
    return response, HTTPStatus.CREATED
