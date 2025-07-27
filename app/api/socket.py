from fastapi import APIRouter, WebSocket
from app.schema.server import Receive
from app.core.config import settings
from app.services.bot.chessllm import run_gemini
from starlette.websockets import WebSocketDisconnect

router = APIRouter()

@router.websocket("/chess")
async def chess(socket: WebSocket):
    await socket.accept()
    try:
        while True:
            data = await socket.receive_json()
            rec_data = Receive.model_validate(data)
            res = run_gemini(settings.gemini_key, player=rec_data.player, opponent=rec_data.opponent, fen=rec_data.fen)
            print("-------------")
            print(res)
            print("-------------")
            await socket.send_json(res)
    except WebSocketDisconnect:
        return