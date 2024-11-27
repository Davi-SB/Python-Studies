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

# In[3]:


file = client.files.create(
    file    = open('full_netflix_dataset.csv', 'rb'),
    purpose = 'assistants'
)
print(file)


# ### Cria o [assistant](https://platform.openai.com/docs/assistants/overview/agents)
# - `tool_resources` recebe os ids dos arquivos

# In[4]:


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

# In[5]:


myThread = client.beta.threads.create()
print(myThread, end='\n\n')

message = client.beta.threads.messages.create( # cria uma mensagem
    thread_id = myThread.id, # na thread especificada
    role = 'user',
    content = 'Gere um gráfico com o ano de lançamento dos filmes do catálogo da Netflix no eixo x e a quantidade de filmes lançados no eixo y. Considere apenas os filmes que foram lançados entre 2000 e 2024 e que estão disponíveis no Brasil.'
)
print(message)


# ### Roda a thread no assistant

# In[6]:


run = client.beta.threads.runs.create(
    thread_id    = myThread.id,
    assistant_id = DataAssistant.id,
    instructions = 'O nome do usuário é Davi Brilhante e ele está pensando em assinar o serviço de streaming da netflix.'
)
print(run)


# ### Aguarda a run terminar
# - [estados que uma run pode assumir](https://platform.openai.com/docs/assistants/deep-dive/run-lifecycle)

# In[7]:


while run.status in ['queued', 'in_progress', 'cancelling']:
    run = client.beta.threads.runs.retrieve( # recupera os dados da run 
        thread_id = myThread.id, # na thread especificada
        run_id = run.id # especifica qual run recuperar os dados
    )
    print(run.status)


# ### Verifica a resposta

# In[8]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id = myThread.id
    )
    print(mensagens)
else:
    print('Erro:', run.status)


# ### Analisando os passos do modelo

# In[9]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id = myThread.id,
  run_id = run.id
)


# In[10]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)


# In[17]:


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
        if message.content[0].type == 'text':
            print(message.content[0].text.value)
        elif message.content[0].type == 'image_file':
            file_id    = message.content[0].image_file.file_id
            image_data = client.files.content(file_id)
            try:
                with open('graficoGerado.png', 'wb') as f:
                    f.write(image_data.read())
                    print('Imagem salva com sucesso!')
            except Exception as e:
                print('Erro ao salvar a imagem:', e)

