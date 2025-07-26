from fastapi import APIRouter, WebSocket
# from app.bot
router = APIRouter()


@router.websocket("/chess")
async def chess(socket: WebSocket):
    await socket.accept()
    while True:
        data = await socket.receive_json()
        
    
    return 