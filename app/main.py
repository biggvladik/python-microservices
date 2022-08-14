from fastapi import FastAPI
from api.routers import map
app = FastAPI()
app.include_router(map.router)

