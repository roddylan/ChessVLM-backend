from channels.generic.websocket import WebsocketConsumer

class ChessLLMConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        return super().disconnect(code)
    
    def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)