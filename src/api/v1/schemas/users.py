from datetime import datetime

from pydantic import BaseModel, EmailStr, validator, ValidationError


class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    user_name: str
    phone_number: str
    date_of_birth: datetime
    password: str
    role: str
    
    @validator('date_of_birth', pre=True)
    def validate_date_of_birth(cls, value):
        return datetime.strptime(value, "%d-%m-%Y")
            
        


class UserSigninSchema(BaseModel):
    user_name: str
    password: str
