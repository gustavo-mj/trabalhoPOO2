from limite.tela_pessoas import *
from entidade.doador import *
from entidade.adotante import *
from DAOs.doador_dao import DoadorDAO
from DAOs.adotante_dao import AdotanteDAO


class ControladorDoador():

    def __init__(self, controlador_sistema):
        #self.__doadores = []
        self.__doador_DAO = DoadorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_doador = TelaDoador()

    '''
    @property
    def doadores(self) -> list:
        return self.__doadores
    '''

    @property
    def doadores(self):
        return self.__doador_DAO.get_all()

    def pega_doador_por_cpf(self, cpf: int):
        #for doador in self.__doadores:
        for doador in self.__doador_DAO.get_all():
            print(doador.cpf)
            if(doador.cpf == cpf):
                return doador
        return None

    def cadastrar_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        d = self.pega_doador_por_cpf(dados_doador["cpf"])
        if d is None:
            doador = Doador(
                dados_doador["cpf"],
                dados_doador["nome"],
                dados_doador["data_de_nascimento"],
                dados_doador["endereco"]
            )
            #self.__doadores.append(doador)
            self.__doador_DAO.add(doador)
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Doador já cadastrado.")

    def alterar_cadastro(self):
        self.lista_doador()
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        if(doador is not None):
            novos_dados_doador = self.__tela_doador.pega_dados_doador()
            doador.cpf = novos_dados_doador["cpf"] #não deve ser alterado!!!!!!!!
            doador.nome = novos_dados_doador["nome"]
            doador.data_de_nascimento = novos_dados_doador["data_de_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
            self.__doador_DAO.update(doador)
            self.lista_doador()
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Doador não cadastrado.")

    def lista_doador(self):
        dados_doador = []
        #for doador in self.__doadores:
        for doador in self.__doador_DAO.get_all():
            dados_doador.append({
                "cpf" : doador.cpf,
                "nome" : doador.nome,
                "data_de_nascimento" : doador.data_de_nascimento,
                "endereco" : doador.endereco
            })
        self.__tela_doador.mostra_doador(dados_doador)

    def excluir_doador(self):
        self.lista_doador()
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        if(doador is not None):
            #self.__doadores.remove(doador)
            self.__doador_DAO.remove(doador.cpf)
            self.lista_doador()
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Doador não cadastrado.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_doador, 2: self.alterar_cadastro, 3: self.lista_doador, 4:self.excluir_doador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_doador.tela_opcoes()]()


class ControladorAdotante():

    def __init__(self, controlador_sistema):
        #self.__adotantes = []
        self.__adotante_DAO = AdotanteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_adotante = TelaAdotante()

    '''
    @property
    def adotantes(self) -> list:
        return self.__adotantes
    '''

    @property
    def adotantes(self):
        return self.__adotante_DAO.get_all()

    def pega_adotante_por_cpf(self, cpf: int):
        #for adotante in self.__adotantes:
        for adotante in self.__adotante_DAO.get_all():
            print(adotante.cpf)
            if(adotante.cpf == cpf):
                return adotante
        return None

    def cadastrar_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        a = self.pega_adotante_por_cpf(dados_adotante["cpf"])
        if (a is None):
            if (self.mais_de_18_anos(dados_adotante["data_de_nascimento"], datetime.now())):
                adotante = Adotante(
                    dados_adotante["cpf"],
                    dados_adotante["nome"],
                    dados_adotante["data_de_nascimento"],
                    dados_adotante["endereco"],
                    dados_adotante["tipo_de_habitacao"],
                    dados_adotante["tamanho_da_habitacao"],
                    dados_adotante["numero_de_animais"]
                )
                #self.__adotantes.append(adotante)
                self.__adotante_DAO.add(adotante)
            else:
                self.__tela_adotante.mostra_mensagem("ATENÇÃO: Adotante menor de idade.")
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Adotante já cadastrado.")

    def mais_de_18_anos(self, data_inicial: datetime, data_final: datetime) -> bool:
        diferenca = data_final.year - data_inicial.year
        if (data_final.month, data_final.day) < (data_inicial.month, data_inicial.day):
            diferenca -= 1

        return diferenca >= 18

    def alterar_cadastro(self):
        self.lista_adotante()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if(adotante is not None):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"] #Não deve ser alterado!!!!!!
            adotante.nome = novos_dados_adotante["nome"]
            adotante.data_de_nascimento = novos_dados_adotante["data_de_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            adotante.tipo_de_habitacao = TipoHabitacao(novos_dados_adotante["tipo_de_habitacao"])
            adotante.tamanho_da_habitacao = TamanhoHabitacao(novos_dados_adotante["tamanho_da_habitacao"])
            adotante.numero_de_animais = novos_dados_adotante["numero_de_animais"]

            self.__adotante_DAO.update(adotante)
            self.lista_adotante()
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Adotante não cadastrado.")

    def lista_adotante(self):
        dados_adotante = []
        #for adotante in self.__adotantes:
        for adotante in self.__adotante_DAO.get_all():
            dados_adotante.append({
                "cpf" : adotante.cpf,
                "nome" : adotante.nome,
                "data_de_nascimento" : adotante.data_de_nascimento,
                "endereco" : adotante.endereco,
                "tipo_de_habitacao" : adotante.tipo_de_habitacao.name,
                "tamanho_da_habitacao" : adotante.tamanho_da_habitacao.name,
                "numero_de_animais" : adotante.numero_de_animais
            })
        self.__tela_adotante.mostra_adotante(dados_adotante)

    def excluir_adotante(self):
        self.lista_adotante()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if(adotante is not None):
            #self.__adotantes.remove(adotante)
            self.__adotante_DAO.remove(adotante.cpf)
            self.lista_adotante()
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Adotante não cadastrado.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_adotante, 2: self.alterar_cadastro, 3: self.lista_adotante, 4:self.excluir_adotante, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_adotante.tela_opcoes()]()            