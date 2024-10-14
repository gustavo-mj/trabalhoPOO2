from entidade.animal import *
from enum import Enum
from datetime import date


class Tipo(Enum):
    raiva = 1
    leptospirose = 2
    hepatite = 3


class Vacina():

    def __init__(self, codigo: int, animal: Animal, tipo: Tipo, data: date):
        self.__codigo = None
        self.__animal = None
        self.__tipo = None
        self.__data = None
        if isinstance(tipo, Tipo):
            self.__tipo = tipo
        if isinstance(data, date):
            self.__data = date
    
    @property
    def animal(self) -> Animal:
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def tipo(self) -> Tipo:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: Tipo):
        if isinstance(tipo, Tipo):
            self.__tipo = tipo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
