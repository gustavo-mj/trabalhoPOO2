from Pessoa import Pessoa
from Animal import Animal
from datetime import date

class RegistroD:
    # Atributos: data, animal, doador, motivo
    def __init__(self, data: date, animal: Animal, doador: Pessoa, motivo: str):
        self.__data = None
        self.__animal = None
        self.__doador = None
        self.__motivo = None
        
        if isinstance(data, date):
            self.__data = data
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(doador, Pessoa):
            self.__doador = doador
        if isinstance(motivo, str):
            self.__motivo = motivo

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

    # Getter e Setter para doador
    @property
    def doador(self) -> Pessoa:
        return self.__doador

    @doador.setter
    def doador(self, doador: Pessoa):
        if isinstance(doador, Pessoa):
            self.__doador = doador

    # Getter e Setter para motivo
    @property
    def motivo(self) -> str:
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo