from limite.tela_registros import TelaAdocao
from entidade.adocao import Adocao
from entidade.animal import *
from entidade.cachorro import *
from entidade.gato import *
from entidade.adotante import *
from random import randint
from dateutil.relativedelta import relativedelta
from exception.lista_vazia_exception import ListaVaziaException
from exception.dados_invalidos_exception import DadosInvalidosException
from exception.cadastro_inexistente_exception import CadastroInexistenteException


class ControladorAdocoes():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()

    def pega_adocao_por_codigo(self, codigo: int):
        for adocao in self.__adocoes:
            if(adocao.codigo == codigo):
                return adocao
        return None

    def cadastrar_adocao(self):
        try:
            if not self.__controlador_sistema.controlador_animais.animais:
                raise ListaVaziaException()
            if not self.__controlador_sistema.controlador_adotantes.adotantes:
                raise ListaVaziaException()
            self.__controlador_sistema.controlador_animais.listar_disponiveis()
            self.__controlador_sistema.controlador_adotantes.lista_adotante()
            dados_adocao = self.__tela_adocao.pega_dados_adocao()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_adocao["chip"])
            adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(dados_adocao["cpf"])
            data = dados_adocao["data"]
            diferenca = relativedelta(data, adotante.data_de_nascimento)
            if (animal is not None and adotante is not None) and (animal.status == Status.disponivel):
                if isinstance(animal, Cachorro):
                    if (animal.tamanho != TamanhoAnimal.grande) or (adotante.tipo_de_habitacao != TipoHabitacao.apartamento) or (adotante.tamanho_da_habitacao != TamanhoHabitacao.pequeno):
                        adocao = Adocao(randint(0, 100), data, animal, adotante, True)
                        self.__adocoes.append(adocao)
                        animal.status = Status.adotado
                    else:
                        self.__tela_adocao.mostra_mensagem("Cachorro e habitação incompatíveis.")
                else:
                    adocao = Adocao(randint(0, 100), data, animal, adotante, True)
                    self.__adocoes.append(adocao)
                    animal.status = Status.adotado
            else:
                raise DadosInvalidosException()
        except ListaVaziaException as e:
            self.__tela_adocao.mostra_mensagem(e)
        except DadosInvalidosException as e:
            self.__tela_adocao.mostra_mensagem(e)

    def alterar_cadastro(self):
        try:
            if not self.__adocoes:
                raise ListaVaziaException()
            self.lista_adocao()
            codigo = self.__tela_adocao.seleciona_adocao()
            adocao = self.pega_adocao_por_codigo(codigo)
            if(adocao is not None):
                adocao.animal.status = Status.disponivel
                novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
                animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(novos_dados_adocao["chip"])
                animal.status = Status.adotado
                adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(novos_dados_adocao["cpf"])
                adocao.data = novos_dados_adocao["data"]
                adocao.animal = animal
                adocao.adotante = adotante
            else:
                raise CadastroInexistenteException()
        except ListaVaziaException as e:
            self.__tela_adocao.mostra_mensagem(e)
        except CadastroInexistenteException as e:
            self.__tela_adocao.mostra_mensagem(e)

    def lista_adocao(self):
        dados_adocao = []
        for a in self.__adocoes:
            dados_adocao.append({
                "codigo" : a.codigo,
                "nome_animal" : a.animal.nome,
                "chip_animal" : a.animal.chip,
                "nome_adotante" : a.adotante.nome,
                "cpf_adotante" : a.adotante.cpf,
                "data" : a.data
            })
            self.__tela_adocao.mostra_adocao(dados_adocao)

    def lista_adocao_periodo(self):
        try:
            if not self.__adocoes:
                raise ListaVaziaException()
            else:
                dados_periodo = self.__tela_adocao.seleciona_periodo()
                inicio = dados_periodo["inicio"]
                fim = dados_periodo["fim"]
                dados_adocao = []
                for a in self.__adocoes:
                    if (inicio <= a.data <= fim):
                        dados_adocao.append({
                            "codigo" : a.codigo,
                            "nome_animal" : a.animal.nome,
                            "chip_animal" : a.animal.chip,
                            "nome_doador" : a.doador.nome,
                            "cpf_doador" : a.doador.cpf,
                            "data" : a.data
                        })
                self.__tela_adocao.mostra_adocao(dados_adocao)
        except ListaVaziaException as e:
            self.__tela_adocao.mostra_mensagem(e)

    def excluir_adocao(self):
        try:
            if not self.__adocoes:
                raise ListaVaziaException()
            else:
                self.lista_adocao()
                codigo_adocao = self.__tela_adocao.seleciona_adocao()
                adocao = self.pega_adocao_por_codigo(codigo_adocao)
                if(adocao is not None):
                    adocao.animal.status = Status.disponivel
                    self.__adocoes.remove(adocao)
                    self.lista_adocao()
                else:
                    raise CadastroInexistenteException()
        except ListaVaziaException as e:
            self.__tela_adocao.mostra_mensagem(e)
        except CadastroInexistenteException as e:
            self.__tela_adocao.mostra_mensagem(e)

    def listar_disponiveis(self):
        self.__controlador_sistema.controlador_animais.listar_disponiveis()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_disponiveis,
            2: self.cadastrar_adocao,
            3: self.alterar_cadastro,
            4: self.lista_adocao,
            5: self.lista_adocao_periodo,
            6: self.excluir_adocao,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()