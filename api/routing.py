from django.urls import path
from .consumers import ChessLLMConsumer


websocket_urlpatterns = [
    path("ws/chess/", ChessLLMConsumer.as_asgi())
]