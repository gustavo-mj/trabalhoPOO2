from entidade.pessoa import *
from entidade.animal import *
from entidade.registro import *
from datetime import date

class Doacao(Registro):

    def __init__(self, codigo: int, data: date, animal: Animal, doador: Pessoa, motivo: str):
        super().__init__(codigo, data, animal, doador)
        self.__motivo = None
        if isinstance(motivo, str):
            self.__motivo = motivo

    @property
    def motivo(self) -> str:
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo