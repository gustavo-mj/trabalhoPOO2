from limite.tela_registros import TelaDoacao
from entidade.doacao import Doacao
from entidade.doador import Doador
from random import randint


class ControladorDoacoes():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__doacoes = []
        self.__tela_doacao = TelaDoacao()

    def pega_doacao_por_codigo(self, codigo: int):
        for doacao in self.__doacoes:
            if(doacao.codigo == codigo):
                return doacao
        return None

    def cadastrar_doacao(self):
        self.__controlador_sistema.controlador_animais.lista_animais()
        self.__controlador_sistema.controlador_doadores.lista_doador()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_doacao["chip"])
        doador = self.__controlador_sistema.controlador_doadores.pega_doador_por_cpf(dados_doacao["cpf"])

        if(animal is not None and doador is not None):
            doacao = Doacao(randint(0, 100), dados_doacao["data"], animal, doador, dados_doacao["motivo"])
            self.__doacoes.append(doacao)
            self.lista_doacao()
        else:
            self.__tela_doacao.mostra_mensagem("Dados inválidos")

    def alterar_cadastro(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(int(codigo_doacao))

        if (doacao is not None):
            novos_dados_doacao = self.__tela_doacao.pega_dados_doacao()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(novos_dados_doacao["chip"])
            doador = self.__controlador_sistema.controlador_doadores.pega_doador_por_cpf(novos_dados_doacao["cpf"])
            if(animal is not None and doador is not None):
                doacao.data = novos_dados_doacao["data"]
                doacao.animal = animal
                doacao.doador = doador
                doacao.motivo = novos_dados_doacao["motivo"]
        else:
            self.__tela_doacao.mostra_mensagem("Dados inválidos")

    def lista_doacao(self):
        for d in self.__doacoes:
            self.__tela_doacao.mostra_doacao({
                "codigo" : d.codigo,
                "nome_animal" : d.animal.nome,
                "chip_animal" : d.animal.chip,
                "nome_doador" : d.doador.nome,
                "cpf_doador" : d.doador.cpf,
                "data" : d.data
            })

    def lista_doacoes_periodo(self):
        dados_periodo = self.__tela_doacao.seleciona_periodo()
        inicio = dados_periodo["inicio"]
        fim = dados_periodo["fim"]
        for d in self.__doacoes:
            if (inicio <= d.data <= fim):
                self.__tela_doacao.mostra_doacao({
                    "codigo" : d.codigo,
                    "nome_animal" : d.animal.nome,
                    "chip_animal" : d.animal.chip,
                    "nome_doador" : d.doador.nome,
                    "cpf_doador" : d.doador.cpf,
                    "data" : d.data
                })

    def excluir_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(int(codigo_doacao))

        if(doacao is not None):
            self.__doacoes.remove(doacao)
            self.lista_doacao()
        else:
            self.__tela_doacao.mostra_mensagem("ATENÇÃO: esta doação não existe.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_doacao,
            2: self.alterar_cadastro,
            3: self.lista_doacao,
            4: self.lista_doacoes_periodo,
            5: self.excluir_doacao,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_doacao.tela_opcoes()]()
        