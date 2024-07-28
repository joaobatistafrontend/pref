
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("ask_question/", Chat.as_view, name="ask_question"),

    path('cadastro', Cadastro.as_view(), name="cadastro")
]
