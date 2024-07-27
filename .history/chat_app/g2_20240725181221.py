import google.generativeai as genai

chave = 'AIzaSyCTG0iYJKRv0D0FXBw3Ikai0FPfE68ZUSo'

genai.configure(api_key=chave)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        #print(f'nomes: {m.name}')
        pass


# Inicializar o modelo
model = genai.GenerativeModel("gemini-pro")

# Iniciar um chat e definir o contexto
chat_instance = model.start_chat(context="políticas públicas para as mulheres")
# Enviar uma mensagem dentro do contexto definido
response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
print(response)

# Continuar a conversa dentro do mesmo contexto
response = chat_instance.send_message("Como essas políticas têm evoluído ao longo dos anos?")
print(response)
print(f'chat: {chat} \n')
prompt = input('olha me escreva algo: ')

while prompt != 'fim':
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')
