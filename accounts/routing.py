from django.urls import path
from accounts.consumers import MySyncConsumer

websocket_urlpatterns = [
    path('sc/', MySyncConsumer.as_asgi()),
]
