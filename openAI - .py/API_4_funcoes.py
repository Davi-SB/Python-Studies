#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# In[2]:


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
    
def print_chat(chat):
    for message in chat:
        role = message['role']
        content = message['content']
        if role == 'user': said = 'asked'
        else: said = 'awnsered'
        print(f"{role} said: {content}", end='\n'+('-'*40)+'\n')


# In[3]:


myChat = []
while True:
    text = input()
    if text == 'STOP': break
    print(chr(27) + "[2J") # limpa o terminal
    myChat = add_user_message(myChat, text)
    print_chat(myChat)

