
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('chat/', Chat.as_view(),''),
    path("ask_question/", ask_question, name="ask_question"),

    path('cadastro', Cadastro.as_view(), name="cadastro")
]
