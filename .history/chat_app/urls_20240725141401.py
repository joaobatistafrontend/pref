
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("ask_question/", views.ask_question, name="ask_question"),
]
