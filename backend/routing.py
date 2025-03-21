from django.urls import include, path

websocket_urlpatterns = [
    path('', include('api.routing'))
]