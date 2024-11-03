class Animal:
    # Atributos: chip, nome, raça, tamanho, carteira vacinal
    def __init__(self, chip: int, nome: str, raca: str):
        self.__chip = None
        self.__nome = None
        self.__raca = None
        self.__vacinas = []
        
        if isinstance(chip, int):
            self.__chip = chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca

    # Getter e Setter para chip
    @property
    def chip(self) -> int:
        return self.__chip

    @chip.setter
    def chip(self, chip: int):
        if isinstance(chip, int):
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

    @property
    def vacinas(self):
        return self.__vacinas
