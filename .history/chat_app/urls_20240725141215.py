
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', chat('chat_app.urls'))
]
