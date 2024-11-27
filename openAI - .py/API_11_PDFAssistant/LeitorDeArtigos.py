#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# ### Armazenamento e upload de arquivos
# - Inicializar uma vector_store, estrutura de armazenamento de dados onde eles ficarão salvos
# - Abrir os arquivos numa lista de streams
# - Adicionar os dados (arquivos) à ``vector_store`` com `upload_and_pool`, passando como argumentos o ID do vector store que deve ser adicionado e lista de stream dos arquivos

# In[3]:


vector_store = client.beta.vector_stores.create(name = 'Informacoes Kaelen Voss')

files = ['Scalable_Optimal_Countermeasure_Selectio.pdf'] # Uma lista pois é possível adicionar mais de um arquivo ao mesmo tempo
files_stream = [open(file, 'rb') for file in files]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id = vector_store.id,
    files           = files_stream,
)


# In[4]:


print(file_batch, end='\n\n')
print(file_batch.status)
print(file_batch.file_counts)


# ### Cria o assistant
# - `tools` indica o uso de `file_search`
# - `tool_resources` envia o id da vector store

# In[5]:


texto_instrucoes = """Você deve responder as perguntas com base nas informações do artigo Scalable_Optimal_Countermeasure_Selectio.pdf.
    Ainda, mostre em qual sessão do PDF você encontrou cada informação. Caso a informação não estiver presente
    no PDF, diga que não sabe responder."""

assitant = client.beta.assistants.create(
    name           = "Analisador de Fault Tree",
    instructions   = texto_instrucoes,
    tools          = [{'type': 'file_search'}],
    tool_resources = {'file_search': {'vector_store_ids': [vector_store.id]}},
    model          = 'gpt-4o-mini'
)


# ### Cria a thread e adiciona mensagem nela

# In[6]:


thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role      = 'user',
    content   = 'Preciso que você me explique toda a lógica e sentido da árvore de falha "Figure3. An ACT for SCADA system. Me explique todo o contexto do artigo necessário para entender a Figura 3". Preciso entender o que é um ACT e como ele é utilizado em um SCADA system. Além, disso, cada evento, por que ele está ali e como ele se relaciona com os outros eventos.'
)


# ### Assistant roda a thread e espera a run terminar

# In[7]:


import time

run = client.beta.threads.runs.create(
    thread_id    = thread.id,
    assistant_id = assitant.id,
    instructions = 'O nome do usuário é Davi e não sabe nada sobre o artigo.'
)

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(0.5)
    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id    = run.id
    )


# ### Verifica a resposta
# 
# <details>
# <summary>Resposta esperada</summary>
# 
# A Biblioteca de Ildra é essencial para Kaelen Voss, pois representa tanto seu refúgio de conhecimento quanto o centro de sua missão de vida: preservar o saber antigo para as futuras gerações. Lá, ele estudou sob a mentoria de Talia Rhen, realizou suas pesquisas mais importantes, e vê a biblioteca como um símbolo de proteção do saber. Ela é seu lar intelectual e o pilar de sua dedicação à preservação da história de Eriador.
# 
# </details>
# 

# In[8]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(mensagens)
else:
    print('Errro', run.status)


# In[10]:


print(mensagens.data[0].content[0].text.value)


# ### Substitui as marcas de sources por índices e suas referências

# In[11]:


mensagens.data[0].content[0].text


# In[12]:


# Função para substituir as anotações por números e adicionar as citações dos arquivos
# Recebe uma mensagem e retorna o value da mensagem com as anotações substituídas
def replace_annotations(mensagem):
    anotacoes = mensagem.annotations
    citacoes = []
    
    for index, anotacao in enumerate(anotacoes):
        # Substitui o texto da anotação pelo índice
        mensagem.value = mensagem.value.replace(anotacao.text, f'[{index}]')
        
        # Adiciona a citação do arquivo na lista de citações
        # := --> (== && =)
        # get attribute, se não existir, retorna None
        if file_cit := getattr(anotacao, 'file_citation', None):
            # Recupera o arquivo do ID
            file = client.files.retrieve(file_cit.file_id)
            # Adiciona o nome do arquivo na lista de citações
            citacoes.append(f'[{index}] {file.filename}')
    
    # Junta as citações em uma única string separando por quebra de linha
    citacoes = "\n".join(citacoes)
    
    mensagem.value = f'{mensagem.value}\n\n{citacoes}'
    return mensagem.value

# Uso da função
# .text tem não só os valores mas também as anotações
mensagemSubstituida = replace_annotations(mensagens.data[0].content[0].text)
print(mensagemSubstituida)


# ### Analisando os passos do modelo

# In[13]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


# In[14]:


for step in run_steps.data[::-1]:
    print('=== Step:', step.step_details.type)
    


# In[15]:


for step in run_steps.data[::-1]:
    print('\n=== Step:', step.step_details.type)
    
    if step.step_details.type == 'tool_calls':
        for tool_call in step.step_details.tool_calls:
            if tool_call.type == 'file_search':
                print(tool_call)
            else: # code_interpreter
                print('-----')
                print(tool_call.code_interpreter.input)
                print('-----')
    
    if step.step_details.type == 'message_creation':
        message = client.beta.threads.messages.retrieve(
            thread_id=thread.id,
            message_id=step.step_details.message_creation.message_id
        )
        print(replace_annotations(message.content[0].text))
    

