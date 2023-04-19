from django.urls import path
from accounts.consumers import MySyncConsumer,MyChatConsumer

websocket_urlpatterns = [
    path('sc/', MySyncConsumer.as_asgi()),
    path('chat/sc/', MyChatConsumer.as_asgi()),
]
