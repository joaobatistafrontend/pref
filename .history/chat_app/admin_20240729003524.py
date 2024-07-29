from django.contrib import admin
from .models import *

admin.site.register(ChatBot)
admin.site.register(SalaMeninas)
from django.contrib import admin
from .models import SalaMeninas, Message

@admin.register(SalaMeninas)
class SalaMeninasAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('participants',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat_room', 'content', 'timestamp')
    search_fields = ('user__username', 'chat_room__name', 'content')
    list_filter = ('timestamp', 'chat_room')