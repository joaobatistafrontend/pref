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
"1. Legislação e Normas Leis federais e estaduais: Inclua leis como a Lei Maria da Penha, a Lei do Feminicídio, e outras legislações específicas que protegem os direitos das mulheres. Decretos e portarias: Documentos que regulamentam e detalham a aplicação das leis. Normas técnicas: Diretrizes que orientam a implementação de políticas públicas."
"2. Programas e Iniciativas Programas governamentais: Detalhes sobre programas federais, estaduais e municipais voltados para as mulheres, como apoio a vítimas de violência, programas de capacitação profissional, entre outros. Iniciativas de ONGs: Projetos e campanhas de organizações não-governamentais que apoiam as mulheres."
"3. Serviços Disponíveis Centros de Atendimento: Informações sobre centros de referência, delegacias especializadas, casas abrigo, e outros serviços de atendimento a mulheres. Telefones de Emergência: Números de telefone para suporte emergencial, como o 180 (Central de Atendimento à Mulher)."
"4. Estatísticas e Estudos Dados estatísticos: Estatísticas sobre violência contra a mulher, participação no mercado de trabalho, acesso à educação, entre outros. Estudos e pesquisas: Pesquisas acadêmicas e relatórios de instituições que abordam questões de gênero e políticas públicas."
"5. Direitos e Benefícios Direitos das mulheres: Informações sobre direitos trabalhistas, direitos reprodutivos, direitos à saúde, entre outros Benefícios sociais: Detalhes sobre benefícios sociais específicos para mulheres, como bolsa família, auxílio-maternidade, etc."
"6. Processos e Procedimentos Como acessar serviços: Passo a passo de como acessar determinados serviços e benefícios.Procedimentos legais: Orientações sobre como proceder em casos de violência, discriminação, entre outros."
"7. Educação e Capacitação Cursos e treinamentos: Informações sobre cursos gratuitos ou subsidiados voltados para mulheres. Campanhas educativas: Materiais e campanhas que promovam a conscientização sobre direitos e violência contra a mulher."
"8. Informações Regionais Especificidades locais: Políticas públicas, serviços e iniciativas específicas de cada região do país Fontes de Dados:Sites oficiais do governo: Ministérios, secretarias estaduais e municipais.Organizações internacionais: ONU Mulheres, Banco Mundial, entre outros.Instituições de pesquisa: IBGE, IPEA, universidades, e centros de pesquisa.Documentos legais: Disponíveis em diários oficiais e sites de legislação."
)

# Enviar a mensagem com o contexto inicial
response = chat_instance.send_message(f'o assunto que vamos conversa é sobre :{contexto_inicial}, me de um retorno do')
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
