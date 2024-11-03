from datetime import date


class Pessoa:
    # Atributos: cpf, nome, data de nascimento e endereço
    def __init__(self, cpf: int, nome: str, data_de_nascimento: date, endereco: str):

        self.__cpf = None
        self.__nome = None
        self.__data_de_nascimento = None
        self.__endereco = None

        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(data_de_nascimento, date):
            self.__data_de_nascimento = data_de_nascimento
        if isinstance(endereco, str):
            self.__endereco = endereco
    
    # Getter e Setter para cpf
    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    # Getter e Setter para nome
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    # Getter e Setter para dataNasc
    @property
    def data_de_nascimento(self) -> date:
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: date):
        if isinstance(data_de_nascimento, date):
            self.__data_de_nascimento = data_de_nascimento

    # Getter e Setter para endereco
    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
