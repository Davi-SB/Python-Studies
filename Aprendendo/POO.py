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