from pydantic  import BaseModel
from typing import List
class Place(BaseModel):
    nickname:str
    coordinates:List
    date:str
    description:str

