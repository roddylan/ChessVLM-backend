from fastapi import APIRouter
import app.api.socket as socket 

router = APIRouter()

router.include_router(socket.router, '/ws', ['chess'])