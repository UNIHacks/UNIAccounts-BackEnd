from werkzeug.security import generate_password_hash

from config.database import get_session
from models import ServicesModel, UserServicesModel, UsersModel

from ..schemas import UserServicesSchema


class UserServicesService:
    def get_user_by_user_name(self, user_name: str) -> UserServicesModel:
        session = get_session()
        user = (
            session.query(UserServicesModel)
            .filter(UserServicesModel.user_name == user_name)
            .first()
        )
        session.close()
        return user

    def create_user_service(
        self,
        service: ServicesModel,
        user_mother: UsersModel,
        user_service: UserServicesSchema,
    ) -> str:
        session = get_session()

        user_name = None
        user_password = None
        if user_service:
            user_name = user_service.user_name
            user_password = generate_password_hash(user_service.password)

        user_service_created = UserServicesModel(
            user_name=user_name,
            password=user_password,
            service_id=str(service.id),
            user_id=str(user_mother.id),
        )
        session.add(user_service_created)
        session.commit()
        session.close()
        return user_name
