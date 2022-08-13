from motor import motor_asyncio
#from .models import Place
from typing import List
import os

class Database():
    def __init__(self):
        self.client = motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
        self.db = self.client.test_database
        self.collection = self.db.map


    def add_place(self,nickname:str,coordinates:List,date:str,description:str):
         place = {
             'nickname': nickname,
             'coordinates': coordinates,
             'date': date,
             'description': description,
         }

         self.collection.insert_one(place)

    #
    #
    # def get_places_by_nickname(self,nickname):
    #     A = []
    #     res = self.collection.find({"nickname": nickname}, {'_id': 0})
    #     for i in res:
    #         place=Place(
    #             nickname = i['nickname'],
    #             coordinates = i['coordinates'],
    #             date = i['date'],
    #             description = i['description']
    #
    #
    #         )
    #         A.append(place)
    #     return A
    #
    #
    #
    # def delete_place(self,nickname,coordinates):
    #     self.collection.delete_one({'nickname':nickname, 'coordinates':coordinates})












