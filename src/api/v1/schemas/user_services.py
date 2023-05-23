from pydantic import BaseModel


class UserServicesSchema(BaseModel):
    user_name: str
    password: str
