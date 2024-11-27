#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())
client = openai.Client()


# Criação de função que o modelo vai poder usar para extrair informações. Na prática essa função poderia vir de outra API ou de um banco de dados.
# 
# - JSON (JavaScript Object Notation) --> formato de texto leve (string) usado para representar dados estruturados (nesse caso, dicionários)
# 
# - `json.dumps()` recebe um objeto Python (nesse caso, dicionário) e retorna ele como uma string. Assim, a função retorna a informação num formato padronizado e estruturado e facilita o entendimento de outros sistemas que esperam dados em JSON

# In[2]:


def obter_temperatura_atual(local, unidade="celsius"):
    if "são paulo" in local.lower():
        return json.dumps({"local": "São Paulo", "temperatura": "32", "unidade": unidade})
    elif "porto alegre" in local.lower():
        return json.dumps({"local": "Porto Alegre", "temperatura": "25", "unidade": unidade})
    elif "rio de janeiro" in local.lower():
        return json.dumps({"local": "Rio de Janeiro", "temperatura": "35", "unidade": unidade})
    else:
        return json.dumps({"local": local, "temperatura": "unknown", unidade: unidade})


# Para informar ao modelo que ferramentas podem ser usadas, a lista de dicionários `tools` é passada para ele como um parametro de `client.chat.completions.create()` e tem o papel de especificar as ferramentas disponíveis.
# 
# - Cada função deve ser um elemento dessa lista, um dicionário. Cada dicionário da `lista tools` se refere a uma função e inclui:
#     - `type`: tipo da ferramenta. Nesse caso, function
#     - `function`: descreve tudo da função em questão. Também é um dicionário e contém:
#         - `name`: nome da função
#         - `description`: explicação da utilidade da função para que o modelo saiba para que usá-la
#         - `parameters`: descrição e informações sobre os argumentos da função. Também é um dicionário e inclui:
#             - `type`: tipo dos parâmetros. Frequentemente, objetos
#             - `required`: lista dos argumentos (strings) que precisam ser fornecidos, os que não possuem valor padrão na função
#             - `properties`: é outro dicionário em que cada chave se refere ao nome de um argumento. Cada chave está associada à outro dicionário que contém informações sobre o parâmetro em questão:
#                 - `type`: tipo do dado do argumento (int, string, etc)
#                 - `description`: descrição do significado daquele dado
#                 - `enum`: se for o caso, enum se associa com uma lista de valores predefinidos, em caso de opções bem definidas de entradas 

# In[83]:


tools = [{
    "type": "function",
    "function": {
        "name": "obter_temperatura_atual",
        "description": "Obtém a temperatura atual em uma dada cidade",
        "parameters": {
            "type": "object",
            "required": ["local"],
            "properties": {
                "local": {
                    "type": "string",
                    "description": "O nome da cidade. Ex: São Paulo"
                },
                "unidade": {
                    "type": "string", 
                    "enum": ["celsius", "fahrenheit"]
                }
            }
        }
    }
}]


# - Ao chamar chat.completions.create a lista `tools` é passada como parâmetro para que o modelo possa acessá-las.
# - `tool_choice` define a escolha das ferramentas pelo modelo
#     - `auto`: deixa que a escolha seja feita automaticamente. é o valor padrão
#     - Para forçar o modelo a usar uma determinada função, tool_choice pode receber o nome da função.

# In[84]:


mensagens = [
    {"role": "user", 
     "content": "Qual é a temperatura em São Paulo, Porto Alegre e Recife?"}
    ]

resposta = client.chat.completions.create(
    model       = "gpt-4o-mini",
    messages    = mensagens,
    tools       = tools,
    tool_choice = "auto",
)


# - Verificando a resposta dada pelo modelo apenas com o código até aqui, percebe-se que o conteúdo está vazio (`content=None`), ou seja, o modelo não forneceu uma resposta em formato de texto
# - Por outro lado, o parâmetro `tool_calls` em `resposta.choices[0].message` agora possui um valor, o que mostra que o modelo está chamando funções externas para fornecer a resposta
#     - `tool_calls` mostra as chamadas de função que o modelo realizou para poder prosseguir com a resposta 

# In[85]:


print(resposta.choices[0].message)
print('_'*30)


# Assim, as funções requisitadas devem ser chamadas e suas respostas atribuidas às mensagens com o role `tools` para que uma nova resposta seja gerada mas agora com essas informações já dispiníveis
# 
# - Ao final, a segunda resposta é gerada com 5 mensagens em `menssagens`: A pergunta do usuário, a primeira resposta que o modelo gerou requisitando as ferramentas e a resposta dos três usos de ferramenta

# In[86]:


funcoes_disponiveis = { "obter_temperatura_atual": obter_temperatura_atual }

mensagem_resp = resposta.choices[0].message
tool_calls = resposta.choices[0].message.tool_calls

# se houve chamada de ferramentas
if tool_calls:
    mensagens.append(mensagem_resp)
    
    # para cada tool call
    for tool_call in tool_calls:
        # obtemos o nome e argumentos da função a ser chamada
        # os argumentos são um json, .loads carrega como um dicionário
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        # a variável function_to_call recebe a função a ser chamada,
        # nome da função é a chave para o dicionário funcoes_disponiveis
        function_to_call = funcoes_disponiveis[function_name]
        
        # chamamos a função com os argumentos
        # .get para obter o valor do argumento, caso não exista, retorna None
        function_response = function_to_call(
            local   = function_args["local"],
            unidade = function_args["unidade"],
        )

        # adicionamos a resposta da função no array de mensagens
        # que será fornecido ao modelo para gerar a resposta final
        mensagens.append(
            {
                # novo role: tool
                "role": "tool",
                
                # deve ser adicionado para saber de qual chamada se trata,
                # qual função foi chaamda e qual foi a resposta
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": function_response,
            }
        )
    
    for mensagem in mensagens:
        print(mensagem, end='\n\n')
        
    # uma vez que todas as chamadas foram processadas, basta gerar a resposta final
    segunda_resposta = client.chat.completions.create(
        # só são necessários esses dois parâmetros
        model    = "gpt-4o-mini",
        messages = mensagens,
    )


# In[87]:


print(segunda_resposta.choices[0].message.content)

