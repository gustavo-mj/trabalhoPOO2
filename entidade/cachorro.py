from entidade.animal import Animal
from enum import Enum

class TamanhoAnimal(Enum):
    pequeno = 1
    medio = 2
    grande = 3

class Cachorro(Animal):

    def __init__(self, chip: int, nome: str, raca: str, tamanho: TamanhoAnimal):
        super().__init__(chip, nome, raca)
        self.__tamanho = None
        if isinstance(tamanho, TamanhoAnimal):
            self.__tamanho = tamanho

    # Getter e Setter para tamanho
    @property
    def tamanho(self) -> TamanhoAnimal:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: TamanhoAnimal):
        if isinstance(tamanho, TamanhoAnimal):
            self.__tamanho = tamanho