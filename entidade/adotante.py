from entidade.pessoa import *
from datetime import date
from enum import Enum


class TipoHabitacao(Enum):
    casa = 1
    apartamento = 2


class TamanhoHabitacao(Enum):
    pequeno = 1
    medio = 2
    grande = 3


class Adotante(Pessoa):

    def __init__(
        self,
        cpf: int,
        nome: str,
        data_de_nascimento: date,
        endereco: str,
        tipo_de_habitacao: TipoHabitacao,
        tamanho_da_habitacao: TamanhoHabitacao,
        numero_de_animais: int
    ):
        super().__init__(cpf, nome, data_de_nascimento, endereco)

        self.__tipo_de_habitacao = None
        self.__tamanho_da_habitacao = None
        self.__numero_de_animais = None

        if isinstance(tipo_de_habitacao, TipoHabitacao):
            self.__tipo_de_habitacao = tipo_de_habitacao
        if isinstance(tamanho_da_habitacao, TamanhoHabitacao):
            self.__tamanho_da_habitacao = tamanho_da_habitacao
        if isinstance(numero_de_animais, int):
            self.__numero_de_animais = numero_de_animais

    # Getter e Setter para tipoHab
    @property
    def tipo_de_habitacao(self) -> TipoHabitacao:
        return self.__tipo_de_habitacao

    @tipo_de_habitacao.setter
    def tipo_de_habitacao(self, tipo_de_habitacao: TipoHabitacao):
        if isinstance(tipo_de_habitacao, TipoHabitacao):
            self.__tipo_de_habitacao = tipo_de_habitacao

    # Getter e Setter para tamanhoHab
    @property
    def tamanho_da_habitacao(self) -> TamanhoHabitacao:
        return self.__tamanho_da_habitacao

    @tamanho_da_habitacao.setter
    def tamanho_da_habitacao(self, tamanho_da_habitacao: TamanhoHabitacao):
        if isinstance(tamanho_da_habitacao, TamanhoHabitacao):
            self.__tamanho_da_habitacao = tamanho_da_habitacao

    # Getter e Setter para numeroAnimais
    @property
    def numero_de_animais(self) -> int:
        return self.__numero_de_animais

    @numero_de_animais.setter
    def numero_de_animais(self, numero_de_animais: int):
        if isinstance(numero_de_animais, int):
            self.__numero_de_animais = numero_de_animais