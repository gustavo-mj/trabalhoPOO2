from entidade.doador import *
from entidade.animal import *
from entidade.registro import *
from datetime import date

class Doacao(Registro):

    def __init__(self, codigo: int, data: date, animal: Animal, doador: Doador, motivo: str):
        super().__init__(codigo, data, animal)
        self.__doador = None
        self.__motivo = None
        if isinstance(motivo, str):
            self.__motivo = motivo
        if isinstance(doador, Doador):
            self.__doador = doador

    @property
    def motivo(self) -> str:
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo

    @property
    def doador(self) -> Doador:
        return self.__doador

    @doador.setter
    def doador(self, doador: Doador):
        if isinstance(doador, Doador):
            self.__doador = doador