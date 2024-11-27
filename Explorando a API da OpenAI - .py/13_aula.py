#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Cria o assistant

# In[2]:


assitant = client.beta.assistants.create(
    name="Tutor de Matemática da Asimov",
    instructions='Você é um tutor pessoal de matemática da empresa Asimov. \
        Escreva e execute códigos para responder as perguntas de matemática que lhe forem passadas.',
    tools=[{'type': 'code_interpreter'}],
    model='gpt-3.5-turbo-0125'
)


# ## Cria uma thread

# In[3]:


thread = client.beta.threads.create()


# ## Adiciona mensagem a thread criada

# In[4]:


message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content='Se eu jogar um dado honesto 1000 vezes, qual é a probabilidade de eu obter exatamente 150 vezes o número 6? Resolva com um código'
)


# ## Roda a thread no assistant

# In[5]:


run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assitant.id,
    instructions='O nome do usuário é Adriano Soares e ele é um usuário Premium.'
)


# ## Aguarda a thread rodar

# In[6]:


import time

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )


# In[7]:


run.status


# ## Verifica a resposta

# In[8]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(mensagens)
else:
    print('Errro', run.status)


# In[9]:


print(mensagens.data[0].content[0].text.value)


# ## Analisando os passos do modelo

# In[ ]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[14]:


for step in run_steps.data:
    print('=== Step:', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            print('-----')
            print(tool_call.code_interpreter.input)
            print('-----')
            print('Result')
            print(tool_call.code_interpreter.outputs[0].logs)
    


# In[16]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            print('-----')
            print(tool_call.code_interpreter.input)
            print('-----')
            print('Result')
            print(tool_call.code_interpreter.outputs[0].logs)
    if step.step_details.type == 'message_creation':
        message = client.beta.threads.messages.retrieve(
            thread_id=thread.id,
            message_id=step.step_details.message_creation.message_id
        )
        print(message.content[0].text.value)
    


# In[ ]:




