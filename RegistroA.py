from Pessoa import Pessoa
from Animal import Animal
from datetime import date

class RegistroA:
    # Atributos: data, animal, adotante, termo
    def __init__(self, data: date, animal: Animal, adotante: Pessoa, termo: bool):
        self.__data = None
        self.__animal = None
        self.__adotante = None
        self.__termo = None
        
        if isinstance(data, date):
            self.__data = data
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(adotante, Pessoa):
            self.__adotante = adotante
        if isinstance(termo, bool):
            self.__termo = termo

    # Getter e Setter para data
    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    # Getter e Setter para animal
    @property
    def animal(self) -> Animal:
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    # Getter e Setter para adotante
    @property
    def adotante(self) -> Pessoa:
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante: Pessoa):
        if isinstance(adotante, Pessoa):
            self.__adotante = adotante

    # Getter e Setter para termo
    @property
    def termo(self) -> bool:
        return self.__termo

    @termo.setter
    def termo(self, termo: bool):
        if isinstance(termo, bool):
            self.__termo = termo
