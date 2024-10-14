from limite.tela_pessoa import TelaPessoa
from entidade.pessoa import *


class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__pessoas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()

    def pega_pessoa_por_cpf(self, cpf: int):
        for pessoa in self.__pessoas:
            if(pessoa.cpf == cpf):
                return pessoa
        return None

    def cadastrar_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        p = self.pega_pessoa_por_cpf(dados_pessoa["CPF"])
        if p is None:
            pessoa = Pessoa(
                dados_pessoa["CPF"],
                dados_pessoa["nome"],
                dados_pessoa["data de nascimento"],
                dados_pessoa["endereço"],
                dados_pessoa["tipo de habitação"],
                dados_pessoa["tamanho da habitação"],
                dados_pessoa["número de animais"]
            )
            self.__pessoas.append(pessoa)
        else:
            self.__tela_livro.mostra_mensagem("ATENÇÃO: Pessoa já cadastrada.")

    def alterar_cadastro(self):
        self.lista_pessoa()
        cpf_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf_pessoa)

        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.cpf = novos_dados_pessoa["CPF"]
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.dataNasc = novos_dados_pessoa["data de nascimento"]
            pessoa.endereco = novos_dados_pessoa["endereço"]
            pessoa.tipoHab = novos_dados_pessoa["tipo de habitação"]
            pessoa.tamanhoHab = novos_dados_pessoa["tamanho da habitação"]
            pessoa.numeroAnimais = novos_dados_pessoa["número de animais"]
            self.lista_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")

    def lista_pessoa(self):
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoa({
                "CPF" : pessoa.cpf,
                "nome" : pessoa.nome,
                "data de nascimento" : pessoa.dataNasc,
                "endereço" : pessoa.endereco,
                "tipo de habitação" : pessoa.tipoHab,
                "tamanho da habitação" : pessoa.tamanhoHab,
                "númmero de animais" : pessoa.numeroAnimais
            })

    def excluir_pessoa(self):
        self.lista_pessoa()
        cpf_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf_pessoa)

        if(pessoa is not None):
            self.__pessoas.remove(pessoa)
            self.lista_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não cadastrada.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_pessoa, 2: self.alterar_cadastro, 3: self.lista_pessoa, 4:self.excluir_pessoa, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
            