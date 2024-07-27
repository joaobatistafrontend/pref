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

# Definir o contexto inicial enviando uma mensagem detalhada
contexto_inicial = (
    "As políticas públicas para as mulheres no Brasil têm evoluído ao longo dos anos, refletindo mudanças nas normas sociais, avanços no movimento feminista e maior reconhecimento dos direitos das mulheres.\n\n"
    "**Década de 1980:**\n"
    "* Criação do Conselho Nacional dos Direitos da Mulher (CNDM) em 1985.\n"
    "* Aprovação da Lei do Divórcio (Lei 6.515/1977) e da Lei dos Crimes Hediondos (Lei 8.072/1990), que incluía o feminicídio como crime hediondo.\n\n"
    "**Década de 1990:**\n"
    "* Aprovação da Lei Maria da Penha em 2006, marco na legislação de combate à violência contra as mulheres.\n"
    "* Criação do Programa Bolsa Família em 2003, que beneficia principalmente mulheres em situação de vulnerabilidade social.\n\n"
    "**Década de 2000:**\n"
    "* Aprovação da Lei de Cotas para Mulheres em Eleições em 1997, estabelecendo cotas mínimas de candidaturas femininas.\n"
    "* Criação do Programa Pronatec Mulheres em 2011, oferecendo cursos de qualificação profissional gratuitos para mulheres.\n\n"
    "**Década de 2010:**\n"
    "* Aprovação da Lei de Incentivo à Cultura com Linguagem de Gênero em 2021, promovendo a representação feminina em projetos culturais.\n"
    "* Criação do Ligue 180, uma linha direta nacional para denúncias de violência contra mulheres em 2013.\n\n"
    "**Evolução Recente:**\n"
    "Nos últimos anos, houve uma tendência crescente de fortalecimento das políticas públicas."
)

# Enviar a mensagem com o contexto inicial
response = chat_instance.send_message(contexto_inicial)
#print(response.text)

# Continuar a conversa dentro do mesmo contexto
response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
print(response.text)

# Loop de conversa contínua
prompt = input('olha me escreva algo: ')

while prompt.lower() != 'fim':
    response = chat_instance.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')
