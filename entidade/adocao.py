from entidade.pessoa import *
from entidade.animal import *
from entidade.adotante import *
from entidade.registro import *
from datetime import date

class Adocao(Registro):

    def __init__(self, codigo: int, data: date, animal: Animal, adotante: Adotante, termo: bool):
        super().__init__(codigo, data, animal)
        self.__adotante = None
        self.__termo = None
        if isinstance(termo, bool):
            self.__termo = termo
        if isinstance(adotante, Adotante):
            self.__adotante = adotante

    @property
    def termo(self) -> bool:
        return self.__termo

    @termo.setter
    def termo(self, termo: bool):
        if isinstance(termo, bool):
            self.__termo = termo

    @property
    def adotate(self) -> Adotante:
        return self.__adotante

    @adotate.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
