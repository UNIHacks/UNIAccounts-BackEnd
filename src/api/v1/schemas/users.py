from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    user_name: str
    phone_number: str
    date_of_birth: str
    password: str
    role: str


class UserSigninSchema(BaseModel):
    user_name: str
    password: str
