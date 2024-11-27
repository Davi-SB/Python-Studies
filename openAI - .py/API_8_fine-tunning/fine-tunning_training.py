#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = openai.Client()


# In[4]:


def generate_response(chat, model='gpt-4o-mini', temperature=0, max_tokens=1000, stream = False):
    return client.chat.completions.create(
        messages = chat,
        model = model,
        temperature = temperature,
        max_tokens= max_tokens,
        stream = stream
    )

def export_chat(chat):
    with open('chat.md', 'w', encoding='utf-8') as file:
        for message in chat:
            file.write(f"{message['role']}: {message['content']}\n\n")


# https://platform.openai.com/finetune para verificar os fine tunes

# In[3]:


file = client.files.create(
    # rb --> read binary
    file = open("answeredQuestions.jsonl", "rb"),
    purpose = "fine-tune"
)

# NAO RODAR DE NOVO
# client.fine_tuning.jobs.create(
#     training_file = file.id,
#     model = "gpt-4o-mini-2024-07-18"
# )


# input: Que barulho foi esse? Você ouviu? Melhor ficar atento

# In[7]:


chat_default = []
model_default = "gpt-4o-mini-2024-07-18"

chat_fine_tuned = []
model_fine_tuned = "ft:gpt-4o-mini-2024-07-18:personal::ALzPu9it"

line = ''
while True:
    line = input('\nYou: ')
    if line.upper() == 'STOP': break
    if not line: continue
    
    # adiciona pergunta aos chats
    chat_default.append({'role': 'user', 'content': line})
    chat_fine_tuned.append({'role': 'user', 'content': line})
    
    # gera resposta
    response_default     = generate_response(chat_default,    model = model_default,    temperature = 0.0)
    ressponse_fine_tuned = generate_response(chat_fine_tuned, model = model_fine_tuned, temperature = 1.3)
    
    # printa resposta
    message_default    = response_default.choices[0].message
    message_fine_tuned = ressponse_fine_tuned.choices[0].message
    
    print(f"\nDefault: {message_default.content}")
    print(f"Fine-tuned: {message_fine_tuned.content}", end='\n\n')
    
    # adiciona resposta ao chat 
    chat_default.append(message_default.model_dump(exclude_none = True))
    chat_fine_tuned.append(message_fine_tuned.model_dump(exclude_none = True))

