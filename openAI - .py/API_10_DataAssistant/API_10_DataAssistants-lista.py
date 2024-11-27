#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# In[2]:


import pandas as pd

dataset = pd.read_csv('full_netflix_dataset.csv')
dataset.head(3)


# ### Cria o arquivo para ser enviado

# In[6]:


file = client.files.create(
    file    = open('full_netflix_dataset.csv', 'rb'),
    purpose = 'assistants'
)
print(file)


# ### Cria o [assistant](https://platform.openai.com/docs/assistants/overview/agents)
# - `tool_resources` recebe os ids dos arquivos

# In[8]:


DataAssistant = client.beta.assistants.create(
    name = "Engenheiro de Dados",
    instructions = 'Você é um Engenheiro de Dados que trabalha para a Netflix. Você recebeu o arquivo .CSV full_netflix_dataset.csv com informações importantes sobre o catálogo da Netflix. Sua tarefa é analisar o arquivo e responder as perguntas sobre os dados.',
    tools = [{'type': 'code_interpreter'}],
    tool_resources = {'code_interpreter': 
                        {'file_ids': 
                            [file.id]
                        }
                     },
    model = 'gpt-4o-mini'
)


# ### Cria e adiciona a mensagem em myThread

# In[9]:


myThread = client.beta.threads.create()
print(myThread, end='\n\n')

message = client.beta.threads.messages.create( # cria uma mensagem
    thread_id = myThread.id, # na thread especificada
    role = 'user',
    content = 'Liste todos os elementos do catálogo da Netflix com maior nota imdb que estão disponíveis no Brasil e possuem mais de um milhão de votos. Ordene a lista resposta por nota imdb de forma decrescente e mostre qual foi.'
)
print(message)


# ### Roda a thread no assistant

# In[10]:


run = client.beta.threads.runs.create(
    thread_id    = myThread.id,
    assistant_id = DataAssistant.id,
    instructions = 'O nome do usuário é Davi Brilhante e ele está pensando em assinar o serviço de streaming da netflix.'
)
print(run)


# ### Aguarda a run terminar
# - [estados que uma run pode assumir](https://platform.openai.com/docs/assistants/deep-dive/run-lifecycle)

# In[11]:


while run.status in ['queued', 'in_progress', 'cancelling']:
    run = client.beta.threads.runs.retrieve( # recupera os dados da run 
        thread_id = myThread.id, # na thread especificada
        run_id = run.id # especifica qual run recuperar os dados
    )
    print(run.status)


# ### Verifica a resposta

# In[12]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id = myThread.id
    )
    print(mensagens)
else:
    print('Erro:', run.status)


# ### Acesso de mensagens
# 
# <details>
#   <summary>------- Output Esperado -------</summary>
# 
#   - Breaking Bad
#   - The Godfather
#   - Pulp Fiction
#   - Forrest Gump
#   - Stranger Things
#   - Terminator 2: Judgment Day
#   - Saving Private Ryan
#   - Whiplash
#   - Django Unchained
#   - Eternal Sunshine of the Spotless Mind
#   - Shutter Island
#   - The Walking Dead
#   - The Hunger Games
# </details>
# 
# 

# In[15]:


for mensagem in mensagens.data[::-1]:
    role    = mensagem.role
    content = mensagem.content[0].text.value
    print(f'    {role}: {content}', end='\n\n')


# ### Analisando os passos do modelo

# In[16]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id = myThread.id,
  run_id = run.id
)


# In[19]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)


# In[18]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)
    
    if step.step_details.type == 'tool_calls':
            for tool_call in step.step_details.tool_calls:
                print('-----')
                print(tool_call.code_interpreter.input)
                print('-----')
                # print('Result')
                # print(tool_call.code_interpreter.outputs[0].logs)
                
    if step.step_details.type == 'message_creation':
        message = client.beta.threads.messages.retrieve(
            thread_id  = myThread.id,
            message_id = step.step_details.message_creation.message_id
        )
        print(message.content[0].text.value)

