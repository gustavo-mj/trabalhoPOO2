from Pessoa import Pessoa
from Animal import Animal
from RegistroA import RegistroA
from RegistroD import RegistroD

class Sistema:
    def __init__(self):
        self.__animais = []
        self.__pessoas = []
        self.__doacoes = []
        self.__adocoes = []
    
    @property
    def animais(self):
        return self.__animais
    
    @property
    def pessoas(self):
        return self.__pessoas

    @property
    def doacoes(self):
        return self.__doacoes

    @property
    def adocoes(self):
        return self.__adocoes

    def cadastrarPessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa) and pessoa in self.__pessoas:
            self.__pessoas.append(pessoa)

    def excluirPessoa(self, pessoa: Pessoa):
        if pessoa in self.__pessoas:
            self.__pessoas.remove(pessoa)
    
    def cadastrarAnimal(self, animal: Animal):
        if isinstance(animal, Animal) and autor not in self.__animais:
            self.__animais.append(animal)

    def excluirAnimal (self, animal: Animal):
        if animal in self.__animais:
            self.__animais.remove(animal)