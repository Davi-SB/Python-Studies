#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# - `content` do gpt vision é diferente, é composto por um texto e uma url de imagem

# In[4]:


resposta = client.chat.completions.create(
    model='gpt-4o',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': 'Descreva a imagem fornecida e transcreva o texto dela, se houver.'},
            {'type': 'image_url', 'image_url': {'url': 'https://blog.decorlumen.com.br/wp-content/uploads/2023/07/1-3.jpg'}}
        ]
    }]
)


# In[5]:


print(resposta.choices[0].message.content)


# ### Converter uma imagem local em `base64`, decodificação que funciona também

# In[6]:


import base64

def encode_image(caminho_imagem):
    with open(caminho_imagem, 'rb' ) as img:
        return base64.b64encode(img.read()).decode('utf-8')


# In[10]:


base_64_img = encode_image("Sala de espera.jpeg")

texto = """A imagem mostra a sala de espera de um hospital. Identifique a quantidade de pessoas nessa sala no total. 
Além disso, você deve estimar o tempo de espera atual para ser atendido. Para isso você deve considerar a 
quantidade de pacientes, ou seja, não considerar médicos ou funcionários. Além disso, desconsidere as crianças, 
pois elas não estão esperando por atendimento médico. Para cada paciente, adicione 15min ao tempo de espera."""

resposta = client.chat.completions.create(
    model='gpt-4o',
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

