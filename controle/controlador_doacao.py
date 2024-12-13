from limite.tela_registros import TelaDoacao
from entidade.doacao import Doacao
from entidade.doador import Doador
from random import randint
from exception.lista_vazia_exception import ListaVaziaException
from exception.dados_invalidos_exception import DadosInvalidosException
from exception.cadastro_inexistente_exception import CadastroInexistenteException
from DAOs.doacao_dao import DoacaoDAO


class ControladorDoacoes():

    def __init__(self, controlador_sistema):
        #self.__doacoes = []
        self.__doacao_DAO = DoacaoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_doacao = TelaDoacao()

    def pega_doacao_por_codigo(self, codigo: int):
        #for doacao in self.__doacoes:
        for doacao in self.__doacao_DAO.get_all():
            print(doacao.codigo)
            if(doacao.codigo == codigo):
                return doacao
        return None

    def cadastrar_doacao(self):
        try:
            if not self.__controlador_sistema.controlador_animais.animais:
                raise ListaVaziaException()
            if not self.__controlador_sistema.controlador_doadores.doadores:
                raise ListaVaziaException()
            self.__controlador_sistema.controlador_animais.lista_animais()
            self.__controlador_sistema.controlador_doadores.lista_doador()
            dados_doacao = self.__tela_doacao.pega_dados_doacao()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_doacao["chip"])
            doador = self.__controlador_sistema.controlador_doadores.pega_doador_por_cpf(dados_doacao["cpf"])
            if(animal is not None and doador is not None):
                doacao = Doacao(randint(0, 100), dados_doacao["data"], animal, doador, dados_doacao["motivo"])
                #self.__doacoes.append(doacao)
                self.__doacao_DAO.add(doacao)
                self.lista_doacao()
            else:
                raise DadosInvalidosException()
        except ListaVaziaException as e:
            self.__tela_doacao.mostra_mensagem(e)
        except DadosInvalidosException as e:
            self.__tela_doacao.mostra_mensagem(e)

    def alterar_cadastro(self):
        try:
            #if not self.__doacoes:
            if not self.__doacao_DAO.get_all():
                raise ListaVaziaException()
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
                    self.__doacao_DAO.update(doacao)
                    self.lista_doacao()
                else:
                    raise DadosInvalidosException()
            else:
                raise DadosInvalidosException()
        except ListaVaziaException as e:
            self.__tela_doacao.mostra_mensagem(e)
        except DadosInvalidosException as e:
            self.__tela_doacao.mostra_mensagem(e)

    def lista_doacao(self):
        dados_doacao = []
        #for d in self.__doacoes:
        for d in self.__doacao_DAO.get_all():
            dados_doacao.append({
                "codigo" : d.codigo,
                "nome_animal" : d.animal.nome,
                "chip_animal" : d.animal.chip,
                "nome_doador" : d.doador.nome,
                "cpf_doador" : d.doador.cpf,
                "data" : d.data
            })
        self.__tela_doacao.mostra_doacao(dados_doacao)

    def lista_doacoes_periodo(self):
        dados_doacao = []
        try:
            #if not self.__doacoes:
            if not self.__doacao_DAO.get_all():
                raise ListaVaziaException()
            else:
                dados_periodo = self.__tela_doacao.seleciona_periodo()
                inicio = dados_periodo["inicio"]
                fim = dados_periodo["fim"]
                #for d in self.__doacoes:
                for d in self.__doacao_DAO.get_all():
                    if (inicio <= d.data <= fim):
                        dados_doacao.append({
                            "codigo" : d.codigo,
                            "nome_animal" : d.animal.nome,
                            "chip_animal" : d.animal.chip,
                            "nome_doador" : d.doador.nome,
                            "cpf_doador" : d.doador.cpf,
                            "data" : d.data
                        })
                self.__tela_doacao.mostra_doacao(dados_doacao)
        except ListaVaziaException as e:
            self.__tela_doacao.mostra_mensagem(e)

    def excluir_doacao(self):
        try:
            #if not self.__doacoes:
            if not self.__doacao_DAO.get_all():
                raise ListaVaziaException()
            self.lista_doacao()
            codigo_doacao = self.__tela_doacao.seleciona_doacao()
            doacao = self.pega_doacao_por_codigo(int(codigo_doacao))
            if(doacao is not None):
                #self.__doacoes.remove(doacao)
                self.__doacao_DAO.remove(doacao.codigo)
                self.lista_doacao()
            else:
                raise CadastroInexistenteException()
        except ListaVaziaException as e:
            self.__tela_doacao.mostra_mensagem(e)
        except CadastroInexistenteException as e:
            self.__tela_doacao.mostra_mensagem(e)

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
        