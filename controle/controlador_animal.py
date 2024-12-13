from limite.tela_animal import TelaAnimal
from entidade.animal import *
from entidade.cachorro import *
from entidade.gato import *
from DAOs.animal_dao import AnimalDAO

class ControladorAnimal():

    def __init__(self, controlador_sistema):
        #self.__animais = []
        self.__animal_DAO = AnimalDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_animal = TelaAnimal()

    @property
    def animais(self):
        return self.__animal_DAO.get_all()

    def update_remoto(self, animal: Animal):
        self.__animal_DAO.update(animal)

    def pega_animal_por_chip(self, chip: int):
        #for animal in self.__animais:
        for animal in self.__animal_DAO.get_all():
            print(animal.chip)
            if(animal.chip == chip):
                return animal
        return None

    def cadastrar_cachorro(self):
        dados_cachorro = self.__tela_animal.pega_dados_cachorro()
        c = self.pega_animal_por_chip(dados_cachorro["chip"])
        if c is None:
            cachorro = Cachorro(
                dados_cachorro["chip"],
                dados_cachorro["nome"],
                dados_cachorro["raca"],
                dados_cachorro["tamanho"]
            )
            #self.__animais.append(cachorro)
            self.__animal_DAO.add(cachorro)
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Cachorro já cadastrado.")

    def cadastrar_gato(self):
        dados_gato = self.__tela_animal.pega_dados_gato()
        g = self.pega_animal_por_chip(dados_gato["chip"])
        if g is None:
            gato = Gato(
                dados_gato["chip"],
                dados_gato["nome"],
                dados_gato["raca"],
            )
            #self.__animais.append(gato)
            self.__animal_DAO.add(gato)
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Gato já cadastrado.")

    def alterar_cadastro(self):
        self.lista_animais()
        chip_animal = self.__tela_animal.seleciona_animal()
        animal = self.pega_animal_por_chip(chip_animal)
        if(animal is not None):
            if isinstance(animal, Cachorro):
                novos_dados_animal = self.__tela_animal.pega_dados_cachorro_alteracao()
                animal.nome = novos_dados_animal["nome"]
                animal.raca = novos_dados_animal["raca"]
                animal.tamanho = TamanhoAnimal(novos_dados_animal["tamanho"])
            else:
                novos_dados_animal = self.__tela_animal.pega_dados_gato_alteracao()
                animal.nome = novos_dados_animal["nome"]
                animal.raca = novos_dados_animal["raca"]
            self.__animal_DAO.update(animal)
            self.lista_animais()
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Animal não cadastrado.")

    def lista_animais(self):
        dados_animal = []
        #for animal in self.__animais:
        for animal in self.__animal_DAO.get_all():
            if isinstance(animal, Cachorro):
                dados_animal.append({
                    "especie" : "cachorro",
                    "status" : animal.status.name,
                    "chip" : animal.chip,
                    "nome" : animal.nome,
                    "raca" : animal.raca,
                    "tamanho" : animal.tamanho.name
                })
            else:
                dados_animal.append({
                    "especie" : "gato",
                    "status" : animal.status.name,
                    "chip" : animal.chip,
                    "nome" : animal.nome,
                    "raca" : animal.raca
                })
        self.__tela_animal.mostra_animal(dados_animal)

    def listar_disponiveis(self):
        dados_animal = []
        #for animal in self.__animais:
        for animal in self.__animal_DAO.get_all():
            if animal.status == Status.disponivel:
                if isinstance(animal, Cachorro):
                    dados_animal.append({
                        "especie" : "cachorro",
                        "status" : animal.status.name,
                        "chip" : animal.chip,
                        "nome" : animal.nome,
                        "raca" : animal.raca,
                        "tamanho" : animal.tamanho.name
                    })
                else:
                    dados_animal.append({
                        "especie" : "gato",
                        "status" : animal.status.name,
                        "chip" : animal.chip,
                        "nome" : animal.nome,
                        "raca" : animal.raca
                    })
        self.__tela_animal.mostra_animal(dados_animal)

    def excluir_animal(self):
        self.lista_animais()
        chip_animal = self.__tela_animal.seleciona_animal()
        animal = self.pega_animal_por_chip(chip_animal)

        if(animal is not None):
            #self.__animais.remove(animal)
            self.__animal_DAO.remove(animal.chip)
            self.lista_animais()
        else:
            self.__tela_animal.mostra_mensagem("ATENÇÃO: Animal não cadastrado.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_cachorro,
            2: self.cadastrar_gato,
            3: self.alterar_cadastro,
            4: self.lista_animais,
            5: self.excluir_animal,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
            