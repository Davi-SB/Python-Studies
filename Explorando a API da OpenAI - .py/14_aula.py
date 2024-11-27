#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd

dataset = pd.read_csv('arquivos/supermarket_sales.csv')
dataset.head()


# In[54]:


dataset['Rating'].mean()


# In[ ]:


dataset['Rating'].mean()


# In[39]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Cria o assistant

# In[40]:


file = client.files.create(
    file=open('arquivos/supermarket_sales.csv', 'rb'),
    purpose='assistants'
)


# In[41]:


assistant = client.beta.assistants.create(
    name="Analista Fianceiro Supermercados Asimov",
    instructions="Você é um analista financeiro de um supermercado. Você utiliza os dados .csv relativo às vendas \
        do supermercado para realizar as suas análises",
    tools=[{'type': 'code_interpreter'}],
    file_ids=[file.id],
    model='gpt-4-turbo-preview'
)


# ## Cria uma thread

# In[42]:


thread = client.beta.threads.create()


# ## Adiciona mensagem a thread criada

# In[60]:


pergunta = 'Qual é o rating médio das vendas do nosso supermercado?'
pergunta = 'Gere um gráfico pizza com o percentual de vendas por meio de pagamento'

messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content=pergunta
)


# ## Roda a thread no assistant

# In[61]:


run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions='O nome do usuário é Adriano.'
)


# ## Aguarda a thread rodar

# In[62]:


import time

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

print(run.status)


# ## Verifica a resposta

# In[64]:


if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print('Erro', run.status)


# In[67]:


messages.data[0].content[0]


# ## Analisando os passos do modelo

# In[ ]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[83]:


for step in run_steps.data[::-1]:
    print('======= Step >', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            print('```')
            print(tool_call.code_interpreter.input)
            print('```')
            if tool_call.code_interpreter.outputs[0].type == 'logs':
                print('Result')
                print(tool_call.code_interpreter.outputs[0].logs)
    if step.step_details.type == 'message_creation':
        message = client.beta.threads.messages.retrieve(
            thread_id=thread.id,
            message_id=step.step_details.message_creation.message_id
        )
        if message.content[0].type == 'text':
            print(message.content[0].text.value)

        if message.content[0].type == 'image_file':
            file_id = message.content[0].image_file.file_id
            image_data = client.files.content(file_id)

            with open(f'arquivos/{file_id}.png', 'wb') as file:
                file.write(image_data.read())

            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg

            img = mpimg.imread(f'arquivos/{file_id}.png')
            fig, ax = plt.subplots()
            ax.set_axis_off()
            ax.imshow(img)
            plt.show()
        


# In[ ]:




