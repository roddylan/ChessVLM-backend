from fastapi import FastAPI, Websocket
from app.api import socket


app = FastAPI()

app.include_router(socket.router, '/ws')