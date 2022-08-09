from pydantic  import BaseModel

class Place(BaseModel):
    nickname:str
    coordinates:str
    date:str
    description:str

