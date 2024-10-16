# 4. Loops (for e while)
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"Número: {num}")

pessoas = [('nome', 'idade', 'cpf'),
           ('davi', 19, "1232354")
          ]

for nome, idade, cpf in pessoas:
    # usar essas variaveis aqui
    print()

while contador in range(5):
    print(f"Contador: {contador}")

# obs: break e contiue existem igual


# 5. Funções
def soma(a=0, b=0): # valores padrao em caso de nao serem fornecidos
    return a + b

print(f"Resultado da soma: {soma(5, 3)}")
print(f"Resultado da soma: {soma(b=3, a=5)}")

def somar_tudo(*numeros): # pode receber varios numeros
    return sum(numeros)

def operacoes(a, b): # retorna como tupla 
    soma = a+b
    sub = a-b
    return soma, sub

# Se você passar uma lista ou um dicionário, pode modificar seu conteúdo diretamente. Para tipos imutáveis 
# (como inteiros, strings e tuplas), você não pode alterar o valor em si, mas pode retornar o novo valor.

var = 1
def modificar(): # modificar uma variavel global dentro de uma funcao
    global var
    var = 10
    
def multiplicar(a, b):
    return a * b

operacao = multiplicar # uso como ponteiro de funcao
print(operacao(3, 4))  # Saída: 12

def executar_operacao(funcao, a, b): # passar funcao como argumento
    return funcao(a, b)

print(executar_operacao(multiplicar, 3, 4))  # Saída: 12

soma = lambda a, b: a + b # lambda argumentos: retorno (definir função sem uso de def)
print(soma(5, 3))  # Saída: 8

# Usando lambda com sorted()
lista = [(1, 'zzz'), (2, 'bbb'), (3, 'aaa')]
lista_ordenada = sorted(lista, key=lambda item: item[1])
print(lista_ordenada)  # Saída: [(3, 'aaa'), (2, 'bbb'), (1, 'zzz')]

# Em Python, você pode criar funções que recebem diversos tipos de estruturas de dados (listas, 
# dicionários, sets, etc.) sem a necessidade de definir explicitamente o tipo de dado que será passado, já 
# que Python é dinamicamente tipado.
def processar_estrutura(estrutura):
    if isinstance(estrutura, list):
        return f"Lista com {len(estrutura)} elementos"
    elif isinstance(estrutura, dict):
        return f"Dicionário com {len(estrutura.keys())} chaves"
    elif isinstance(estrutura, set):
        return f"Set com {len(estrutura)} elementos"
    elif isinstance(estrutura, tuple):
        return f"Tupla com {len(estrutura)} elementos"
    else:
        return "Tipo de dado não suportado"

print(processar_estrutura([1, 2, 3]))  # Saída: Lista com 3 elementos
print(processar_estrutura({"a": 1, "b": 2}))  # Saída: Dicionário com 2 chaves
print(processar_estrutura({1, 2, 3}))  # Saída: Set com 3 elementos
print(processar_estrutura((10, 20)))  # Saída: Tupla com 2 elementos