from fastapi import APIRouter,Depends,HTTPException
from .models import Place
from .database import Database
from typing import List
from service import is_correct_password
router = APIRouter()


@router.get('/',response_model=List[Place])
def get_place_by_username(nickname:str,password:str,Database =Depends(Database)):
    if is_correct_password(nickname,password):
        places = Database.get_places_by_nickname(nickname)
        return places
    else:
        raise HTTPException(status_code=404, detail="Error")


@router.delete('/')
def delete_place(nickname:str,coordinates:str,password:str,Database = Depends(Database)):
    if is_correct_password(nickname, password):
        Database.delete_place(nickname,coordinates)
    else:
        raise HTTPException(status_code=404, detail="Error")



@router.post('/',response_model=Place)
def upload_user(place:Place,Database = Depends(Database)):
    if is_correct_password(nickname, password):
        Database.add_place(place.nickname,place.coordinates,place.date,place.description)
        return place
    else:
        raise HTTPException(status_code=404, detail="Error")
