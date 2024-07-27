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
# Verifique se o método start_chat aceita o contexto
# e inicialize o chat com o contexto definido
try:
    chat_instance = model.start_chat(context="políticas públicas para as mulheres")
except TypeError:
    print("O método start_chat não aceita o argumento 'context'. Verifique a documentação da biblioteca.")

# Se o chat_instance foi criado com sucesso, envie uma mensagem
if 'chat_instance' in locals():
    response = chat_instance.send_message("Quais são as principais políticas públicas para as mulheres no Brasil?")
    print(response.text)
else:
    print("Não foi possível iniciar o chat.")
