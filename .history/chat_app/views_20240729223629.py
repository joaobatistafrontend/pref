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
class IndexView(View):
    def get(self, request):
        
        return render(request, "index.html")

#chave api
genai.configure(api_key="AIzaSyCkg2khwEkqTQ7kYa8gVzsz2bWWpweUEO8")


class AskQuestionView(LoginRequiredMixin, View):
    def post(self, request):
        text = request.POST.get("text")  # receber o texto do user
        model = genai.GenerativeModel("gemini-pro")  # modelo da ia

        chat = model.start_chat()  # iniciar um chat

        user = request.user  # usuário
        iniciativa = ( #parametros
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

        response_data = { #parametro da 
            "text": response.text,  # transforma a resposta em texto
        }
        return JsonResponse({"data": response_data})

    def get(self, request):
        return HttpResponseRedirect(reverse("ask_question"))


class ChatBotView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user #saber o user autenticado
        chats = ChatBot.objects.filter(user=user)
        return render(request, "chat_bot.html",{"chats": chats}) 
    

class ChatRedirectView(View):
    def get(self, request):
        room_name = 'meninas'  # nome da sala existente
        return redirect('chat_room', room_name=room_name)


class ChatRoomView(LoginRequiredMixin,TemplateView):
    def get(self, request, room_name):
        room = get_object_or_404(SalaMeninas, name=room_name)
        messages = room.message_set.all().order_by('timestamp')#na ordem das mensagens mais antigas aparecem primeiro.
        return render(request, 'chat_meninas.html', {'room': room, 'messages': messages})

    def post(self, request, room_name):
        room = get_object_or_404(SalaMeninas, name=room_name)
        content = request.POST.get('message', '').strip()

        if content:  # Verifica se a mensagem não está vazia ou composta apenas de espaços em branco.
            message = Message(user=request.user, chat_room=room, content=content)
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
    

