from datetime import date

class Pessoa:
    # Atributos: cpf, nome, data de nascimento, endereço, tipo de habitação, tamanho da habitação, número de animais
    def __init__(self, cpf: str, nome: str, dataNasc: date, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int):
        self.__cpf = None
        self.__nome = None
        self.__dataNasc = None
        self.__endereco = None
        self.__tipoHab = None
        self.__tamanhoHab = None
        self.__numeroAnimais = None

        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(dataNasc, date):
            self.__dataNasc = dataNasc
        if isinstance(endereco, str):
            self.__endereco = endereco
        if tipoHab in ['casa', 'apartamento']:
            self.__tipoHab = tipoHab
        if tamanhoHab in ['pequeno', 'médio', 'grande']:
            self.__tamanhoHab = tamanhoHab
        if isinstance(numeroAnimais, int):
            self.__numeroAnimais = numeroAnimais
    
    # Getter e Setter para cpf
    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
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
    def dataNasc(self) -> date:
        return self.__dataNasc

    @dataNasc.setter
    def dataNasc(self, dataNasc: date):
        if isinstance(dataNasc, date):
            self.__dataNasc = dataNasc

    # Getter e Setter para endereco
    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    # Getter e Setter para tipoHab
    @property
    def tipoHab(self) -> str:
        return self.__tipoHab

    @tipoHab.setter
    def tipoHab(self, tipoHab: str):
        if tipoHab in ['casa', 'apartamento']:
            self.__tipoHab = tipoHab

    # Getter e Setter para tamanhoHab
    @property
    def tamanhoHab(self) -> str:
        return self.__tamanhoHab

    @tamanhoHab.setter
    def tamanhoHab(self, tamanhoHab: str):
        if tamanhoHab in ['pequeno', 'médio', 'grande']:
            self.__tamanhoHab = tamanhoHab

    # Getter e Setter para numeroAnimais
    @property
    def numeroAnimais(self) -> int:
        return self.__numeroAnimais

    @numeroAnimais.setter
    def numeroAnimais(self, numeroAnimais: int):
        if isinstance(numeroAnimais, int):
            self.__numeroAnimais = numeroAnimais

    def idade(self, data: date) -> int:
        if isinstance(data, date):
            idade = self.__dataNasc.year - data.year
        if (data.month, data.day) < (self.__dataNasc.month, self.__dataNasc.day):
            idade -= 1
        return idade