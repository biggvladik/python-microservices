import os
import httpx

USERS_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/user/password/'
url = os.environ.get('USERS_SERVICE_HOST_URL') or USERS_SERVICE_HOST_URL

def is_correct_password(nickname:str,password:str):
    r = httpx.get(f'{url}{nickname}/{password}')
    return True if r.status_code == 200 else False


