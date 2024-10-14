from limite.tela_vacina import TelaVacina
from entidade.vacina import *
from random import randint

class ControladorVacina():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vacinacoes = []
        self.__tela_vacinacao = TelaVacina()

    def pega_vacina_por_codigo(self, codigo: int):
        for vacina in self.__vacinacoes:
            if(vacina.codigo == codigo):
                return vacina
        return None

    def cadastrar_vacinacao(self):
        self.__controlador_sistema.controlador_animais.lista_animal()
        dados_doacao = self.__tela_vacinacao.pega_dados_vacina()

        animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_doacao["chip"])
        
        if (animal is not None):
            vacina = Vacina(randint(0, 100), animal, Tipo(dados_doacao["tipo_vacinal"]), dados_doacao['data'])
            self.__vacinacoes.append(vacina)
        else:
            self.__tela_vacinacao.mostra_mensagem("Dados inválidos.")

    def alterar_cadastro(self):
        self.lista_vacinacoes()
        codigo_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacina = self.pega_vacina_por_codigo(codigo_vacinacao)

        if(vacina is not None):
            novos_dados_vacina = self.__tela_pessoa.pega_dados_vacina()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(novos_dados_vacina["chip"])
            vacina.animal = animal
            vacina.data = novos_dados_vacina["data"]
            vacina.tipo = Tipo(novos_dados_vacina["tipo_vacinal"])
            self.lista_vacinacoes()
        else:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Vacinação não existe.")

    def lista_vacinacoes(self):
        for v in self.__vacinacoes:
            self.__tela_vacinacao.mostra_vacinacao({
                "codigo" : v.codigo,
                "nome_animal" : v.animal.nome,
                "chip_animal" : v.animal.chip,
                "tipo_vacinal" : v.tipo
            })

    def lista_vacinas_por_animal(self, chip: int):
        vacinasTomadas = []
        for vacina in self.__vacinacoes:
            if(vacina.animal.chip == chip):
                vacinasTomadas.append(vacina.tipo)
        return vacinasTomadas

    def excluir_vacinacao(self):
        self.lista_vacinacoes()
        codigo_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.pega_vacina_por_codigo(int(codigo_vacinacao))

        if (vacinacao is not None):
            self.__vacinacoes.remove(vacinacao)
            self.lista_vacinacoes()
        else:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: esta vacinação não existe.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_vacinacao, 2: self.alterar_cadastro, 3: self.lista_vacinacoes, 4: self.excluir_vacinacao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_vacinacao.tela_opcoes()]()
