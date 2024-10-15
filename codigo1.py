#print("ao", end="\n\n") # o print tem o end="\n" por padrão
#
#print(3 // 2) # divisao inteira
#print(int(3 / 2), end="\n\n")
#
#print(5 + int('5')) # == 10 (int)
#print(len('davi'))  # length
#help(len)
#print() # so uma quebra de linha
#
#
############### 1. Entrada e saída ##############
## print("Digite seu nome:") 
#nome = input("Digite seu nome:\n")  # Recebe entrada
#print(type(nome)) # input vai ser >>>str<<< por padrao
#
#idade = int(input('Digite sua idade:\n'))
#print(type(idade))
#
#print(f"Olá, {nome} de {idade} anos!")  # f-string para formatação 
#
#a = 5
#b = 10 # nesse caso, a e b sao int por padrao
#print(f"A soma de {a} + {b} é {a + b}.")
#print("A soma de {} + {} é {}.".format(a, b, a + b))
#print("A soma de " + str(a) + " + " + str(b) + " é " + str(a + b) + ".", end="\n\n")
#print(f"escolhendo a quantidade de casas decimais: {float(a/b):.7f}")
#print(f"escolhendo formatacao de quantidade de algarismos: {(a):03d}", end="\n\n")
#
#texto = """esse eh um texto que 
#ocupa varias linhas 
#e preserva as quebras de texto"""
#print(texto)
#print('-*' * 15) # kkkkkcomo
#
#
############### 2. Variaveis e tipos de dados ##############
## Python eh dinamicamente tipado
#inteiro = 4      # Inteiro
#flutuante = 3.14  # Ponto flutuante (float)
#booleano = True   # Booleano (True ou False)
#texto = "Python"  # String
#
## Exemplo de exibicao de tipos
#print(f"Tipos: {type(inteiro)}, {type(flutuante)}, {type(booleano)}, {type(texto)}")
#
############### 3. Condicionais ##############
#if inteiro > 5:
#    print("O número é maior que 5")
#elif inteiro == 5:
#    print("O número é 5")
#else: print("O número é menor que 5") # um statement pode ficar na mesma linha
#
#if (0 < 1 and not(1 < 0)) or 1 == 2: # and tem precedência maior que o or
#    print("if and e or")
#
############### 4. Loops (for e while) ##############
## foreach numa lista
#numeros = [1, 2, 3, 4, 5]
#for num in numeros:
#    print(f"Número: {num}")
#
#pessoas = [('nome', 'idade', 'cpf'),
#           ('davi', 19, "1232354")
#          ]
#
#for nome, idade, cpf in pessoas:
#    # usar essas variaveis aqui
#
#
## While loop
#while contador in range(5):
#    print(f"Contador: {contador}")
#
## obs: break e contiue existem igual
#
############### 5. Funções ##############
#def soma(a=0, b=0): # valores padrao em caso de nao serem fornecidos
#    return a + b
#
#print(f"Resultado da soma: {soma(5, 3)}")
#print(f"Resultado da soma: {soma(b=3, a=5)}")
#
#def somar_tudo(*numeros): # pode receber varios numeros
#    return sum(numeros)
#
#def operacoes(a, b): # retorna como tupla 
#    soma = a+b
#    sub = a-b
#    return soma, sub
#
## Se você passar uma lista ou um dicionário, pode modificar seu conteúdo diretamente. Para tipos imutáveis 
## (como inteiros, strings e tuplas), você não pode alterar o valor em si, mas pode retornar o novo valor.
#
#var = 1
#def modificar(): # modificar uma variavel global dentro de uma funcao
#    global var
#    var = 10
#    
#def multiplicar(a, b):
#    return a * b
#
#operacao = multiplicar # uso como ponteiro de funcao
#print(operacao(3, 4))  # Saída: 12
#
#def executar_operacao(funcao, a, b): # passar funcao como argumento
#    return funcao(a, b)
#
#print(executar_operacao(multiplicar, 3, 4))  # Saída: 12
#
#soma = lambda a, b: a + b # lambda argumentos: expressão (definir função sem uso de def)
#print(soma(5, 3))  # Saída: 8
#
## Usando lambda com sorted()
#lista = [(1, 'zzz'), (2, 'bbb'), (3, 'aaa')]
#lista_ordenada = sorted(lista, key=lambda item: item[1])
#print(lista_ordenada)  # Saída: [(3, 'aaa'), (2, 'bbb'), (1, 'zzz')]
#
##Em Python, você pode criar funções que recebem diversos tipos de estruturas de dados (listas, 
## dicionários, sets, etc.) sem a necessidade de definir explicitamente o tipo de dado que será passado, já 
## que Python é dinamicamente tipado.
#def processar_estrutura(estrutura):
#    if isinstance(estrutura, list):
#        return f"Lista com {len(estrutura)} elementos"
#    elif isinstance(estrutura, dict):
#        return f"Dicionário com {len(estrutura.keys())} chaves"
#    elif isinstance(estrutura, set):
#        return f"Set com {len(estrutura)} elementos"
#    elif isinstance(estrutura, tuple):
#        return f"Tupla com {len(estrutura)} elementos"
#    else:
#        return "Tipo de dado não suportado"
#
#print(processar_estrutura([1, 2, 3]))  # Saída: Lista com 3 elementos
#print(processar_estrutura({"a": 1, "b": 2}))  # Saída: Dicionário com 2 chaves
#print(processar_estrutura({1, 2, 3}))  # Saída: Set com 3 elementos
#print(processar_estrutura((10, 20)))  # Saída: Tupla com 2 elementos
#
#
############### 6. Listas, tuplas, dicionarios e conjuntos ##############
#lista = [1, 2, 3, 4]
#
#primeiro = lista[0]
#ultimo = lista[-1]
#antipenultimo = lista[-3]
#if lista: print("lista nao esta vazia")
#
#lista.append(5) # push_back
#lista.extend([6, 7, 9])
#lista.insert(0, -10) # insere o -10 na posicao sem sobrescrever o 1
#if 9 in lista: lista.remove(9)
#pop = lista.pop() # remove e retorna o de indice especificado ou ultimo se não especificar
#pos = lista.index(-10) # retorna o indice da primeira ocorrencia do elemento especificado
#qtde = lista.count(2) # conta quantas vezes um elemento aparece na lista 
#lista.sort() # ordena
#lista.reverse() # inverte a lista
## lista.clear()
#
#sublista = lista[1:3] # nao inclui o 3, pega os elementos de indice 1 e 2
#    # Mais exemplos de slicing:
#    # numeros[:3] – Do início até o índice 2 (primeiros 3 elementos): [10, 20, 30]
#    # numeros[3:] – Do índice 3 até o final: [40, 50, 60]
#    # numeros[-3:] – Os últimos 3 elementos da lista: [40, 50, 60]
#    # numeros[::2] – Pula um elemento, pegando apenas os índices pares: [10, 30, 50]
#    # numeros[0:3:2] – Pula um elemento, pegando apenas os índices pares entre os indices 0 e 2
#    # numeros[::-1] - itera de tras pra frente
# 
#listaComposta = [1, 3.4, "string", True, [123, 567], {1, 6}]    
#
#
#lista2 = range(10) # [0, 1, ... , 9]
#lista3 = range(2, 10, 2) # [2, 4, ... , 8]
#
#tupla = (1, 2, 3) # valores podem ser acessados mas nao modificados
#um, dois, tres = tupla # isso funciona para quase tudo, util para "desmembrar" uma "struct"
#lista4 = list(tuple(lista)) # conversoes
#
#
#dicionario = {"chave": 10, "outra_chave": 20}  # Dicionário (map ou hash map)
#dicionario["nova_chave"] = 30  # Adiciona novo par chave-valor no dicionário
#print(dicionario.keys()) # retorna todas as chaves
#print(dicionario.values()) # retorna todos os valores
#print(dicionario.items()) # retorna todos os pares chave-valor
#print(dicionario.get("chave"))  # Output: 10
#print(dicionario.get("x", "não encontrado"))  # Output: não encontrado
#print(dicionario.pop("outra_chave")) # retorna 20 e remove
## dicionario.popitem() # da pop no par
##dict.setdefault(key, default=None): Retorna o valor da chave se ela existir; caso contrário, insere a ##chave com o valor padrão e a retorna
## dicionario.update(outro_dic) # faz update, mescla
## dicionario.clear()
#
#
#conjunto = {1, 2, 3, 4}    # Conjunto (similar a sets em C++)
#conjunto2 = {4, 5, 6}
#conjunto.add(5)  # Adiciona elemento ao conjunto
#conjunto.remove(2) # remove o 2
#conjunto.discard(2) # remove e nao gera erro se nao existir
#print(conjunto.pop()) # remove e retorna um elemento aleatorio
#conjuntoUnido = conjunto.union(conjunto2) # retorna a uniao*
#ConjuntoIntersec = conjunto.intersection(conjunto2) # retorna a intersecao*
#diff = conjunto.difference(conjunto2) # conjunto - conjunto2*
#simDiff = conjunto.symmetric_difference(conjunto2) # retorna elementos que estao em um OU outro, mas nao #em ambos*
## conjunto.clear()
## *OBS: os metodos com * possuem sua versao com "update" no final. assim setam o proprio conjunto em vez #de retornar
## ex: (set = set.diff(set2)) igual a (set.diff_update(set2))
#
#print(f"Lista: {lista}\nSublista: {sublista}\nDicionário: {dicionario}\nConjunto: {conjunto}")
#
#
############### 7. Manipulação de strings ##############
#frase = "Hello, Python!"
#print(frase.lower())  # Converte para minúsculas
#print(frase.upper())  # Converte para maiúsculas
#print(frase.replace("Python", "Mundo"))  # Substitui partes da string
#
#texto = " Python é uma linguagem "
#
## 1. Remover espaços em branco
#texto_sem_espacos = texto.strip()  # Remove espaços no início e no fim
#print(f"Sem espaços: '{texto_sem_espacos}'")
#
## 2. Dividir a string em uma lista
#palavras = texto_sem_espacos.split()  # Divide por espaços em branco
#print(f"Palavras: {palavras}")
#
## 3. Juntar uma lista em uma string
#texto_junto = " ".join(palavras)  # Junta palavras com um espaço
#print(f"Texto junto: '{texto_junto}'")
#
## 4. Encontrar a posição de uma substring
#posicao = texto.find("linguagem")  # Retorna a posição da primeira ocorrência
#print(f"Posição da palavra 'linguagem': {posicao}")
#
## 5. Contar ocorrências de uma substring
#ocorrencias = texto.count("a")  # Conta quantas vezes 'a' aparece
#print(f"Número de ocorrências de 'a': {ocorrencias}")
#
## 6. Verificar se a string começa ou termina com uma substring
#começa_com = texto.startswith(" Python")  # Verifica se começa com ' Python'
#termina_com = texto.endswith("aprender. ")  # Verifica se termina com 'aprender.'
#print(f"Começa com ' Python': {começa_com}, Termina com 'aprender. ': {termina_com}")
#
## 7. Substituir parte da string
#texto_substituido = texto.replace("linguagem", "simples")  # Substitui 'fácil' por 'simples'
#print(f"Texto após substituição: '{texto_substituido}'")
#
## 8. Converter a string para maiúsculas e minúsculas
#maiusculas = texto.upper()  # Converte para maiúsculas
#minusculas = texto.lower()  # Converte para minúsculas
#print(f"Maiúsculas: '{maiusculas}', Minúsculas: '{minusculas}'")
#
## 9. Capitalizar a string (primeira letra maiúscula)
#capitalizado = texto.capitalize()  # Primeira letra em maiúscula
#print(f"String capitalizada: '{capitalizado}'")
#
## 10. Trocar a posição de caracteres
#texto_trocado = texto.replace("poderosa", "forte")  # Troca 'poderosa' por 'forte'
#print(f"Texto trocado: '{texto_trocado}'")
#
## 11. Reverter a string
#texto_reverso = texto[::-1]  # Inverte a string usando slicing
#print(f"Texto reverso: '{texto_reverso}'")
#
## 12. Obter o comprimento da string
#comprimento = len(texto)  # Obtém o comprimento da string
#print(f"Comprimento da string: {comprimento}")
#
## 13. Obter a substring (slicing)
#substring = texto[10:20]  # Obtém uma parte da string (índices 10 a 19)
#print(f"Substring (índices 10 a 19): '{substring}'")
#
## 14. Verificar se a string é alfanumérica
#alfanumerica = texto.isalnum()  # Retorna True se a string é alfanumérica
#print(f"A string é alfanumérica? {alfanumerica}")
#
## 15. Verificar se a string é numérica
#numerica = "12345".isnumeric()  # Retorna True se a string contém apenas números
#print(f"A string '12345' é numérica? {numerica}")
#
#

