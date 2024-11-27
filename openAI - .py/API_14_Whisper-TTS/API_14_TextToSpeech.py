#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# ### [Text to speech](https://platform.openai.com/docs/guides/text-to-speech)

# In[2]:


text = """ Oi! esse é um teste de conversão de texto em fala. Se liga nesse trava língua: casa suja, 
chão sujo, casa suja, chão sujo, casa suja, chão sujo. E você? tem algum 
trava língua para me contar?"""

resposta = client.audio.speech.create(
    model = 'tts-1',
    voice = 'onyx',
    input = text
)

resposta.write_to_file("AudioGerado - Onyx.mp3")


# In[3]:


with client.audio.speech.with_streaming_response.create(
    model = 'tts-1',
    voice = 'shimmer',
    input = text
) as resposta:
    resposta.stream_to_file("AudioGerado - Shimmer.mp3")


# The default response format is "mp3", but other formats like "opus", "aac", "flac", and "pcm" are available.

# In[ ]:


resposta = client.audio.speech.create(
    model = 'tts-1',
    voice = 'echo',
    # O texto abaixo é um exemplo mais complicado para reconhecimento de fala
    input = """Eu acho que... é... hm.. na verdad-de eu não sei o que dizer, mas... é isso, 
    Vou passar a palavra para Szczęśniewski"""
)

resposta.write_to_file("AudioGeradoDificil - Echo.mp3")

