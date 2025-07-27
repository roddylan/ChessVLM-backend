from starlette.testclient import WebSocketTestSession
from httpx import AsyncClient
from app.main import app
from app.schema.server import Receive, Send
from app.services.bot.constants import STARTING_FEN
import pytest
import asyncio
# import websockets
from websockets.asyncio.client import connect, ClientConnection

@pytest.mark.asyncio
async def test_websocket_init():
    base_url = "ws://0.0.0.0:8000"
    json_send_data = Receive(
        fen=STARTING_FEN,
        player="b",
        opponent="w"
    ).model_dump_json()
    assert(isinstance(json_send_data, str))
    
    socket: ClientConnection
    async with connect(f"{base_url}/ws/chess") as socket:
        await socket.send(json_send_data)
        resp = await socket.recv()
        parsed = Send.model_validate_json(resp)
        
        assert isinstance(parsed, Send)

@pytest.mark.asyncio
async def test_websocket_bad():
    base_url = "ws://0.0.0.0:8000"
    json_send_data = Receive(
        fen="x",
        player="b",
        opponent="w"
    ).model_dump_json()
    assert(isinstance(json_send_data, str))
    
    socket: ClientConnection
    async with connect(f"{base_url}/ws/chess") as socket:
        await socket.send(json_send_data)
        resp = await socket.recv()
        parsed = Send.model_validate_json(resp)
        
        assert isinstance(parsed, Send)
