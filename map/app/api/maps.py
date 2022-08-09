from fastapi import APIRouter,Depends
from .models import Place
from .database import Database
from typing import List

router = APIRouter()


@router.get('/',response_model=List[Place])
def get_place_by_username(nickname:str,Database =Depends(Database)):
    places = Database.get_places_by_nickname(nickname)

    return places


@router.delete('/')
def delete_place(nickname:str,coordinates:str,Database = Depends(Database)):
    Database.delete_place(nickname,coordinates)


@router.post('/',response_model=Place)
def upload_user(place:Place,Database = Depends(Database)):
    Database.add_place(place.nickname,place.coordinates,place.date,place.description)
    return place