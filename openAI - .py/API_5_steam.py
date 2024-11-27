#!/usr/bin/env python
# coding: utf-8

# In[44]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()

chat = [{'role': 'user', 'content': 'me conte uma história de 150 palavras'}]

resposta = client.chat.completions.create(
    model = "gpt-3.5-turbo-0125",
    messages = chat, 
    max_tokens = 500,
    temperature = 1.5,
    stream = True # faz a API retornar a resposta assim que ela estiver pronta
)


# `resposta` agora é uma stream e não pode ser usada como antes (`resposta.choices[0].message.content`). Os pedaços devem ser concatenados para ter a mensagem completa

# In[45]:


resposta


# `steam = True` libera um iterator para a resposta que pode ser acessada como no for abaixo. Na última iteração, o token é `None`. por isso, `if token:` é usado para evitar que ele seja printado. Isso dá o efeito do texto sendo escrito e não deixa o usuário esperando

# In[46]:


resposta_completa = ''
for stream_resposta in resposta: 
    token = stream_resposta.choices[0].delta.content
    if token:
        resposta_completa += token
        print(token, end='')


# In[47]:


print(resposta_completa)