# parei aqui

# 8. Trabalhando com arquivos
# 1. Abrindo um arquivo para escrita
try:
    # O parâmetro 'w' indica que o arquivo será criado ou sobrescrito
    with open("exemplo.txt", "w") as arquivo:
        arquivo.write("Linha 1: Olá, mundo!\n")  # Escreve uma linha no arquivo
        arquivo.write("Linha 2: Aprendendo Python.\n")  # Outra linha
        print("Arquivo criado e texto escrito com sucesso.")

except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo para escrita: {e}")

# 2. Abrindo um arquivo para leitura
try:
    # O parâmetro 'r' indica que o arquivo será aberto para leitura
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
        print("Conteúdo do arquivo:")
        print(conteudo)  # Exibe o conteúdo lido

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")  # Captura erro específico se o arquivo não existir
except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo para leitura: {e}")

# 3. Lendo um arquivo linha por linha
try:
    with open("exemplo.txt", "r") as arquivo:
        print("Lendo o arquivo linha por linha:")
        for linha in arquivo:  # Itera sobre cada linha do arquivo
            print(linha.strip())  # Exibe a linha sem quebras de linha

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")  # Captura erro específico
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo linha por linha: {e}")

# 4. Adicionando texto a um arquivo existente
try:
    # O parâmetro 'a' indica que o arquivo será aberto para adição
    with open("exemplo.txt", "a") as arquivo:
        arquivo.write("Linha 3: Adicionando mais uma linha.\n")  # Adiciona nova linha
        print("Texto adicionado ao arquivo com sucesso.")

