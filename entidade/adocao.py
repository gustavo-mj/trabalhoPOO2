from entidade.pessoa import *
from entidade.animal import *
from entidade.registro import *
from datetime import date

class Adocao(Registro):

    def __init__(self, codigo: int, data: date, animal: Animal, adotante: Pessoa, termo: bool):
        super().__init__(codigo, data, animal, adotante)
        self.__termo = None
        if isinstance(termo, bool):
            self.__termo = termo

    @property
    def termo(self) -> bool:
        return self.__termo

    @termo.setter
    def termo(self, termo: bool):
        if isinstance(termo, bool):
            self.__termo = termo
