# 6. Listas, tuplas, dicionarios e conjuntos
# Listas
lista = [1, 2, 3, 4]

primeiro = lista[0]
ultimo = lista[-1]
antipenultimo = lista[-3]
if lista: print("lista nao esta vazia")

lista.append(5) # push_back
lista.extend([6, 7, 9])
lista.insert(0, -10) # insere o -10 na posicao sem sobrescrever o 1
if 9 in lista: lista.remove(9)
pop = lista.pop() # remove e retorna o de indice especificado ou ultimo se não especificar
pos = lista.index(-10) # retorna o indice da primeira ocorrencia do elemento especificado
qtde = lista.count(2) # conta quantas vezes um elemento aparece na lista 
lista.sort() # ordena
lista.reverse() # inverte a lista
# lista.clear()

sublista = lista[1:3] # nao inclui o 3, pega os elementos de indice 1 e 2
    # Mais exemplos de slicing:
    # numeros[:3] – Do início até o índice 2 (primeiros 3 elementos): [10, 20, 30]
    # numeros[3:] – Do índice 3 até o final: [40, 50, 60]
    # numeros[-3:] – Os últimos 3 elementos da lista: [40, 50, 60]
    # numeros[::2] – Pula um elemento, pegando apenas os índices pares: [10, 30, 50]
    # numeros[0:3:2] – Pula um elemento, pegando apenas os índices pares entre os indices 0 e 2
    # numeros[::-1] - itera de tras pra frente
 
listaComposta = [1, 3.4, "string", True, [123, 567], {1, 6}]    

lista2 = range(10) # [0, 1, ... , 9]
lista3 = range(2, 10, 2) # [2, 4, ... , 8]


# Tuplas
tupla = (1, 2, 3) # valores podem ser acessados mas nao modificados
um, dois, tres = tupla # isso funciona para quase tudo, util para "desmembrar" uma "struct"
lista4 = list(tuple(lista)) # conversoes


# Dicionários
dicionario = {"chave": 10, "outra_chave": 20}  # Dicionário (map ou hash map)
dicionario["nova_chave"] = 30  # Adiciona novo par chave-valor no dicionário
print(dicionario.keys()) # retorna todas as chaves
print(dicionario.values()) # retorna todos os valores
print(dicionario.items()) # retorna todos os pares chave-valor
print(dicionario.get("chave"))  # Output: 10
print(dicionario.get("x", "não encontrado"))  # Output: não encontrado
print(dicionario.pop("outra_chave")) # retorna 20 e remove
# dicionario.popitem() # da pop no par
#dict.setdefault(key, default=None): Retorna o valor da chave se ela existir; caso contrário, insere a ##chave com o valor padrão e a retorna
# dicionario.update(outro_dic) # faz update, mescla
# dicionario.clear()


# Sets
conjunto = {1, 2, 3, 4}    # Conjunto (similar a sets em C++)
conjunto2 = {4, 5, 6}
conjunto.add(5)  # Adiciona elemento ao conjunto
conjunto.remove(2) # remove o 2
conjunto.discard(2) # remove e nao gera erro se nao existir
print(conjunto.pop()) # remove e retorna um elemento aleatorio
conjuntoUnido = conjunto.union(conjunto2) # retorna a uniao*
ConjuntoIntersec = conjunto.intersection(conjunto2) # retorna a intersecao*
diff = conjunto.difference(conjunto2) # conjunto - conjunto2*
simDiff = conjunto.symmetric_difference(conjunto2) # retorna elementos que estao em um OU outro, mas nao #em ambos*
# conjunto.clear()
# *OBS: os metodos com * possuem sua versao com "update" no final. assim setam o proprio conjunto em vez #de retornar
# ex: (set = set.diff(set2)) igual a (set.diff_update(set2))

print(f"Lista: {lista}\nSublista: {sublista}\nDicionário: {dicionario}\nConjunto: {conjunto}")