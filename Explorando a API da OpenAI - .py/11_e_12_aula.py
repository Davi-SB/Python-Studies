#!/usr/bin/env python
# coding: utf-8

# ### Resposta que gostaríamos do modelo

# ```
# {
#   "resposta": "Equação quadrática é uma equação polinomial de segundo grau, com a forma ax² + bx + c = 0.",
#   "categoria": "Matemática",
#   "fonte": "AsimoBot"
# }
# ```

# ### Resposta que o modelo está nos dando

# Uma equação quadrática é uma equação polinomial de segundo grau, ou seja, uma equação na forma ax^2 + bx + c = 0, onde a, b e c são constantes e a é diferente de zero. A incógnita da equação é x e o objetivo é encontrar os valores de x que satisfazem a equação. As equações quadráticas podem ter duas soluções reais, uma solução real ou duas soluções complexas.

# ### Prompt para que ele nos dê a mensagem formatada como queremos

# system_mes = '''
# Responda as perguntas em um parágrafo de até 20 palavras. Categorize as respostas no seguintes conteúdos: física, matemática, língua portuguesa ou outros.
# Retorne a resposta em um formato json, com as keys: 
# fonte: valor deve ser sempre AsimoBot
# resposta: a resposta para a pergunta
# categoria: a categoria da pergunta
# '''

# ### Formatação das mensagens para realizarmos o Fine Tuning

# ```
# {"messages": 
#     [
#         {"role": "user", "content": "O que é uma equação quadrática"},
#         {"role": "assistant", "content": 
#             {
#                 "resposta": "Equação quadrática é uma equação polinomial de segundo grau, com a forma ax² + bx + c = 0.",
#                 "categoria": "Matemática",
#                 "fonte": "AsimoBot"
#             }},
#     ]
# }
# 
# ```

# ### Criando o arquivo JSONL

# In[4]:


import json

with open('arquivos/chatbot_respostas.json', encoding="utf8") as f:
    json_respostas = json.load(f)


# In[9]:


with open('arquivos/chatbot_respostas.jsonl', 'w', encoding="utf8") as f:
    for entrada in json_respostas:
        resposta = {
            'resposta': entrada['resposta'],
            'categoria': entrada['categoria'],
            'fonte': 'AsimoBot'
        }
        entrada_jsonl = {
            'messages': [
                {'role': 'user', 'content': entrada['pergunta']},
                {'role': 'assistant', 'content': json.dumps(resposta, ensure_ascii=False, indent=2)}
            ]
        }
        json.dump(entrada_jsonl, f, ensure_ascii=False)
        f.write('\n')


# In[10]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# In[12]:


file = client.files.create(
    file=open('arquivos/chatbot_respostas.jsonl',  'rb'),
    purpose='fine-tune'
)

client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)


# In[13]:


client.fine_tuning.jobs.list()


# ### Utilizando o Modelo

# In[14]:


mensagens = [{'role': 'user', 'content': 'O que é uma equação quadrática?'}]

resposta = client.chat.completions.create(
    messages=mensagens,
    model="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0
)

print(resposta.choices[0].message.content)


# In[15]:


system_mes = '''
Responda as perguntas em um parágrafo de até 20 palavras. Categorize as respostas no seguintes conteúdos: física, matemática, língua portuguesa ou outros.
Retorne a resposta em um formato json, com as keys: 
fonte: valor deve ser sempre AsimoBot
resposta: a resposta para a pergunta
categoria: a categoria da pergunta
'''

mensagens = [
    {'role': 'system', 'content': system_mes},
    {'role': 'user', 'content': 'O que é uma equação quadrática?'}
    ]

resposta = client.chat.completions.create(
    messages=mensagens,
    model="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0
)

print(resposta.choices[0].message.content)


# In[17]:


resposta.usage


# In[18]:


mensagens = [
    {'role': 'user', 'content': 'O que é uma equação quadrática?'}
    ]

resposta = client.chat.completions.create(
    messages=mensagens,
    model="ft:gpt-3.5-turbo-0125:personal::971R86c5",
    max_tokens=1000,
    temperature=0
)

print(resposta.choices[0].message.content)


# In[19]:


resposta.usage


# In[ ]:




