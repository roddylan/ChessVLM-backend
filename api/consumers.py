from channels.generic.websocket import WebsocketConsumer

'''
Websocket consumer for chess game


'''
class ChessLLMConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        return super().disconnect(code)
    
    def receive(self, text_data=None, bytes_data=None):
        text_data 
        return super().receive(text_data, bytes_data)