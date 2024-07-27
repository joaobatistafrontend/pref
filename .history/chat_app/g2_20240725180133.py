import google.generativeai as genai

chave = 'AIzaSyCTG0iYJKRv0D0FXBw3Ikai0FPfE68ZUSo'

genai.configure(api_key=chave)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        #print(f'nomes: {m.name}')
        pass

model = genai.GenerativeModel('gemini-1.0-pro-latest')
#resposta = model.generate_content('estou sofrendo violencia domestica')
#print(resposta.text)


chat = model.start_chat(history=[], '')
print(f'chat: {chat} \n')
prompt = input('olha me escreva algo: ')

while prompt != 'fim':
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input('olha me escreva algo: ')