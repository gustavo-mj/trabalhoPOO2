class Animal:
    # Atributos: chip, nome, raça, tamanho
    def __init__(self, chip: str, nome: str, raca: str, tamanho: str):
        self.__chip = None
        self.__nome = None
        self.__raca = None
        self.__tamanho = None
        
        if isinstance(chip, str):
            self.__chip = chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        if isinstance(tamanho, str):
            self.__tamanho = tamanho

    # Getter e Setter para chip
    @property
    def chip(self) -> str:
        return self.__chip

    @chip.setter
    def chip(self, chip: str):
        if isinstance(chip, str):
            self.__chip = chip

    # Getter e Setter para nome
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    # Getter e Setter para raça
    @property
    def raca(self) -> str:
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca

    # Getter e Setter para tamanho
    @property
    def tamanho(self) -> str:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: str):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho