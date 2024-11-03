from limite.tela_pessoas import *
from entidade.doador import *
from entidade.adotante import *


class ControladorDoador():

    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_doador = TelaDoador()

    def pega_doador_por_cpf(self, cpf: int):
        for doador in self.__doadores:
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
            self.__doadores.append(doador)
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Pessoa já cadastrada.")

    def alterar_cadastro(self):
        self.lista_doador()
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        if(doador is not None):
            novos_dados_doador = self.__tela_doador.pega_dados_doador()
            doador.cpf = novos_dados_doador["cpf"]
            doador.nome = novos_dados_doador["nome"]
            doador.dataNasc = novos_dados_doador["data_de_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
            self.lista_doador()
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")

    def lista_doador(self):
        for doador in self.__doadores:
            self.__tela_doador.mostra_doador({
                "cpf" : doador.cpf,
                "nome" : doador.nome,
                "data_de_nascimento" : doador.dataNasc,
                "endereco" : doador.endereco
            })

    def excluir_doador(self):
        self.lista_doador()
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        if(doador is not None):
            self.__doadores.remove(doador)
            self.lista_doador()
        else:
            self.__tela_doador.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_doador, 2: self.alterar_cadastro, 3: self.lista_doador, 4:self.excluir_doador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()


class ControladorAdotante():

    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_adotante = TelaAdotante()

    def pega_adotante_por_cpf(self, cpf: int):
        for adotante in self.__adotantes:
            if(adotante.cpf == cpf):
                return adotante
        return None

    def cadastrar_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        a = self.pega_adotante_por_cpf(dados_adotante["cpf"])
        if a is None:
            adotante = Adotante(
                dados_adotante["cpf"],
                dados_adotante["nome"],
                dados_adotante["data_de_nascimento"],
                dados_adotante["endereco"],
                TipoHab(dados_adotante["tipo_de_habitacao"]),
                TamanhoHab(dados_adotante["tamanho_da_habitacao"]),
                dados_adotante["numero_de_animais"]
            )
            self.__adotantes.append(adotante)
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Pessoa já cadastrada.")

    def alterar_cadastro(self):
        self.lista_adotante()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if(adotante is not None):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"]
            adotante.dataNasc = novos_dados_adotante["data_de_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            adotante.tipoHab = TipoHab(novos_dados_adotante["tipo_de_habitacao"])
            adotante.tamanhoHab = TamanhoHab(novos_dados_adotante["tamanho_da_habitacao"])
            adotante.numeroAnimais = novos_dados_adotante["numero_de_animais"]
            self.lista_adotante()
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")

    def lista_adotante(self):
        for adotante in self.__adotantes:
            self.__tela_adotante.mostra_adotante({
                "cpf" : adotante.cpf,
                "nome" : adotante.nome,
                "data_de_nascimento" : adotante.dataNasc,
                "endereco" : adotante.endereco,
                "tipo_de_habitacao" : adotante.tipoHab.name,
                "tamanho_da_habitacao" : adotante.tamanhoHab.name,
                "numero_de_animais" : adotante.numeroAnimais
            })

    def excluir_adotante(self):
        self.lista_adotante()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if(adotante is not None):
            self.__adotantes.remove(adotante)
            self.lista_adotante()
        else:
            self.__tela_adotante.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_adotante, 2: self.alterar_cadastro, 3: self.lista_adotante, 4:self.excluir_adotante, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()            