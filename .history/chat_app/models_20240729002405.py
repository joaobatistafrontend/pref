from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class SalaMeninas(models.Model):
    name = models.CharField(max_length=1000)
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(SalaMeninas, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
class ChatBot(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="GeminiUser", null=True
    )
    text_input = models.CharField(max_length=500)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text_input
    