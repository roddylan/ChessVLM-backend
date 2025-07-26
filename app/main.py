from fastapi import FastAPI, Websocket
from app.api.socket import router as socket_router


app = FastAPI()

app.add_api_websocket_route('/ws', socket_router)