#import minhaBiblioteca # importa tudo do modulo

#minhaBiblioteca.funcaoEspecial() # uso explicitando que vem do import
#print(minhaBiblioteca.varBiblioteca)

#import minhaBiblioteca as mB # import as cria um apelido

#mB.funcaoEspecial() 
#print(mB.varBiblioteca)

#from minhaBiblioteca import funcaoEspecial, varBiblioteca # importa apenas o escrito

#funcaoEspecial()
#print(varBiblioteca)

#from minhaBiblioteca import funcaoEspecial as fE, varBiblioteca as vB # importa apenas o escrito e apelida

#fE()
#print(vB)

#from minhaBiblioteca import * # importa tudo, mas não precisa explicitar de onde vem

#funcaoEspecial()
#print(varBiblioteca)

# Importação de Pacotes:
# Pacotes são coleções de módulos organizados em diretórios. 
# Para um diretório ser um pacote, ele deve conter um arquivo __init__.py.
# O __init__.py permite inicializar o pacote e controlar quais módulos são acessíveis.
# Exemplo de estrutura de diretórios:
# meu_pacote/
#     __init__.py
#     modulo1.py
#     modulo2.py
# No __init__.py, você pode importar funções de outros módulos:
# from .modulo1 import funcao1
# from .modulo2 import funcao2
# Ao importar o pacote, as funções ficam disponíveis diretamente:
# import meu_pacote
# meu_pacote.funcao1()