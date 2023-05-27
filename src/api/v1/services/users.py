from datetime import datetime
from werkzeug.security import generate_password_hash

from config.database import get_session
from models import UsersModel

from ..schemas import UserSchema


class UserService:
    def create_user(self, user_data: UserSchema) -> UsersModel:
        session = get_session()
        user = UsersModel(
            name=user_data.name,
            last_name=user_data.last_name,
            email=user_data.email,
            user_name=user_data.user_name,
            phone_number=user_data.phone_number,
            date_of_birth=user_data.date_of_birth,
            password=generate_password_hash(user_data.password),
            role=user_data.role,
        )
        session.add(user)
        session.commit()
        session.close()
        return user

    def get_user_by_user_name(self, user_name: str) -> UsersModel:
        session = get_session()
        user = (
            session.query(UsersModel).filter(UsersModel.user_name == user_name).first()
        )
        session.close()
        return user
    
    def change_password(self, user_name: str, new_password: str) -> UsersModel:
        session = get_session()
        user = (session.query(UsersModel).filter(UsersModel.user_name==user_name).first())
        user.password = generate_password_hash(new_password)
        session.commit()
        return user
