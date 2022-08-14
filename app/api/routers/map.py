from fastapi import APIRouter,Depends
from ..models.map import Place,Place_get
from ..Database.map import Database

router = APIRouter()

@router.get('/{nickname}',response_model=Place_get)
async def get_place(nickname:str,Database = Depends(Database)):
    res = Database.get_coordinates_by_nickname(nickname)
    place = Place_get(
        nickname = res['nickname'],
        coordinates = res['coordinates']

    )
    return place


@router.post('/')
async def create_place(place:Place):



