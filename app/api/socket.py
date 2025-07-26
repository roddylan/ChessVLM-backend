from fastapi import APIRouter, WebSocket
from app.schema.server import Receive
from app.services.bot.chessllm import run_gemini
router = APIRouter()


@router.websocket("/chess")
async def chess(socket: WebSocket):
    await socket.accept()
    while True:
        data = await socket.receive_json()
        rec_data = Receive.model_validate(data)
        # run_gemini()
    
    return 