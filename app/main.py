from fastapi import FastAPI
from app.api import socket


app = FastAPI()

app.include_router(socket.router, '/ws')