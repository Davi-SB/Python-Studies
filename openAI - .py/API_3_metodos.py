#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# - **`max_tokens`:** limita o tamanho do output do modelo
# ---
# 
# - **`temperature` baixa (próxima de 0)**:
#   - O modelo será mais **determinístico** e **conservador**. Ele tenderá a escolher palavras com maior probabilidade, gerando respostas mais previsíveis e consistentes.
#   - Exemplos:
#     - Uma `temperature` de 0 ou próxima de 0 resultará em respostas bem focadas e diretas, com menos variação.
# 
# - **`temperature` alta (próxima de 1)**:
#   - O modelo será mais **aleatório** e **criativo**. Ele terá maior propensão a explorar opções menos prováveis, resultando em respostas mais variadas e inesperadas.
#   - Exemplos:
#     - Uma `temperature` de 1 ou próxima disso resultará em respostas mais criativas ou "livres", com mais variação na escolha de palavras e estrutura.
# 
# - **`temperature` acima de 1**:
#   - Valores maiores que 1 podem resultar em respostas ainda mais diversas, mas também mais erráticas e menos coerentes.
# 
#  
#  #
# - **`temperature` baixa (0-0.3)**: Respostas mais focadas, diretas e consistentes.
# - **`temperature` média (0.4-0.7)**: Equilíbrio entre consistência e criatividade.
# - **`temperature` alta (0.8-1)**: Respostas mais criativas, diversificadas e imprevisíveis.

# In[2]:


myChat = [
    {'role': 'user', 'content': 'faça uma piada curta'}
]

response = client.chat.completions.create(
    messages = myChat,
    model =  'gpt-3.5-turbo-0125',
    max_tokens = 500,
    temperature = 0
)


# Controle de gastos:

# In[4]:


response.usage


# Transdorma a mensagem já para o formato de dicionário, aí basta fazer o append no chat

# In[11]:


response.choices[0].message.model_dump()


# In[15]:


response.choices[0].message.model_dump(exclude_none=True)


# In[ ]:




