from pydantic import BaseModel
from typing import List
from .map import Place
class User(BaseModel):
    nickname: str
    email: str
    coordinates: List[Place]
