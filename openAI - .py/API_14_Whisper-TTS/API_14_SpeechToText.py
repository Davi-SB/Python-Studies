#!/usr/bin/env python
# coding: utf-8

# In[3]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# ### [Speech to text](https://platform.openai.com/docs/guides/speech-to-text)
# 
# - File uploads are currently limited to 25 MB and the following input file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.

# In[4]:


transcricao = client.audio.transcriptions.create(
    model = 'whisper-1',
    file = open('AudioGeradoDificil - Echo.mp3', 'rb'),
    
    ### not required:
    # se não for definido, o modelo tentará detectar
    language = 'pt', 
    
    # se não for definido, o modelo retornará um JSON. 
    # outras opções são 'text' e 'srt' para legendas
    response_format = 'text',
    
    # pode ser usado para fornecer contexto ao modelo e evitar erros
    prompt = """Transcreva o áudio para texto removendo as marcas de linguagem e sabendo que os nomes dos
    professores Mlwati, Dziedzic, Szczęśniewski e Echevarría podem estar envolvidos na fala"""
)

print(transcricao)


# In[8]:


transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file = open('AudioGerado - Onyx.mp3', 'rb')
)

print(transcricao, end='\n\n')
print(transcricao.text)


# ### Tradução
#  Apenas disponível de qualquer língua suportada para o inglês

# In[ ]:


traducao = client.audio.translations.create(
    model = 'whisper-1',
    file = open('AudioGerado - Shimmer.mp3', 'rb'),
)

print(traducao.text, end='\n\n')


# ### .srt para exportar com formato para legendas

# In[10]:


transcricao = client.audio.transcriptions.create(
    model = 'whisper-1',
    file = open('AudioGerado - Shimmer.mp3', 'rb'),
    response_format='srt'
)

print(transcricao, end='\n\n')

