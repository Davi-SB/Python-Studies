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