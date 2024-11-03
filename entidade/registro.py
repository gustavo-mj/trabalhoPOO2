from entidade.pessoa import *
from entidade.animal import *
from datetime import date


class Registro:

    def __init__(self, codigo: int, data: date, animal: Animal):
        self.__codigo = None
        self.__data = None
        self.__animal = None
        
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(data, date):
            self.__data = data
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def animal(self) -> Animal:
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal
