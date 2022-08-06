from pydantic import BaseModel

class User(BaseModel):
    nickname:str
    country:str
    city: str