except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo para adição: {e}")

# 5. Lendo linhas específicas de um arquivo
try:
    with open("exemplo.txt", "r") as arquivo:
        print("Lendo as duas primeiras linhas:")
        for i in range(2):  # Lê apenas as duas primeiras linhas
            linha = arquivo.readline()  # Lê uma linha de cada vez
            print(linha.strip())

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")  # Captura erro específico
except Exception as e:
    print(f"Ocorreu um erro ao ler linhas específicas: {e}")

# 6. Usando o seek() para mover o cursor
try:
    with open("exemplo.txt", "r") as arquivo:
        arquivo.seek(0)  # Move o cursor para o início do arquivo
        conteudo = arquivo.read(10)  # Lê os primeiros 10 caracteres
        print(f"Primeiros 10 caracteres: {conteudo}")

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")  # Captura erro específico
except Exception as e:
    print(f"Ocorreu um erro ao usar seek: {e}")

# 7. Manipulando arquivos binários
try:
    # Gravação em um arquivo binário
    with open("exemplo_binario.bin", "wb") as arquivo_binario:
        dados = bytearray([120, 3, 255, 0, 100])  # Cria um array de bytes
        arquivo_binario.write(dados)  # Grava os dados binários
        print("Dados binários escritos com sucesso.")

    # Leitura de um arquivo binário
    with open("exemplo_binario.bin", "rb") as arquivo_binario:
        dados_lidos = arquivo_binario.read()  # Lê todos os dados do arquivo binário
        print(f"Dados lidos do arquivo binário: {list(dados_lidos)}")

except Exception as e:
    print(f"Ocorreu um erro ao manipular arquivos binários: {e}")

# 8. Removendo um arquivo
import os

try:
    os.remove("exemplo.txt")  # Remove o arquivo
    print("Arquivo removido com sucesso.")
except FileNotFoundError:
    print("Erro: O arquivo que você tentou remover não foi encontrado.")  # Captura erro específico
except Exception as e:
    print(f"Ocorreu um erro ao tentar remover o arquivo: {e}")

# 9. Exceções
try:
    resultado = 10 / 0  # Divisão por zero
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# 10. Classes e objetos (Programação Orientada a Objetos)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} está fazendo um som!")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex")
meu_cachorro.falar()

