#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Cria o assistant

# In[2]:


file = client.files.create(
    file=open('arquivos/divulgacao_resultado_ambev_4T23.pdf', 'rb'),
    purpose='assistants'
)


# In[3]:


assistant = client.beta.assistants.create(
    name="Analista de Demonstrações Financeiras",
    instructions="Você é um analista de demonstralções \
        financeiras da Ambev. Você tem acesso a demontração \
        de resultado do 4º trimestre de 2023. Baseado apenas \
        no documento que você tem acesso, responda \
        as perguntas do usuário.",
    tools=[{'type': 'retrieval'}],
    file_ids=[file.id],
    model='gpt-4-turbo-preview'
)


# ## Cria uma thread

# In[4]:


thread = client.beta.threads.create()


# ## Adiciona mensagem a thread criada

# In[5]:


pergunta = 'Qual o volume de cerja vendido no Brasil segundo o documento?'

messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content=pergunta
)


# ## Roda a thread no assistant

# In[6]:


run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions='O nome do usuário é Adriano.'
)


# ## Aguarda a thread rodar

# In[7]:


import time

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

print(run.status)


# ## Verifica a resposta

# In[8]:


if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print('Erro', run.status)


# In[9]:


print(messages.data[0].content[0].text.value)


# ## Analisando os passos do modelo

# In[10]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[14]:


for step in run_steps.data[::-1]:
    print('======= Step >', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            if tool_call.type == 'retrieval':
                print(tool_call)
            else:
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
            message = client.beta.threads.messages.retrieve(
                thread_id=thread.id,
                message_id=step.step_details.message_creation.message_id
            )
            print(message.content[0].text.value)

        if message.content[0].type == 'image_file':
            message = client.beta.threads.messages.retrieve(
                thread_id=thread.id,
                message_id=step.step_details.message_creation.message_id
            )
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
        


# In[12]:


step.step_details


# In[13]:


tool_call


# In[ ]:




