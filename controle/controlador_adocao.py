from limite.tela_adocao import TelaAdocao
from entidade.adocao import Adocao
from random import randint
from dateutil.relativedelta import relativedelta


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
        self.__controlador_sistema.controlador_animais.lista_animal()
        self.__controlador_sistema.controlador_pessoas.lista_pessoa()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_adocao["chip"])
        pessoa = self.__controlador_sistema.controlador_pessoas.pega_pessoa_por_cpf(dados_adocao["cpf"])
        #adição minha
        data = dados_adocao["data"]
        diferenca = relativedelta(data, pessoa.dataNasc)
        vacinasTomadas = self.__controlador_sistema.controlador_vacinacoes.lista_vacinas_por_animal(dados_adocao["chip"])
        #acaba aqui

        if (animal is not None and pessoa is not None) and (pessoa.ehDoador == False) and (diferenca.years >= 18):
            if (animal.tamanho != 3) or (pessoa.tipoHab != 2) or (adotante.tamanhoHab != 1):
                if all(vacina in [1, 2, 3] for vacina in vacinasTomadas):
                    adocao = Adocao(randint(0, 100), data, animal, pessoa, True)
                    self.__adocoes.append(adocao)
            else:
                self.__tela_adocao.mostra_mensagem("Tamanho do animal e habitação incompatíveis.")
        else:
            self.__tela_adocao.mostra_mensagem("Dados inválidos ou o adotante é menor de idade.")

    def lista_adocao(self):
        dados_listagem = self.__tela_doacao.pega_dados_listagem()
        if not dados_listagem:
            for a in self.__adocoes:
                self.__tela_adocao.mostra_adocao({
                    "codigo" : a.codigo,
                    "nome_animal" : a.animal.nome,
                    "chip_animal" : a.animal.chip,
                    "nome_adotante" : a.pessoa.nome,
                    "cpf_adotante" : a.pessoa.cpf
                })
        else:
            for a in self.__adocoes:
                if (d.data > dados_listagem["início"]) and (d.data < dados_listagem["fim"]):
                    self.__tela_adocao.mostra_adocao({
                        "codigo" : a.codigo,
                        "nome_animal" : a.animal.nome,
                        "chip_animal" : a.animal.chip,
                        "nome_adotante" : a.pessoa.nome,
                        "cpf_adotante" : a.pessoa.cpf
                    })

    def excluir_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(int(codigo_adocao))

        if(adocao is not None):
            self.__adocoes.remove(adocao)
            self.lista_adocao()
        else:
            self.__tela_adocao.mostra_mensagem("ATENÇÃO: esta adoção não existe.")

    def listar_disponveis_para_adocao(self):
        disponiveis = []
        for animal in self.__controlador_sistema.controlador_animais.animais:
            for adotado in self.__adocoes:
                if animal == adotado:
                    break
                else:
                    disponiveis.append(animal)
        return {"nome_animal" : animal.nome, "chip_animal" : animal.chip, "tamanho_animal" : animal.tamanho}


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_adocao, 2: self.lista_adocao, 3: self.excluir_adocao, 4: self.listar_disponveis_para_adocao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()