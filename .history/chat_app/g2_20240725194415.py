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

    "* Aprovação da Lei de Cotas para Mulheres em Eleições em 1997, estabelecendo cotas mínimas de candidaturas femininas.\n"
    "* Criação do Programa Pronatec Mulheres em 2011, oferecendo cursos de qualificação profissional gratuitos para mulheres.\n"
    "* Aprovação da Lei do Feminicídio (Lei 13.104/2015), classificando o feminicídio como uma forma de homicídio qualificado.\n\n"

    "* Aprovação da Lei de Incentivo à Cultura com Linguagem de Gênero em 2021, promovendo a representação feminina em projetos culturais.\n"
    "* Criação do Ligue 180, uma linha direta nacional para denúncias de violência contra mulheres em 2013.\n"
    "* Lei da Importunação Sexual (Lei 13.718/2018), combatendo o assédio sexual e outras formas de importunação.\n"
    "* Plano Nacional de Políticas para as Mulheres (PNPM), promovendo a igualdade de gênero e os direitos das mulheres.\n"
    "* Política Nacional de Saúde Mental e Direitos das Mulheres, abordando necessidades específicas das mulheres em saúde mental.\n"
    "* Medidas para Promover a Igualdade de Gênero no Mercado de Trabalho, como a redução da desigualdade salarial e promoção de oportunidades iguais.\n\n"

    "* Ações para fortalecer a proteção das mulheres vítimas de violência, como a Lei de Proteção e Defesa dos Direitos das Mulheres em Situação de Violência (Lei 13.491/2017).\n"
    "* Programas de Empoderamento Econômico, incluindo microcrédito e apoio a empreendimentos femininos.\n"
    "* Políticas de Saúde Reprodutiva, garantindo acesso a serviços de planejamento familiar e suporte durante a gravidez e parto.\n\n"

    "* Análise dos desafios persistentes nas políticas públicas e áreas onde melhorias são necessárias.\n"
    "* Exemplos de boas práticas e inovações em políticas públicas voltadas para mulheres em outros países que podem servir como modelo.\n\n"
    
    "* Diferenças regionais nas políticas públicas e desafios específicos enfrentados em áreas rurais ou urbanas.\n"
    "* Impacto das políticas em diferentes grupos sociais, incluindo negras, indígenas e mulheres em situação de vulnerabilidade.\n\n"

    "* **Identificação de Necessidades e Dúvidas Comuns:** Realizar pesquisas para identificar perguntas frequentes e necessidades específicas das mulheres em relação a políticas públicas, saúde, direitos e suporte social. Coletar feedback de usuárias para ajustar e melhorar o atendimento.\n"
    "* **Treinamento com Dados Relevantes:** Fornecer à IA informações detalhadas e atualizadas sobre políticas públicas voltadas para mulheres, leis, programas de apoio e serviços disponíveis. Incluir dados sobre situações específicas como violência doméstica e saúde reprodutiva.\n"
    "* **Criação de Scripts e Fluxos de Conversa:** Desenvolver scripts e fluxos de conversa para abordar uma ampla gama de tópicos e cenários, desde informações básicas até situações complexas que exigem suporte emocional ou informações detalhadas.\n"
    "* **Inclusão de Recursos de Suporte e Referência:** Fornecer links para recursos externos, números de telefone para serviços de emergência e materiais educativos sobre direitos das mulheres e outros tópicos relevantes.\n"
    "* **Desenvolvimento de Empatia e Sensibilidade:** Ensinar a IA a responder de maneira empática e sensível, especialmente em tópicos delicados. Utilizar técnicas de processamento de linguagem natural para reconhecer e responder adequadamente a emoções expressas pelos usuários.\n"
    "* **Implementação de Testes e Validações:** Realizar testes com usuárias reais para validar a eficácia das respostas e ajustar a IA com base no feedback. Monitorar e ajustar continuamente o sistema com base em novas informações e mudanças nas políticas públicas.\n"
    "* **Capacitação e Atualização Constante:** Manter a IA atualizada com as últimas mudanças nas políticas públicas e realizar treinamentos contínuos para lidar com novas questões e contextos emergentes.\n"
    "* **Abordagem Multicanal:** Garantir que o chatbot esteja acessível em múltiplos canais, como sites, aplicativos móveis e redes sociais, para alcançar um público mais amplo.\n"
    "* **Garantia de Privacidade e Segurança:** Assegurar que o sistema respeite a privacidade dos usuários e proteja suas informações pessoais de acordo com as regulamentações de proteção de dados.\n"
    "* **Inclusão de Aspectos Culturais e Regionais:** Considerar as diferenças culturais e regionais nas políticas e necessidades das mulheres, adaptando as respostas para refletir essas variáveis."
)

# Enviar a mensagem com o contexto inicial
response = chat_instance.send_message(f'o assunto que vamos conversa é sobre :{contexto_inicial}, eu sou uma mulher que preciso de suporte sobre esses assuntos')
#print(response.text)

# Continuar a conversa dentro do mesmo contexto
#response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
#print(response.text)

# Loop de conversa contínua
prompt = input('olha me escreva algo: ')
senti = model.analyze(prompt)
print(f'sentimentos {senti}')
while prompt.lower() != 'fim':
    response = chat_instance.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')
