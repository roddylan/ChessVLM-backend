from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
import bot
import bot.chessllm
import bot.constants as constants
import os

'''
Websocket consumer for chess game
'''
class ChessLLMConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # await self.accept()
        # await self.send(text_data=json.dumps({
        #     "message": "Connected to server"
        # }))
        # return await super().connect()
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
        # TODO: generate uuid for each instance
        self.room_name = "chess1"
        self.room_group_name = f"chess_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    
    async def disconnect(self, code):
        # leave
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        # return await super().disconnect(code)
    
    async def receive(self, text_data=None, bytes_data=None):
        # print(f"\n\n{text_data=}\n\n")
        data = json.loads(text_data)
        # print(f"\n\n{data=}\n\n")
        fen = data.get("fen", constants.STARTING_FEN)
        # api = data.get("api", "")
        api = data.get("api", os.getenv("API_KEY"))
        # print(f"{api=}")
        # print(f"{os.getenv("API_KEY")=}")
        player = data.get("player", "w")
        opponent = data.get("opponent", "b")
        # print("rec data")
        # print(data)
        print("\nreceived data:\n")
        print(data)
        print("\n--------------\n")
        
        # TODO: make async, maybe use asyncio
        resp = bot.chessllm.run_gemini(
            gem=api,
            player=player,
            opponent=opponent,
            fen=fen
        )

        await self.send(text_data=json.dumps(resp))
        # await self.send(text_data=json.dumps({"api": api}))

        # return await super().receive(text_data, bytes_data)
    
    async def send(self, text_data=None, bytes_data=None, close=False):
        return await super().send(text_data, bytes_data, close)