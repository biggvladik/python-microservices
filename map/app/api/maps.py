from fastapi import APIRouter,Depends,HTTPException
from .models import Place
from .database import Database


router = APIRouter()

@router.post('/',response_model=Place)
async def upload_user(place:Place,Database = Depends(Database)):
    Database.add_place(place.nickname,place.coordinates,place.date,place.description)
    return place

# @router.get('/',response_model=Place)
# async def get_user_by_nickname(nickname:str,Database = Depends(Database)):
#     Database.

