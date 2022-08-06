from pymongo import MongoClient
import hashlib

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.database = self.client.users
        self.users = self.database.users


    def add_user(self,nickname,password,country,city):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        user = {
            'nickname': nickname,
            'password': hashed_password,
            'country': country,
            'city': city,
        }

        self.users.insert_one(user)



    def change_password(self):
        pass



    def change_country(self):
        pass


    def change_city(self):
        pass

    
    def delete_account(self):

        pass

a= Database()

