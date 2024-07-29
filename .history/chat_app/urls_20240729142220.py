
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),

    path("ask_question/", ask_question, name="ask_question"),

    
    path('chat', chat,name='chat'),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('chat/<str:room_name>/send/', send_message, name='send_message'),

    path('cadastro', Cadastro.as_view(), name="cadastro")
]
