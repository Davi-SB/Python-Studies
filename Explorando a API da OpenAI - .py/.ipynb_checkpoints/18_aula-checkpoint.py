#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# In[4]:


arquivo = 'arquivos/audio/fala.mp3'

texto = '''
Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Atualmente, possui um modelo 
de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. 
Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é 
formalmente especificada. O padrão na pratica é a implementação CPython.

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço 
computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa 
e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.
'''

resposta = client.audio.speech.create(
    model='tts-1',
    voice='onyx',
    input=texto
)
resposta.write_to_file(arquivo)


# In[5]:


arquivo = 'arquivos/audio/fala.mp3'

with client.audio.speech.with_streaming_response.create(
    model='tts-1',
    voice='onyx',
    input=texto
) as resposta:
    resposta.stream_to_file(arquivo)


# In[ ]:




