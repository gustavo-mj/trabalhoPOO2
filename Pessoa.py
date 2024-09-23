class Pessoa:
    #atributos:cpf, nome, data de nascimento, endereço, tipo da habitação (casa ou apartamento; pequeno, médio ou grande)
    #e se já possui outros animais em casa
    def __init__(self, cpf: str, nome: str, dataNasc: int, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int):
        self.__cpf = None
        self.__nome = None
        self.__dataNasc = None
        self.__endereco = None
        self.__tipoHab = None
        self.__tamanhoHab = None
        self.__numeroAnimais = None
        if isinstance(cpf, str):
            self.__cpf = cpf