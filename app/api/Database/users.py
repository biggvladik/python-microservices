from pymongo import MongoClient

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.mushrooms
        self.collection = self.db.map



    def create_user(self,nickname:str,email:str):

        user = {
            "nickname": nickname,
            "email": email,
            "coordinates": [],

        }
        self.collection.insert_one(user)







