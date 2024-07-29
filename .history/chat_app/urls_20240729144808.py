
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),

    path("ask_question/", AskQuestionView.as_view(), name="ask_question"),

    path('chat_meninas', ChatRedirectView.as_view(), name='chat_meninas'),
    path('chat_bot/', ChatBotView.as_view(), name='chat_bot'),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('chat/<str:room_name>/send/', send_message, name='send_message'),

    path('cadastro', Cadastro.as_view(), name="cadastro")
]
