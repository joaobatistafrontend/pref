#https://espere.in/Build-your-chatbot-with-the-power-of-Gemini-API-using-Django/
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from .treinamentos import contexto_inicial, contexto_de_estudos

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from .forms import CustomUserCreationForm

#chave api
genai.configure(api_key="AIzaSyCkg2khwEkqTQ7kYa8gVzsz2bWWpweUEO8")


class AskQuestionView(LoginRequiredMixin, View):
    def post(self, request):
        text = request.POST.get("text")  # receber o texto do user
        model = genai.GenerativeModel("gemini-pro")  # modelo da ia

        chat = model.start_chat()  # iniciar um chat

        user = request.user  # usuário
        iniciativa = (
            f"O assunto que o {user} pode conversar é sobre responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres. "
            f"Tenha conhecimento e forneça aconselhamento acessível para o {user}. "
            f"Use as seguintes leis e contextos para ajudar: {contexto_inicial} e {contexto_de_estudos}. "
            f"Foque em dados do Ceará. Mantenha o foco em responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres. "
            f"Mas também esteja pronto para outras perguntas como {text}"
        )
        # receber o texto do usuario como parâmetro
        response = chat.send_message(
            f"{iniciativa} deixei sempre a pergunta: {text} para responder primeiro"
        )

        ChatBot.objects.create(
            text_input=text, gemini_output=response.text, user=user
        )  # criar um bate-papo

        response_data = {
            "text": response.text,  # transforma a resposta em texto
        }
        return JsonResponse({"data": response_data})

    def get(self, request):
        return HttpResponseRedirect(reverse("ask_question"))



@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")#receber o texto do user
        model = genai.GenerativeModel("gemini-pro")#modelo da ia

        chat = model.start_chat()#iniciar um chat
        
        user = request.user #ususario
        iniciativa = f'O assunto que o {user} pode conversar é sobre responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres. Tenha conhecimento e forneça aconselhamento acessível para o {user}. Use as seguintes leis e contextos para ajudar: {contexto_inicial} e {contexto_de_estudos}. Foque em dados do Ceará. Mantenha o foco em responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres.Mais tambem esteje pronto para outras perguntas como {text}'
        #receber o texto do usuario como parametro
        response = chat.send_message(f" {iniciativa} deixei sepre a pergunta: {text} para responder primeiro"
        )
        
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)#criar um batepapo
        
        response_data = {#extrair apenas a resposta
            "text": response.text,  #tranforma a resposta em texto
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("ask_question")
        ) 

class Chat(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user #saber o user autenticado
        chats = ChatBot.objects.filter(user=user)
        return render(request, "chat_bot.html")


@login_required
def chat(request):
    user = request.user #saber o user autenticado
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chat_bot.html", {"chats": chats})

def index(request):
    
    return render(request, "index.html")


@login_required
def chat_room(request, room_name):
    room = get_object_or_404(SalaMeninas, name=room_name)
    messages = room.message_set.all().order_by('timestamp')
    return render(request, 'chat_meninas.html', {'room': room, 'messages': messages})

@login_required
def send_message(request, room_name):
    if request.method == 'POST':
        room = get_object_or_404(SalaMeninas, name=room_name)
        message = Message(user=request.user, chat_room=room, content=request.POST['message'])
        message.save()
    return redirect('chat_room', room_name=room_name)

class Cadastro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/cadastro.html',{'form':form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/cadastro.html', {'form': form})
    

