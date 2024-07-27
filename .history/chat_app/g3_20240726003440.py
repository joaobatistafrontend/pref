import google.generativeai as genai

# Configure a chave da API
chave = 'AIzaSyCTG0iYJKRv0D0FXBw3Ikai0FPfE68ZUSo'
genai.configure(api_key=chave)

# Listar modelos disponíveis
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        #print(f'nomes: {m.name}')
        pass
# Inicializar o modelo
model = genai.GenerativeModel("gemini-pro")

# Iniciar um chat
chat_instance = model.start_chat()

# Definir o contexto inicial enviando uma mensagem detalhada
contexto_inicial = (

)

# Enviar a mensagem com o contexto inicial
response = chat_instance.send_message(f'o assunto que vamos conversa é sobre :{contexto_inicial}, eu sou uma mulher que preciso de suporte sobre esses assuntos')
#print(response.text)

# Continuar a conversa dentro do mesmo contexto
#response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
#print(response.text)

# Loop de conversa contínua
prompt = input('olha me escreva algo: ')

while prompt.lower() != 'fim':
    response = chat_instance.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')
