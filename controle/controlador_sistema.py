from limite.tela_sistema import TelaSistema
from controle.controlador_animal import ControladorAnimal
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_doacao import ControladorDoacoes
from controle.controlador_adocao import ControladorAdocoes
from controle.controlador_vacina import ControladorVacina

class ControladorSistema:

    def __init__(self):
        self.__controlador_animais = ControladorAnimal(self)
        self.__controlador_pessoas = ControladorPessoa(self)
        self.__controlador_doacoes = ControladorDoacoes(self)
        self.__controlador_adocoes = ControladorAdocoes(self)
        self.__controlador_vacinacoes = ControladorVacina(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_animais(self):
        return self.__controlador_animais
    
    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    @property
    def controlador_doacoes(self):
        return self.__controlador_doacoes

    @property
    def controlador_adocoes(self):
        return self.__controlador_adocoes

    @property
    def controlador_vacinacoes(self):
        return self.__controlador_vacinacoes

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_animal(self):
        self.__controlador_animais.abre_tela()

    def cadastra_pessoa(self):
        self.__controlador_pessoas.abre_tela()

    def cadastra_doacao(self):
        self.__controlador_doacoes.abre_tela()

    def cadastra_adocao(self):
        self.__controlador_adocoes.abre_tela()

    def cadastra_vacinacao(self):
        self.__controlador_vacinacoes.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_animal,
            2: self.cadastra_pessoa,
            3: self.cadastra_doacao,
            4: self.cadastra_adocao,
            5: self.cadastra_vacinacao,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
