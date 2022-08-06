from pydantic import BaseModel

class User(BaseModel):
    nickname:str
    country:str
    city: str


class Create_User(User):
    password:str