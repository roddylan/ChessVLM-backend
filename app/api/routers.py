from fastapi import APIRouter
import app.api.socket as socket 
import app.api.healthcheck as healthcheck

router = APIRouter()

router.include_router(socket.router, prefix='/ws', tags=['chess'])
router.include_router(healthcheck.router, prefix='', tags=['healthcheck'])
