print("ao", end="\n\n") # o print tem o end="\n" por padrão

print(3 // 2) # divisao inteira
print(int(3 / 2), end="\n\n")

print(5 + int('5')) # == 10 (int)
print(len('davi'))  # length
help(len)
print() # so uma quebra de linha


# 1. Entrada e saída 
nome = input("Digite seu nome:\n")  # Recebe entrada
print(type(nome)) # input vai ser >>>str<<< por padrao

idade = int(input('Digite sua idade:\n'))
print(type(idade))

print(f"Olá, {nome} de {idade} anos!")  # f-string para formatação 

a = 5
b = 10 # nesse caso, a e b sao int por padrao
print(f"A soma de {a} + {b} é {a + b}.")
print("A soma de {} + {} é {}.".format(a, b, a + b))
print("A soma de " + str(a) + " + " + str(b) + " é " + str(a + b) + ".", end="\n\n")
print(f"escolhendo a quantidade de casas decimais: {float(a/b):.7f}")
print(f"escolhendo formatacao de quantidade de algarismos: {(a):03d}", end="\n\n")

texto = """esse eh um texto que 
ocupa varias linhas 
e preserva as quebras de texto"""
print(texto)
print('-*' * 15) # kkkkkcomo


# 2. Variaveis e tipos de dados
inteiro = 4      # Inteiro
flutuante = 3.14  # Ponto flutuante (float)
booleano = True   # Booleano (True ou False)
texto = "Python"  # String
# Python eh dinamicamente tipado
# Exemplo de exibicao de tipos
print(f"Tipos: {type(inteiro)}, {type(flutuante)}, {type(booleano)}, {type(texto)}")

# 3. Condicionais
if inteiro > 5:
    print("O número é maior que 5")
elif inteiro == 5:
    print("O número é 5")
else: print("O número é menor que 5") # um statement pode ficar na mesma linha

if (0 < 1 and not(1 < 0)) or 1 == 2: # and tem precedência maior que o or
    print("if and e or")