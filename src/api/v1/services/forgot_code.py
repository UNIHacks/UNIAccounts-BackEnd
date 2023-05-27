from datetime import datetime
from werkzeug.security import generate_password_hash

from config.database import get_session
from models import ForgotCodeModel

from ..schemas import ForgotCodesSchema

from sqlalchemy import and_


class ForgotCodeService:
    def create_forgot_code(self, forgot_code_data: ForgotCodesSchema) -> ForgotCodeModel:
        session = get_session()
        forgot_code = ForgotCodeModel(
            user_name=forgot_code_data.user_name,
            code=forgot_code_data.code
        )
        session.add(forgot_code)
        session.commit()
        session.close()
        return forgot_code
    
    def get_forgot_code_by_username_and_code(self, code: str, user_name: str) -> ForgotCodeModel:
        session = get_session()
        user = (
            session.query(ForgotCodeModel).filter(and_(ForgotCodeModel.code == code, ForgotCodeModel.user_name == user_name)).first()
        )
        session.commit()
        session.close()
        return user
    
    def remove_forgot_code(self, code: str, user_name: str) -> ForgotCodeModel:
        session = get_session()
        forgot_code = (
            session.query(ForgotCodeModel).filter(and_(ForgotCodeModel.code == code, ForgotCodeModel.user_name == user_name)).first()
        )
        session.delete(forgot_code)
        session.commit()
        return forgot_code