from django.urls import path
from accounts.consumers import *

websocket_urlpatterns = [
    path('sc/',MySyncConsumer.as_asgi()),

]