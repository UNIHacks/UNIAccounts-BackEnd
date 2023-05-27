# External Packages
from flask import Blueprint, request
from flask import render_template
import json
import requests
import config.base as CONFIG

from tools.functions_authentication import valid_headers

from ..views.users import signup_route_POST
from ..views.forgot_codes import forgot_password_POST, forgot_password_PUT

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

@views_users.route("/signup", methods=["GET", "POST"])
def signup_app():
    """SignUp EndPoint

    Returns:
        dict: JSON response
        int: status code of the request
    """
    
    if request.method == 'POST':
        
        name   = request.form['name']
        last_name   = request.form['last_name']
        email  = request.form['email']
        user_name  = request.form['user_name']
        phone_number = request.form['phone_number']
        date_of_birth = request.form['date_of_birth']
        password  = request.form['password']
        role   = request.form['role']
        
        query = {
            'name'              : name,
            'last_name'         : last_name,
            'email'             : email,
            'user_name'         : user_name,
            'phone_number'      : phone_number,
            'date_of_birth'     : date_of_birth,
            'password'          : password,
            'role'              : role,
        }
        response = requests.post(f'http://127.0.0.1:{CONFIG.PORT}/api/v1/signup',json=query, headers={'Api-Key': CONFIG.config("API-KEY"), 'Service': CONFIG.config("SERVICE")} )
        response_json = json.loads(response.content)

        if(response_json.get('Success') == True):
            return render_template('successful_signup.html')
        else:
            return render_template('error_signup.html')

    return render_template('signup.html')

@views_users.route("/api/v1/forgot-password", methods=["POST", "PUT"])
def forgot_password():
    """Forgot Password EndPoint

    Returns:
        dict: JSON response
        int: status code of the request
    """

    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "POST":
        response = forgot_password_POST(parameters_json=request.get_json())
        return response
    if request.method == "PUT":
        response = forgot_password_PUT(parameters_json=request.get_json())
        return response