from fastapi import FastAPI
from .api import maps
app = FastAPI()

app.include_router(maps.router,prefix='/api/v1/maps', tags=['movies'])

