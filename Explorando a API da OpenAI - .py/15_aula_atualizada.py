#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


# ## Cria o assistant

# In[2]:


vector_store = client.beta.vector_stores.create(name = 'Apostilas Asimov Aula 15')


# In[3]:


files = ['arquivos/Explorando a API da OpenAI.pdf',
         'arquivos/Explorando o Universo das IAs com Hugging Face.pdf']
file_stream = [open(f, 'rb') for f in files]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_stream
)


# In[4]:


print(file_batch.status)
print(file_batch.file_counts)


# In[5]:


assitant = client.beta.assistants.create(
    name="Tutor Asimov",
    instructions="Você é um tutor de uma escola de programação. Você é ótimo para responder \
        perguntas teóricas sobre a api da OpenAI e sobre a utilização da biblioteca do Hugging \
        Face com Python. Você utiliza as apostilas dos cursos para basear suas respostas. Caso \
        você não encontre as respostas nas apostilas informadas, você fala que não sabe responder.",
    tools=[{'type': 'file_search'}],
    tool_resources={'file_search': {'vector_store_ids': [vector_store.id]}},
    model='gpt-4o'
)


# ## Cria uma thread

# In[6]:


thread = client.beta.threads.create()


# ## Adiciona mensagem a thread criada

# In[37]:


mensagem_texto = 'Segundo o documento fornecido, o que é o Hugging Face?'
mensagem_texto = 'Segundo o documento fornecido, Como utilizar assistants com python?'


message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content=mensagem_texto
)


# ## Roda a thread no assistant

# In[38]:


run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assitant.id,
    instructions='O nome do usuário é Adriano Soares e ele é um usuário Premium.'
)


# ## Aguarda a thread rodar

# In[39]:


import time

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
print(run.status)


# ## Verifica a resposta

# In[40]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(mensagens)
else:
    print('Errro', run.status)


# In[41]:


print(mensagens.data[0].content[0].text.value)


# ## Analisando os passos do modelo

# In[42]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[43]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            if tool_call.type == 'file_search':
                print(tool_call)
            else:
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
    


# In[44]:


mensagens = client.beta.threads.messages.list(
    thread_id=thread.id
)
mensagem = list(mensagens)[0].content[0].text
anotacoes = mensagem.annotations
citacoes = []
for index, anotacao in enumerate(anotacoes):
    mensagem.value = mensagem.value.replace(anotacao.text, f'[{index}]')
    if file_cit := getattr(anotacao, 'file_citation', None):
        file = client.files.retrieve(file_cit.file_id)
        citacoes.append(f'[{index}] {file.filename}')
citacoes = "\n".join(citacoes)
mensagem.value = f'{mensagem.value}\n\n{citacoes}' 


# In[45]:


print(mensagem.value)


# In[ ]:




