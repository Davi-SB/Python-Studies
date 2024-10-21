import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

def generate_response(chat, model='gpt-4o-mini', temperature=0.3, max_tokens=1000, stream = True):
    return client.chat.completions.create(
        messages = chat,
        model = model,
        temperature = temperature,
        max_tokens= max_tokens,
        stream = stream
    )

def print_stream_response(response):
    full_response = ''
    print('\nBoardGPT: ', end='')
    for steam_response in response:
        token = steam_response.choices[0].delta.content
        if token:
            full_response += token
            print(token, end='')
    print()
    return full_response

def export_chat(chat):
    with open('chat.md', 'w', encoding='utf-8') as file:
        for message in chat:
            file.write(f"{message['role']}: {message['content']}\n\n")
    

if __name__ == '__main__':
    chat = [{'role': 'system', 'content': 'Você é um especialista em jogos de tabuleiro. Sua função é explicar regras, sugerir jogos, dar dicas estratégicas e propor variações criativas para melhorar a experiência dos jogadores. Baseie suas recomendações no tipo de jogo, número de jogadores e preferências de duração ou tema, ajudando tanto novatos quanto veteranos a aproveitarem ao máximo os jogos'}]

    print('--- Bem-vindo ao BoardGPT, seu assistente especializado em jogos de tabuleiro. ---')

    line = ''
    while True:
        line = input('\nVocê: ')
        if line.upper() == 'STOP': break
        if not line: continue
        
        # adiciona pergunta ao chat
        chat.append({'role': 'user', 'content': line})
        
        # gera resposta
        response = generate_response(chat)
        
        # printa resposta
        full_response = print_stream_response(response)
        
        # adiciona resposta ao chat 
        chat.append({'role': 'assistant', 'content': full_response})
        
    # salva chat em arquivo
    export_chat(chat)