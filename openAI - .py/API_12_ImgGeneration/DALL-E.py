#!/usr/bin/env python
# coding: utf-8

# In[12]:


import openai
from dotenv import load_dotenv, find_dotenv

# Novos imports
import requests
from PIL import Image

load_dotenv(find_dotenv())
client = openai.Client()


# ### Criando imagens
# - [Pricing dos modelos de imagem](https://openai.com/api/pricing/#:~:text=2%5E30%20bytes.-,Image%20models,-Build%20DALL%C2%B7E%20directly)
# - The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. **This param is only supported for dall-e-3**.

# In[ ]:


resposta = client.images.generate(
    model   = 'dall-e-3',
    prompt  = """Crie uma imagem de Um astronauta flutuando em um planeta alienígena, com
    um céu colorido cheio de estrelas e nebulosas, e uma paisagem surreal ao fundo.""",
    size    = '1024x1024',
    quality = 'standard', # not required, por padrão é 'standard'
    style   = 'vivid',
    n       =  1
)


# In[ ]:


print(resposta)


# In[ ]:


print(resposta.data[0].revised_prompt)


# In[ ]:


print(resposta.data[0].url)


# ### Salvar imagem

# In[ ]:


# Uso de requests
img_data = requests.get(resposta.data[0].url).content

with open('ImagemGerada.png', 'wb') as f:
    f.write(img_data)


# # Editando imagens

# - Para editar uma imagem, é necessário criar um mask, deixar em vazio a parte quem que a IA vai editar.
# - Até o momento, disponível apenas para o DALL-E 2
# - [Site que faz isso](https://ai-image-editor.netlify.app/)

# In[15]:


resposta = client.images.edit(
    model  = 'dall-e-2',
    image  = open('original.png', 'rb'),
    mask   = open('masked.png', 'rb'),
    prompt = """Adicione o fogo das turbinas do foguete.""",
    n      = 1,
    size   = '1024x1024'
)


# In[ ]:


print(resposta.data[0].revised_prompt)
print(resposta.data[0].url)
# obs: o resultado da ediçao ficou ruim mesmo


# In[17]:


img_data = requests.get(resposta.data[0].url).content

with open("ImagemEditadaGerada.png", 'wb') as f:
    f.write(img_data)


# ### Craindo Variações

# In[18]:


resposta = client.images.create_variation(
    image = open('ImagemGerada.png', 'rb'),
    n     = 1,
    size  = '1024x1024'
)


# In[19]:


print(resposta.data[0].revised_prompt)
print(resposta.data[0].url)


# In[20]:


img_data = requests.get(resposta.data[0].url).content

with open("ImagemGeradaVariacao.png", 'wb') as f:
    f.write(img_data)

