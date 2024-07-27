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

print(f'chat: {chat} \n')
prompt = input('olha me escreva algo: ')

while prompt != 'fim':
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')
