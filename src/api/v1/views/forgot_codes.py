# Local Packages
from http import HTTPStatus
import random

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from ..schemas import UserForgotPasswordSchema, ForgotCodesSchema, ForgotCodesPasswordSchema
from ..services.users import UserService
from ..services.forgot_code import ForgotCodeService

from tools.email import sendEmail, hideEmail, generateHTML_forgot_code

def forgot_password_POST(parameters_json: dict):
    """EndPoint /forgot-password with method HTTP POST, Reset Password use email

    Args:
        parameters_json (dict): User data
    Returns:
        dict: response of the operation
    """
    try:
        user_forgot_password_schema = UserForgotPasswordSchema(**parameters_json)
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
    try:
        #Create Service
        user_service = UserService()
        forgot_code_service = ForgotCodeService()
        
        # Find User
        user_data = user_service.get_user_by_user_name(user_name=user_forgot_password_schema.user_name)
        
        #Generate Code random
        code = random.randrange(100000, 1000000)
        
        #Create Schema
        forgot_code_schema = ForgotCodesSchema(code=code, user_name=user_data.user_name)
        forgot_code_service.create_forgot_code(forgot_code_schema)
        body_html = generateHTML_forgot_code(str(code))
        #SendEmail
        send_email_response = sendEmail(user_data.email, 'Forgot Password', body_html)
    except IntegrityError as e:
        response = {
            "Success": False,
            "Message": "Error for create ForgotCode",
            "Data": {"errors": str(e)},
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    response = {
        "Success": True,
        "Message": 'send_email_response',
        "Data": {
            "user_name": user_forgot_password_schema.user_name,
            "user_email": hideEmail(user_data.email)
        },
    }
    return response, HTTPStatus.CREATED


def forgot_password_PUT(parameters_json: dict):
    """EndPoint /forgot-password with method HTTP POST, Reset Password use email

    Args:
        parameters_json (dict): User data
    Returns:
        dict: response of the operation
    """
    try:
        user_forgot_code_schema = ForgotCodesPasswordSchema(**parameters_json)
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
    try:
        #Create Service
        forgot_code_service = ForgotCodeService()
        user_service = UserService()
        
        #Get Forgot Code
        forgot_code_data = forgot_code_service.get_forgot_code_by_username_and_code(user_name=user_forgot_code_schema.user_name, code=user_forgot_code_schema.code)
        
        # If no exist Forgot Code
        if(forgot_code_data == None):
            response = {
                        "Success": False,
                        "Message": "Error No previous request for password change was found.",
                        "Data": {"errors": "No previous request for password change was found"},
                    }
            return response, HTTPStatus.FORBIDDEN
        
        # Update User
        new_user = user_service.change_password(user_name=user_forgot_code_schema.user_name, new_password=user_forgot_code_schema.password)
        
        # Remove Forgot Code
        forgot_code_service.remove_forgot_code(user_name=user_forgot_code_schema.user_name, code=user_forgot_code_schema.code)
        
    except IntegrityError as e:
        response = {
            "Success": False,
            "Message": "Error for Forgot Passwo",
            "Data": {"errors": str(e)},
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    # Return User Data
    response = {
        "Success": True,
        "Message": "Success forgot Password",
        "Data": {
            "name": new_user.name,
            "last_name": new_user.last_name,
            "email": new_user.email,
            "user_name": new_user.user_name,
            "phone_number": new_user.phone_number,
            "date_of_birth": new_user.date_of_birth,
            "role": new_user.role,
        },
    }
    return response, HTTPStatus.CREATED