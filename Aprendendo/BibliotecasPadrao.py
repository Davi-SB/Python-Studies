# Principais imports da biblioteca pdrao de Python

# 1. math
import math

raiz = math.sqrt(16)
print(raiz)  # Saída: 4.0

print(math.pi)  # Saída: 3.141592653589793

fatorial = math.factorial(5)
print(fatorial)  # Saída: 120

potencia = math.pow(2, 3)
print(potencia)  # Saída: 8.0

gcd = math.gcd(8, 12)
print(gcd)  # Saída: 4

# 2. A biblioteca datetime lida com datas e horas.
import datetime

agora = datetime.datetime.now()
print(agora)  # Saída: data e hora atuais

data_futura = datetime.datetime(2025, 1, 1)
print(data_futura)  # Saída: 2025-01-01 00:00:00

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)  # Saída: data e hora formatadas

data_passada = datetime.datetime(2020, 1, 1)
diferenca = agora - data_passada
print(diferenca.days)  # Saída: número de dias entre as datas

# 3. números aleatórios
import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

opcoes = ['A', 'B', 'C']
selecao = random.choice(opcoes)
print(selecao)

random.shuffle(opcoes)
print(opcoes)  # Saída: lista embaralhada

amostra = random.sample(opcoes, 2)
print(amostra)  # Saída: lista com 2 elementos selecionados aleatoriamente

# 4. interagir com o sistema operacional.
import os

# Listando arquivos e pastas no diretório atual
itens = os.listdir()
print(itens)

os.mkdir('novo_diretorio')

# Mudando o diretório atual
os.chdir('novo_diretorio')
print(os.getcwd())  # getCurrentWorkingDir, Saída: caminho do novo diretório

# Voltando para o diretório anterior
os.chdir('..')

os.rmdir('novo_diretorio')

# 5. permite trabalhar com dados JSON.
import json

# Convertendo um dicionário em uma string JSON
dados = {'nome': 'Alice', 'idade': 25}
json_string = json.dumps(dados)
print(json_string)  # Saída: {"nome": "Alice", "idade": 25}

# Convertendo uma string JSON de volta para um dicionário
dados_carregados = json.loads(json_string)
print(dados_carregados)  # Saída: {'nome': 'Alice', 'idade': 25}

# Trabalhando com arquivos JSON
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)

with open('dados.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)  # Saída: {'nome': 'Alice', 'idade': 25}
    
# 6. tempo
import time

# Pausa a execução do programa por 2 segundos
time.sleep(2) 

# Retorna o tempo atual em segundos desde a "época".
inicio = time.time()
# ... (código aqui)
duracao = time.time() - inicio

# Retorna a hora atual como uma estrutura de tempo local
hora_atual = time.localtime() 

# Formata a data e hora de acordo com o formato especificado.
data_formatada = time.strftime("%d/%m/%Y %H:%M:%S", hora_atual)

# Retorna o valor do contador de alta resolução em segundos.
inicio = time.perf_counter()
# ... (código aqui)
intervalo = time.perf_counter() - inicio

    