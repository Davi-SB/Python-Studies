import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

def add_assistant_message(chat, content):
    chat.append({'role': 'assistant', 'content': content})
    return chat

def add_user_message(chat, content, model='gpt-3.5-turbo-0125', max_tokens=500, temperature=0):
    chat.append({'role': 'user', 'content': content})
    generate_response(chat, model, max_tokens, temperature)
    return chat

def generate_response(chat, model='gpt-3.5-turbo-0125', max_tokens=500, temperature=0):
    response = client.chat.completions.create(
        messages = chat,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
    )
    add_assistant_message(chat, response.choices[0].message.content)
    
def print_chat(chat, file=None):
    for message in chat:
        role = message['role']
        content = message['content']
        if role == 'user': said = 'asked'
        else: said = 'awnsered'
        output = f"{role.capitalize()} {said}:\n{content}\n" + ('-'*40) + '\n'
        print(output, end='')
        if file:
            file.write(output)

myChat = []
while True:
    text = input("Digite sua mensagem: ")
    if text.upper() == 'STOP': break
    print(chr(27) + "[2J") # limpa o terminal
    myChat = add_user_message(myChat, text)
    print_chat(myChat)
    
with open('chat.txt', 'w') as f:
    print_chat(myChat, file=f)
    
#faltam 8min