from pydantic import BaseModel


class Place(BaseModel):
    x : float
    y : float
    description : str
