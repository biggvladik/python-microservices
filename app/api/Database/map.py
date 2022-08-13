from pymongo import MongoClient

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.mushrooms
        self.collection = self.db.map

    def insert_coordinates(self,nickname,x,y,description):
        self.collection.update_one({"nickname":nickname},{"$push" :{ "coordinates": {"x":x,"y":y,"description":description}}})





   # def get_coordinates_by_nickname(self,nickname) -> List




