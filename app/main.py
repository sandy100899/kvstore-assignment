from fastapi import FastAPI
from api import key

app = FastAPI()

app.include_router(key.router)