######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 06/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# Local Packages
from services.db.idata_base import IDataBase
from models.user import User

def signup_route_POST(parameters_json: dict, data_base: IDataBase, service_name: str):
    """EndPoint /signup with method HTTP POST, Create new User in DataBase

    Args:
        parameters_json (dict): User data
        data_base (IDataBase): Implementation of the database to be used
        service_name (str): Name of the service requested by the operation

    Returns:
        dict: response of the operation in the DataBase
    """
    new_user = User.from_dict(parameters_json)
    if new_user == None:
        return {'message': 'Error User no created', 'status_code': 428}
    # TODO: Convert return types to dict
    message, status_code = data_base.create_user(new_user, service_name)
    response = {'message': message, 'status_code': status_code}
    return response