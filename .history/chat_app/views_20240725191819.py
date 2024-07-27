from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from treinamento import contexto_inicial
#chave api
genai.configure(api_key="AIzaSyCkg2khwEkqTQ7kYa8gVzsz2bWWpweUEO8")


@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")#receber o texto do user
        model = genai.GenerativeModel("gemini-pro")#modelo da ia

        chat = model.start_chat()#iniciar um chat
        
#receber o texto do usuario como parametro
        response = chat_instance.send_message(f'o assunto que vamos conversa é sobre :{contexto_inicial}, eu sou uma mulher que preciso de suporte sobre esses assuntos')
        user = request.user #ususario
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)#criar um batepapo
        
        response_data = {#extrair apenas a resposta
            "text": response.text,  #tranforma a resposta em texto
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        ) 


@login_required
def chat(request):
    user = request.user #saber o user autenticado
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chat_bot.html", {"chats": chats})