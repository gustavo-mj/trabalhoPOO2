class Pessoa:
    # Atributos: cpf, nome, data de nascimento, endereço, tipo de habitação, tamanho da habitação, número de animais
    def __init__(self, cpf: str, nome: str, dataNasc: str, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int):
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
        if isinstance(dataNasc, str):
            self.__dataNasc = dataNasc
        if isinstance(endereco, str):
            self.__endereco = endereco
        if isinstance(tipoHab, str):
            self.__tipoHab = tipoHab
        if isinstance(tamanhoHab, str):
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
    def dataNasc(self) -> str:
        return self.__dataNasc

    @dataNasc.setter
    def dataNasc(self, dataNasc: str):
        if isinstance(dataNasc, str):
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
        if isinstance(tipoHab, str):
            self.__tipoHab = tipoHab

    # Getter e Setter para tamanhoHab
    @property
    def tamanhoHab(self) -> str:
        return self.__tamanhoHab

    @tamanhoHab.setter
    def tamanhoHab(self, tamanhoHab: str):
        if isinstance(tamanhoHab, str):
            self.__tamanhoHab = tamanhoHab

    # Getter e Setter para numeroAnimais
    @property
    def numeroAnimais(self) -> int:
        return self.__numeroAnimais

    @numeroAnimais.setter
    def numeroAnimais(self, numeroAnimais: int):
        if isinstance(numeroAnimais, int):
            self.__numeroAnimais = numeroAnimais