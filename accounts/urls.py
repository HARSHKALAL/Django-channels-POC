from django.urls import path,include
from .views import index,chat

urlpatterns = [
    path('homepage/',index,name="homepage"),
    path('chat/',chat,name="chat")

]
