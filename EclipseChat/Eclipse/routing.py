from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('lobby/', consumers.ChatConsumer.as_asgi()),
]