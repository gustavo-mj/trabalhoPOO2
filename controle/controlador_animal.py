from limite.tela_animal import TelaAnimal
from entidade.animal import *


class ControladorAnimal():

    def __init__(self, controlador_sistema):
        self.__animais = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_animal = TelaAnimal()

    @property
    def animais(self) -> list:
        return self.__animais

    def pega_animal_por_chip(self, chip: int):
        for animal in self.__animais:
            if(animal.chip == chip):
                return animal
        return None

    def cadastrar_animal(self):
        dados_animal = self.__tela_animal.pega_dados_animal()
        a = self.pega_animal_por_chip(dados_animal["chip"])
        if a is None:
            animal = Animal(
                dados_animal["chip"],
                dados_animal["nome"],
                dados_animal["raca"],
                TamanhoAnimal(dados_animal["tamanho"])
            )
            self.__animais.append(animal)
        else:
            self.__tela_livro.mostra_mensagem("ATENÇÃO: Animal já cadastrado.")

    def alterar_cadastro(self):
        self.lista_animal()
        chip_animal = self.__tela_animal.seleciona_animal()
        animal = self.pega_animal_por_chip(chip_animal)

        if(animal is not None):
            novos_dados_animal = self.__tela_animal.pega_dados_animal()
            animal.chip = novos_dados_animal["chip"]
            animal.nome = novos_dados_animal["nome"]
            animal.raca = novos_dados_animal["raca"]
            animal.tamanho = TamanhoAnimal(novos_dados_animal["tamanho"])
            self.lista_animal()
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Animal não cadastrado.")

    def lista_animal(self):
        for animal in self.__animais:
            self.__tela_animal.mostra_animal({
                "chip" : animal.chip,
                "nome" : animal.nome,
                "raca" : animal.raca,
                "tamanho" : animal.tamanho.name
            })

    def excluir_animal(self):
        self.lista_animal()
        chip_animal = self.__tela_animal.seleciona_animal()
        animal = self.pega_animal_por_chip(chip_animal)

        if(animal is not None):
            self.__animais.remove(animal)
            self.lista_animal()
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Animal não cadastrado.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_animal, 2: self.alterar_cadastro, 3: self.lista_animal, 4: self.excluir_animal, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
            