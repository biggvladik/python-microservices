from pymongo import MongoClient
import hashlib

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.database = self.client.users
        self.collection = self.database.users


    def add_user(self,nickname,password,country,city):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        nicknames = self.get_all_nickname()
        if nickname not in nicknames:

            user = {
                'nickname': nickname,
                'password': hashed_password,
                'country': country,
                'city': city,
            }

            self.collection.insert_one(user)

        else:
            return 'Error'



    def change_password(self,nickname,password,new_password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        new_hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()


        self.collection.update_one({'nickname':nickname,'password':hashed_password},
                                   {'$set':
                                        {'password':new_hashed_password}
                                    }
                                )




    def change_country(self,new_country,password,nickname):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        self.collection.update_one({'nickname': nickname, 'password': hashed_password},
                              {'$set':
                                   {'country': new_country}
                               }
                              )



    def change_city(self,new_city,password,nickname):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        self.collection.update_one({'nickname': nickname, 'password': hashed_password},
                              {'$set':
                                   {'city': new_city}
                               }
                              )


    def delete_account(self,nickname,password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        self.collection.delete_one({'nickname':nickname, 'password':hashed_password})


    def get_all_nickname(self) -> list:
        A = []
        res = self.collection.find({}, {'_id': 0, 'password': 0, 'country': 0,'city':0})
        for i in res:
            A.append(i['nickname'])
        return A







