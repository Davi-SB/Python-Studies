#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

dataset = pd.read_csv('arquivos/supermarket_sales.csv')
dataset.head(5)


# In[23]:


dataset['Rating'].mean()


# In[4]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Cria o assistant

# In[5]:


file = client.files.create(
    file=open('arquivos/supermarket_sales.csv', 'rb'),
    purpose='assistants'
)


# In[7]:


assitant = client.beta.assistants.create(
    name="Analista Fianceiro",
    instructions='Você é um analista financeiro de um supermercado. Você deve utilizar os dados \
        .csv informados relativos as vendas do supermercado para realizar as suas análises.',
    tools=[{'type': 'code_interpreter'}],
    tool_resources={'code_interpreter': {'file_ids': [file.id]}},
    model='gpt-4o'
)


# ## Cria uma thread

# In[8]:


thread = client.beta.threads.create()


# ## Adiciona mensagem a thread criada

# In[27]:


texto_mensagem = 'Qual é o raqting médio das vendas do supermercado? O arquivo estáno formato csv.'
texto_mensagem = 'Gere um gráfico de pizza com o percentual de vendas por meio de pagamento. O arquivo está no formato csv.'

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content=texto_mensagem
)


# ## Roda a thread no assistant

# In[28]:


run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assitant.id,
    instructions='O nome do usuário é Adriano Soares e ele é um usuário Premium.'
)


# ## Aguarda a thread rodar

# In[29]:


import time

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )


# In[30]:


run.status


# ## Verifica a resposta

# In[31]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(mensagens)
else:
    print('Errro', run.status)


# In[33]:


print(mensagens.data[0].content[0])


# ## Analisando os passos do modelo

# In[34]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[39]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            print('-----')
            print(tool_call.code_interpreter.input)
            print('-----')
            print('Result')
            if tool_call.code_interpreter.outputs[0].type == 'logs':
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
            with open(f'arquivos/{file_id}.png', 'wb') as f:
                f.write(image_data.read())
                print(f'Imagem {file_id} salva')
            
            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg

            img = mpimg.imread(f'arquivos/{file_id}.png')
            fig, ax = plt.subplots()
            ax.set_axis_off()
            ax.imshow(img)
            plt.show()
    


# In[ ]:




