from entidade.vacina import *


class Status(Enum):
    nao_disponivel = 1
    disponivel = 2
    adotado = 3


class Animal:
    # Atributos: chip, nome, raça, tamanho, carteira vacinal
    def __init__(self, chip: int, nome: str, raca: str):
        self.__status = Status.nao_disponivel
        self.__chip = None
        self.__nome = None
        self.__raca = None
        self.__vacinas = []
        
        if isinstance(chip, int):
            self.__chip = chip
        else:
            raise ExcecaoEntradaInvalida()
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ExcecaoEntradaInvalida()
        if isinstance(raca, str):
            self.__raca = raca
        else:
            raise ExcecaoEntradaInvalida()

    @property
    def status(self) -> Status:
        return self.__status

    @status.setter
    def status(self, status: Status):
        if isinstance(status, Status):
            self.__status = status
        else:
            raise ExcecaoEntradaInvalida()

    # Getter e Setter para chip
    @property
    def chip(self) -> int:
        return self.__chip

    @chip.setter
    def chip(self, chip: int):
        if isinstance(chip, int):
            self.__chip = chip
        else:
            raise ExcecaoEntradaInvalida()

    # Getter e Setter para nome
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ExcecaoEntradaInvalida()

    # Getter e Setter para raça
    @property
    def raca(self) -> str:
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca
        else:
            raise ExcecaoEntradaInvalida()

    @property
    def vacinas(self) -> list:
        return self.__vacinas

    def adicionar_vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            self.__vacinas.append(vacina)
        else:
            raise ExcecaoEntradaInvalida()

    def excluir_vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            self.__vacinas.remove(vacina)
        else:
            raise ExcecaoEntradaInvalida()
