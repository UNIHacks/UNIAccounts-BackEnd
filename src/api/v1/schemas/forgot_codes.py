from datetime import datetime

from pydantic import BaseModel, EmailStr, validator, ValidationError


class ForgotCodesSchema(BaseModel):
    code: str
    user_name: str

class ForgotCodesPasswordSchema(BaseModel):
    code: str
    user_name: str
    password: str