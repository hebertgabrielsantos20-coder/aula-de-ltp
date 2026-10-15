class Animal:
    def __init__(self, idade, cor, raça):
        self.i = idade
        self.c = cor
        self.r = raça
    def emitir_som(self):
        print("Animal faz som...")

class Cachorro(Animal):
    def __init__(self, idade, cor, raça):
        super().__init__(idade, cor, raça)

    def emitir_som(self):
        print("Cachorro faz au-au...")

class Gato(Animal):
    def __init__(self, idade, cor, raça):
        super().__init__(idade, cor, raça)

    def emitir_som(self):
        print("Gato faz miau...")

class Pintinho(Animal):
    def __init__(self, idade, cor, raça, tamanho):
        self.t = tamanho
        super().__init__(idade, cor, raça)

    def emitir_som(self):
        print("Pintinho faz piu-piu...")

    def info_pintinho(self):
        print(f"Idade: {self.i} anos | Cor: {self.c} | Raça: {self.r} | Tamanho: {self.t} centímetros")

animal1 = Animal(2, "preto", "europeu")
animal1.emitir_som()
print()
cachorro1 = Cachorro(4, "branco", "Husky siberiano")
cachorro1.emitir_som()
print()
gato1 = Gato(2, "marrom", "siamês")
gato1.emitir_som()
print()
pintinho1 = Pintinho(0.5, "rosa", "brasileiro", 0.8)
pintinho1.emitir_som()
pintinho1.info_pintinho()