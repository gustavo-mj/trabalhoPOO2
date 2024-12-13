from DAOs.dao import DAO
from entidade.adocao import *


class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__('adocoes.pkl')

    def add(self, adocao: Adocao):
        if((adocao is not None) and isinstance(adocao, Adocao) and isinstance(adocao.codigo, int)):
            super().add(adocao.codigo, adocao)

    def update(self, adocao: Adocao):
        if((adocao is not None) and isinstance(adocao, Adocao) and isinstance(adocao.codigo, int)):
            super().update(adocao.codigo, adocao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)