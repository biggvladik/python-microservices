from fastapi import APIRouter,Depends
from .models import User,Create_User
from .database import Database
router = APIRouter()


@router.get('/user{nickname}',tags=['users'],response_model=User)
async def get_user_by_nickname(nickname, Database=Depends(Database)):
    user = Database.get_user(nickname)

    return user


@router.post('/user',tags=['users'],response_model=User)    # CДЕЛАТЬ ПРОБРОС ОШИБКИ ПРИ ДОБАВЛЕНИИ СУЩЕСТВУЮЩЕГО ПОЛЬЗОВАТЕЛЯ
async def create_user(user:Create_User,Database=Depends(Database)):
    Database.add_user(user.nickname,user.password,user.country,user.city)

    a = User(
        nickname = user.nickname,
        country = user.country,
        city = user.city,
    )
    return a






