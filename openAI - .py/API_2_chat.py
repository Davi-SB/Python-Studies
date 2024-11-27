#!/usr/bin/env python
# coding: utf-8

# Dessa forma a key é usada no código e fica escondida. openai.Client procura uma variável chamada "OPENAI_API_KEY" nas variáveis de ambiente (enviroment) e usa ela como valor da key

# In[35]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# In[36]:


client = openai.Client()


# In[37]:


myChat = [
    {'role': 'user', 'content': 'faça uma piada curta'}
]

response = client.chat.completions.create(
    messages = myChat,
    model =  'gpt-3.5-turbo-0125',
    max_tokens = 500,
    temperature = 0
)


# output_text.choices[0].message.content --> onde fica a resposta à pergunta
# para adicionar essa resposta ao chat para poder continuar a conversa, é adicionado um novo dicionário com o role sendo o assistant (ou seja, o content veio do "chatGPT") e com o conteúdo sendo a resposta.
# 
# ## myChat --> lista de dicionários

# In[38]:


print(f"resposta do modelo: {response.choices[0].message.content}")

myChat.append({'role': 'assistant', 'content': response.choices[0].message.content})
print(f"\nchat atual: \n{myChat}")

