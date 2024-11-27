#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# In[3]:


audio = open('arquivos/audio/audio_asimov.mp3', 'rb')
transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio
)
print(transcricao.text)


# In[4]:


audio = open('arquivos/audio/audio_asimov.mp3', 'rb')
transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio,
    prompt='Essa é a transcrição de uma aula da Asimov Academy.\
          O professor se chama Rodrigo Soares Tadewald.'
)
print(transcricao.text)


# In[7]:


audio = open('arquivos/audio/audio_asimov.mp3', 'rb')
transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio,
    prompt='Essa é a transcrição de uma aula da Asimov Academy.\
          O professor se chama Rodrigo Soares Tadewald.',
    response_format='srt'
)
print(transcricao)


# In[8]:


audio = open('arquivos/audio/audio_asimov.mp3', 'rb')
transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio,
    prompt='Essa é a transcrição de uma aula da Asimov Academy.\
          O professor se chama Rodrigo Soares Tadewald.',
    response_format='text',
    language='pt',
)
print(transcricao)


# In[ ]:




