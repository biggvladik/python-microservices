import os
import httpx
import hashlib
from users.app.api.database import Database
Database=Database()
USERS_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/users/'
url = os.environ.get('CAST_SERVICE_HOST_URL') or USERS_SERVICE_HOST_URL

def is_correct_password(nickname:str,password:str):
    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hash_password == Database.get_hash_password_by_nickname(nickname)

