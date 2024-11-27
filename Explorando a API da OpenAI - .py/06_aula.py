#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# In[3]:


client = openai.Client()


# In[4]:


mensagens = [{'role': 'user', 'content': 'crie uma história sobre uma viagem a marte'}]

resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    temperature=0,
    stream=True
)


# In[5]:


resposta_completa = ''
for stream_resposta in resposta:
    texto = stream_resposta.choices[0].delta.content
    if texto:
        resposta_completa += texto
        print(texto, end='')      


# In[6]:


print(resposta_completa)


# In[ ]:


print(resposta.choices[0].message.content)

