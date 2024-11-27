#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# ### Cria o [assistant](https://platform.openai.com/docs/assistants/overview/agents)
# - .beta vai ser provavelmente removido após sair do beta
# - Opções para [tools](https://platform.openai.com/docs/assistants/tools/assistant-tools): Code Interpreter, File Search e Function calling

# In[2]:


mathAssistant = client.beta.assistants.create(
    name = "Tutor de Matemática",
    instructions = 'Você é um tutor pessoal de matemática de um aluno da faculdade. Escreva e execute códigos para responder as perguntas de matemática, cálculo e física que receber.',
    tools = [{'type': 'code_interpreter'}],
    model = 'gpt-4o-mini'
)


# ### Cria uma thread
# - Threads simplificam odesenvolvimento deaplicações de IA ao armazenar o histórico de mensagens e truncá-lo quando a conversa fica muito longa para o comprimento do contexto do modelo
# - Você cria uma thread uma vez e simplesmente adiciona mensagens a ela conforme o usuário responde

# In[3]:


myThread = client.beta.threads.create()
print(myThread)


# ### Adiciona a mensagem em myThread
# - Até agora, a thread e o assistente não têm nenhuma relação, não estão associados

# In[4]:


message = client.beta.threads.messages.create( # cria uma mensagem
    thread_id = myThread.id, # na thread especificada
    role = 'user',
    # content = 'Se eu jogar um dado honesto 1000 vezes, qual é a probabilidade de eu obter exatamente 150 vezes o número 6? Resolva com um código'
    content = 'De quantas maneiras é possível embaralhar 12 cartas de baralho? Resolva com um código'
)
print(message)


# ### Roda a thread no assistant
# - Aqui sim a thread e o assistente se relacionam: o assistant processa a thread e gera uma resposta

# In[5]:


run = client.beta.threads.runs.create(
    thread_id = myThread.id,
    assistant_id = mathAssistant.id,
    instructions = 'O nome do usuário é Davi Brilhante e ele está no terceiro período da faculdade de Engenharia da Computação.'
)
print(run)


# ### Aguarda a run terminar
# - [estados que uma run pode assumir](https://platform.openai.com/docs/assistants/deep-dive/run-lifecycle)

# In[6]:


while run.status in ['queued', 'in_progress', 'cancelling']:
    run = client.beta.threads.runs.retrieve( # recupera os dados da run 
        thread_id = myThread.id, # na thread especificada
        run_id = run.id # especifica qual run recuperar os dados
    )
    print(run.status)


# ### Verifica a resposta

# In[7]:


if run.status == 'completed':
    mensagens = client.beta.threads.messages.list(
        thread_id = myThread.id
    )
    print(mensagens)
else:
    print('Erro:', run.status)


# ### Acesso de mensagens
# - As mensagens novas são adicionadas como um push_front()
#     - Menor índice --> mais recente
#     - Exibir de trás pra frente --> ordem cronológica

# In[8]:


print(mensagens.data[0].content[0].text.value, end='\n\n')

for i in range(len(mensagens.data)-1, -1, -1):
    role    = mensagens.data[i].role
    content = mensagens.data[i].content[0].text.value
    print(f'[{i}] {role}: {content}')
    
print()

for mensagem in mensagens.data[::-1]:
    role    = mensagem.role
    content = mensagem.content[0].text.value
    print(f'    {role}: {content}')


# ### Analisando os passos do modelo

# In[9]:


run_steps = client.beta.threads.runs.steps.list(
  thread_id = myThread.id,
  run_id = run.id
)


# - Printar a lista de trás pra frente pelo mesmo motivo que as mensagens

# In[10]:


for step in run_steps.data[::-1]:
    print('=== Step:', step.step_details.type)
    


# In[11]:


print(run_steps.data[1].step_details, end='\n\n')

for tool_call in run_steps.data[1].step_details.tool_calls:
    print(tool_call)


# In[13]:


for step in run_steps.data[::-1]:
    print('=== Step:', step.step_details.type)
    
    if step.step_details.type == 'tool_calls':
            for tool_call in step.step_details.tool_calls:
                print('-----')
                print(tool_call.code_interpreter.input)
                print('-----')
                print('Result')
                # não consegui fazer funcionar, algo mudou
                # print(tool_call.code_interpreter.outputs[0].logs)
                
    if step.step_details.type == 'message_creation':
        message = client.beta.threads.messages.retrieve(
            thread_id  = myThread.id,
            message_id = step.step_details.message_creation.message_id
        )
        print(message.content[0].text.value)

