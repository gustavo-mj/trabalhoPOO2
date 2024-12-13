from DAOs.dao import DAO
from entidade.gato import *
from entidade.cachorro import *
from entidade.animal import *

class AnimalDAO(DAO):
    def __init__(self):
        super().__init__('animais.pkl')

    def add(self, animal: Animal):
        if((animal is not None) and isinstance(animal, Animal) and isinstance(animal.chip, int)):
            super().add(animal.chip, animal)

    def update(self, animal: Animal):
        if((animal is not None) and isinstance(animal, Animal) and isinstance(animal.chip, int)):
            super().update(animal.chip, animal)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)