#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from PIL import Image


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Criando imagens

# In[27]:


nome = 'bosque'
modelo = 'dall-e-3'
prompt = 'Crie uma imagem de um campo de pastagem, \
    amplo com uma leve elevação ao fundo.'
qualidade = 'hd'
style = 'natural'

resposta = client.images.generate(
    model=modelo,
    prompt=prompt,
    size='1024x1024',
    quality=qualidade,
    style=style,
    n=1
)


# In[28]:


print(resposta.data[0].revised_prompt)


# In[29]:


print(resposta.data[0].url)


# ### Salvar imagem

# In[30]:


nome_arquivo = f'arquivos/imagens/{nome}_{modelo}_{qualidade}_{style}.jpg'

image_url = resposta.data[0].url
img_data = requests.get(image_url).content
with open(nome_arquivo, 'wb') as f:
    f.write(img_data)


# ### Mostra imagem

# In[31]:


image = Image.open(nome_arquivo)
image.show()


# ## Editando imagens

# https://ai-image-editor.netlify.app/

# In[ ]:


resposta = client.images.edit(
    model='dall-e-2',
    image=open('arquivos/imagens/original.png', 'rb'),
    mask=open('arquivos/imagens/mask.png', 'rb'),
    prompt='Adicone uma vaca e um terneirinho na imagem fornecida',
    n=1,
    size='1024x1024'
)


# In[34]:


nome_arquivo = 'arquivos/imagens/editada.png'

image_url = resposta.data[0].url
img_data = requests.get(image_url).content
with open(nome_arquivo, 'wb') as f:
    f.write(img_data)


# In[35]:


image = Image.open(nome_arquivo)
image.show()


# ## Craindo Variações

# In[2]:


resposta = client.images.create_variation(
    image=open('arquivos/imagens/bosque_dall-e-3_hd_natural.jpg', 'rb'),
    n=1,
    size='1024x1024'
)


# In[3]:


nome_arquivo = 'arquivos/imagens/variacao.png'

image_url = resposta.data[0].url
img_data = requests.get(image_url).content
with open(nome_arquivo, 'wb') as f:
    f.write(img_data)


# In[4]:


image = Image.open(nome_arquivo)
image.show()


# In[ ]:




