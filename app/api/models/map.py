from pydantic import BaseModel
from typing import List,Optional

class Place(BaseModel):
    x : float
    y : float
    description : str


class Place_get(BaseModel):
    nickname:str
    coordinates: List[Optional[Place]]