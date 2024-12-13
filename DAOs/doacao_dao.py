from DAOs.dao import DAO
from entidade.doacao import *


class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacoes.pkl')

    def add(self, doacao: Doacao):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(doacao.codigo, int)):
            super().add(doacao.codigo, doacao)

    def update(self, doacao: Doacao):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(doacao.codigo, int)):
            super().update(doacao.codigo, doacao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)