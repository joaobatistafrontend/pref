import google.generativeai as genai

# Configure a chave da API
chave = 'AIzaSyCTG0iYJKRv0D0FXBw3Ikai0FPfE68ZUSo'
genai.configure(api_key=chave)

# Listar modelos disponíveis
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f'nomes: {m.name}')

# Inicializar o modelo
model = genai.GenerativeModel("gemini-pro")

# Iniciar um chat
chat_instance = model.start_chat()

# Enviar uma mensagem dentro do contexto definido
response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
print(response)

# Continuar a conversa dentro do mesmo contexto
response = chat_instance.send_message("Como essas políticas têm evoluído ao longo dos anos?")
print(response)
