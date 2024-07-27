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
    "As políticas públicas para as mulheres no Brasil têm evoluído ao longo dos anos, refletindo mudanças nas normas sociais, avanços no movimento feminista e maior reconhecimento dos direitos das mulheres.\n\n"
    
    
    "* Criação do Conselho Nacional dos Direitos da Mulher (CNDM) em 1985.\n"
    "* Aprovação da Lei do Divórcio (Lei 6.515/1977) e da Lei dos Crimes Hediondos (Lei 8.072/1990), que incluía o feminicídio como crime hediondo.\n"
    "* Aprovação da Lei de Igualdade Salarial (Lei 7.855/1989), garantindo salários iguais para homens e mulheres para o mesmo trabalho.\n"
    "* Criação das Delegacias de Defesa da Mulher para tratar exclusivamente de crimes contra mulheres.\n\n"

    
    "* Aprovação da Lei Maria da Penha em 2006, um marco na legislação de combate à violência contra as mulheres.\n"
    "* Criação do Programa Bolsa Família em 2003, beneficiando principalmente mulheres em situação de vulnerabilidade social.\n"
    "* Criação do Programa de Assistência Integral à Saúde da Mulher (PAISM), oferecendo atendimento de saúde abrangente e específico para as mulheres.\n"
    "* Política Nacional de Enfrentamento à Violência contra as Mulheres, para combater a violência doméstica e de gênero.\n\n"

    "* Aprovação da Lei de Cotas para Mulheres em Eleições em 199
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
