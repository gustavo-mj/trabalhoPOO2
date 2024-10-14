from limite.tela_doacao import TelaDoacao
from entidade.doacao import Doacao
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
        self.__controlador_sistema.controlador_animais.lista_animal()
        self.__controlador_sistema.controlador_pessoas.lista_pessoa()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_doacao["chip"])
        pessoa = self.__controlador_sistema.controlador_pessoas.pega_pessoa_por_cpf(dados_doacao["cpf"])

        if(animal is not None and pessoa is not None):
            doacao = Doacao(randint(0, 100), dados_doacao["data"], animal, pessoa, dados_doacao["motivo"])
            self.__doacoes.append(doacao)
        else:
            self.__tela_doacao.mostra_mensagem("Dados inválidos")

    def lista_doacao(self):
        dados_listagem = self.__tela_doacao.pega_dados_listagem()
        if not dados_listagem:
            for d in self.__doacoes:
                self.__tela_doacao.mostra_doacao({
                    "codigo" : d.codigo,
                    "nome_animal" : d.animal.nome,
                    "chip_animal" : d.animal.chip,
                    "nome_doador" : d.pessoa.nome,
                    "cpf_doador" : d.pessoa.cpf
                })
        else:
            for d in self.__doacoes:
                if (d.data > dados_listagem["início"]) and (d.data < dados_listagem["fim"]):
                    self.__tela_doacao.mostra_doacao({
                        "codigo" : d.codigo,
                        "nome_animal" : d.animal.nome,
                        "chip_animal" : d.animal.chip,
                        "nome_doador" : d.pessoa.nome,
                        "cpf_doador" : d.pessoa.cpf
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

    def retonar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_doacao, 2: self.lista_doacao, 3: self.excluir_doacao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_doacao.tela_opcoes()]()
        