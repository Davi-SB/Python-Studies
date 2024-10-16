# 7. Manipulação de strings
texto = " Python é uma linguagem "

# Remover espaços em branco
texto_sem_espacos = texto.strip()  # Remove espaços no início e no fim
print(f"Sem espaços: '{texto_sem_espacos}'")

# Dividir a string em uma lista
palavras = texto_sem_espacos.split()  # Divide por espaços em branco
print(f"Palavras: {palavras}")

# Juntar uma lista em uma string
texto_junto = "_".join(palavras)  # Junta palavras com um espaço
print(f"Texto junto: '{texto_junto}'")

# Encontrar a posição de uma substring
posicao = texto.find("linguagem")  # Retorna a posição da primeira ocorrência
print(f"Posição da palavra 'linguagem': {posicao}")

# Contar ocorrências de uma substring
ocorrencias = texto.count("a")  # Conta quantas vezes 'a' aparece
print(f"Número de ocorrências de 'a': {ocorrencias}")

# Verificar se a string começa ou termina com uma substring
começa_com = texto.startswith(" Python")  # Verifica se começa com ' Python'
termina_com = texto.endswith("aprend")  # Verifica se termina com 'aprender.'
print(f"Começa com ' Python': {começa_com}, Termina com 'aprend': {termina_com}")

# Substituir parte da string
texto_substituido = texto.replace("linguagem", "simples")  # Substitui 'fácil' por 'simples'
print(f"Texto após substituição: '{texto_substituido}'")

# Converter a string para maiúsculas e minúsculas
maiusculas = texto.upper()  # Converte para maiúsculas
minusculas = texto.lower()  # Converte para minúsculas
print(f"Maiúsculas: '{maiusculas}', Minúsculas: '{minusculas}'")

# Capitalizar a string (primeira letra maiúscula)
capitalizado = texto.capitalize()  # Primeira letra em maiúscula
print(f"String capitalizada: '{capitalizado}'")

# Trocar a posição de caracteres
texto_trocado = texto.replace("poderosa", "forte")  # Troca 'poderosa' por 'forte'
print(f"Texto trocado: '{texto_trocado}'")

# Reverter a string
texto_reverso = texto[::-1]  # Inverte a string usando slicing
print(f"Texto reverso: '{texto_reverso}'")

# Obter o comprimento da string
comprimento = len(texto)  # Obtém o comprimento da string
print(f"Comprimento da string: {comprimento}")

# Obter a substring (slicing)
substring = texto[10:20]  # Obtém uma parte da string (índices 10 a 19)
print(f"Substring (índices 10 a 19): '{substring}'")

# Verificar se a string é alfanumérica
alfanumerica = texto.isalnum()  # Retorna True se a string é alfanumérica
print(f"A string é alfanumérica? {alfanumerica}")

# Verificar se a string é numérica
numerica = "12345".isnumeric()  # Retorna True se a string contém apenas números
print(f"A string '12345' é numérica? {numerica}")

# ==, !=, <, > funcionam igualmente