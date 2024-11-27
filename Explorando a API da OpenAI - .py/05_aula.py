#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


# In[2]:


client = openai.Client()


# In[3]:


mensagens = [{'role': 'user', 'content': 'O que é uma maçã em 5 palavras?'}]

resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    temperature=0
)


# In[4]:


print(resposta.choices[0].message.content)


# In[ ]:


mensagens.append({'role': 'user', 'content': 'E qual é a sua cor?'})


# In[ ]:


mensagens


# In[ ]:


resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    temperature=0
)


# In[ ]:


print(resposta.choices[0].message.content)


# ## Adicionando a uma função

# In[ ]:


def geracao_texto(mensagens, model='gpt-3.5-turbo-0125', max_tokens=1000, temperature=0):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature
    )
    print(resposta.choices[0].message.content)
    mensagens.append(resposta.choices[0].message.model_dump(exclude_none=True))
    return mensagens


# In[ ]:


mensagens = [{'role': 'user', 'content': 'O que é uma maçã em 5 palavras?'}]
mensagens = geracao_texto(mensagens)


# In[ ]:


mensagens.append({'role': 'user', 'content': 'E qual é a sua cor?'})
mensagens = geracao_texto(mensagens)


# ## Explorando classe de resposta

# In[ ]:


mensagens = [{'role': 'user', 'content': 'O que é uma maçã em 5 palavras?'}]
resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    temperature=0
)


# In[ ]:


resposta.usage


# In[ ]:


resposta.choices[0].message


# In[ ]:


resposta.choices[0].message.model_dump(exclude_none=True)


# ## Explorando max_tokens e temperature

# In[ ]:


mensagens = [{'role': 'user', 'content': 'O que é uma maçã em 5 palavras?'}]
mensagens = geracao_texto(mensagens, max_tokens=3)


# In[ ]:


mensagens = [{'role': 'user', 'content': 'O que é uma maçã?'}]
mensagens = geracao_texto(mensagens, temperature=2)


# In[ ]:




