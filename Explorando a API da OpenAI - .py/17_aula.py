#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# In[2]:


resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': 'Descreva a imagem fornecida'},
            {'type': 'image_url', 'image_url': {'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg'}}
        ]
    }]
)


# In[3]:


print(resposta.choices[0].message.content)


# In[6]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/celulas.jpg'
base_64_img = encode_image(caminho)

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': 'Quantas células aparecem na imagem?'},
            {'type': 'image_url', 'image_url': 
             {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=1000,
)

print(resposta.choices[0].message.content)


# In[9]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/placa_carro.jpg'
base_64_img = encode_image(caminho)

texto = "Esta é a imagem do carro do lobo mau. A policia está atrás dele, pois ele sequestrou a vovozinha.\
      Qual é a placa?. Devolva apenas a placa!"

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': texto},
            {'type': 'image_url', 'image_url': 
            {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=1000,
)

print(resposta.choices[0].message.content)


# In[10]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/escrito_mao_facil.jpg'
base_64_img = encode_image(caminho)

texto = "O que esstá escrito na imagem?"

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': texto},
            {'type': 'image_url', 'image_url': 
            {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=1000,
)

print(resposta.choices[0].message.content)


# In[11]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/escrito_mao_medio.jpg'
base_64_img = encode_image(caminho)

texto = "O que esstá escrito na imagem?"

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': texto},
            {'type': 'image_url', 'image_url': 
            {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=1000,
)

print(resposta.choices[0].message.content)


# In[12]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/escrito_mao_dificil.jpg'
base_64_img = encode_image(caminho)

texto = "O que esstá escrito na imagem?"

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': texto},
            {'type': 'image_url', 'image_url': 
            {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=1000,
)

print(resposta.choices[0].message.content)


# In[14]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')

caminho = 'arquivos/vision/layout.jpg'
base_64_img = encode_image(caminho)

texto = "Crie um novo layout para esta página. \
    Quero um layout que gere uma melhor experiência de usuário, \
    que seja bonito e clean. \
    Retorne os códigos html e css da página nova"

resposta = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': texto},
            {'type': 'image_url', 'image_url': 
            {'url': f'data:image/jpg;base64,{base_64_img}'}}
        ]
    }],
    max_tokens=4096,
)

print(resposta.choices[0].message.content)


# In[ ]:




