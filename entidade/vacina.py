from entidade.animal import *
from enum import Enum
from datetime import date


class Tipo(Enum):
    raiva = 1
    leptospirose = 2
    hepatite = 3


class Vacina():

    def __init__(self, tipo: Tipo, data: date):
        self.__tipo = None
        self.__data = None
        if isinstance(tipo, Tipo):
            self.__tipo = tipo
        if isinstance(data, date):
            self.__data = date

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
