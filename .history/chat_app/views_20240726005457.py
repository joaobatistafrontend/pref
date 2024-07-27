from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from .treinamentos import contexto_inicial, contexto_de_estudos
#chave api
genai.configure(api_key="AIzaSyCkg2khwEkqTQ7kYa8gVzsz2bWWpweUEO8")


@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")#receber o texto do user
        model = genai.GenerativeModel("gemini-pro")#modelo da ia

        chat = model.start_chat()#iniciar um chat
        
        #receber o texto do usuario como parametro
        response = chat.send_message(f'o assunto que vamos conversa é sobre responder perguntas frequentes e prestar suporte
a assuntos relacionados às políticas públicas voltadas para as mulheres
                                     {contexto_inicial} e {contexto_de_estudos},\
                                        eu sou uma mulher que preciso de suporte sobre esses assuntos, nao seidei o {user} \
                                        troca de assunto mantenha o foco em responder perguntas frequentes e prestar suportea \ 
                                        assuntos relacionados às políticas públicas voltadas para as mulheres.')
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