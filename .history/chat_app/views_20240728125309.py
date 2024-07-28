#https://espere.in/Build-your-chatbot-with-the-power-of-Gemini-API-using-Django/
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
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





@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")#receber o texto do user
        model = genai.GenerativeModel("gemini-pro")#modelo da ia

        chat = model.start_chat()#iniciar um chat
        
        user = request.user #ususario
        iniciativa = 'O assunto que vamos conversar é sobre responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres. Tenha conhecimento e forneça aconselhamento acessível para o {user}. Use as seguintes leis e contextos para ajudar: {contexto_inicial} e {contexto_de_estudos}. Foque em dados do Ceará. Mantenha o foco em responder perguntas frequentes e prestar suporte a assuntos relacionados às políticas públicas voltadas para as mulheres.'
        #receber o texto do usuario como parametro
        response = chat.send_message(f"{iniciativa}, mais o {user} pode fazer "
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
    

