from limite.tela_vacina import TelaVacina
from entidade.vacina import *
from random import randint
from entidade.animal import *

class ControladorVacina():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacinacao = TelaVacina()

    def cadastrar_vacinacao(self):
        if not self.__controlador_sistema.controlador_animais.animais:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Não há animais cadastrados.")
        else:
            self.__controlador_sistema.controlador_animais.lista_animais()
            dados_vacinacao = self.__tela_vacinacao.pega_dados_vacina()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(dados_vacinacao["chip"])
            if (animal is not None):
                vacina = Vacina(
                    Tipo(dados_vacinacao["tipo_vacinal"]),
                    None
                )
                vacina.data = dados_vacinacao["data"]
                animal.adicionar_vacina(vacina)
                self.atualiza_status(animal)
                self.__controlador_sistema.controlador_animais.update_remoto(animal) #atualiza animal
            else:
                self.__tela_vacinacao.mostra_mensagem("Dados inválidos.")
        

    def atualiza_status(self, animal: Animal):
        testagem = []
        for vacina in animal.vacinas:
            testagem.append(vacina.tipo)
        if all(tipo in testagem for tipo in [Tipo.hepatite, Tipo.raiva, Tipo.leptospirose]):
            animal.status = Status.disponivel
        else:
            animal.status = Status.nao_disponivel

    def alterar_cadastro(self):
        if not self.__controlador_sistema.controlador_animais.animais:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Não há animais cadastrados.")
        else:
            self.__controlador_sistema.controlador_animais.lista_animais()
            chip = self.__tela_vacinacao.seleciona_animal()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(chip)
            self.lista_vacinacoes(animal)
            indice = self.__tela_vacinacao.seleciona_vacinacao()
            vacina = animal.vacinas[indice-1]

            if(vacina is not None):
                novos_dados_vacina = self.__tela_vacinacao.pega_novos_dados_vacina()
                vacina.data = novos_dados_vacina["data"]
                vacina.tipo = Tipo(novos_dados_vacina["tipo_vacinal"])
                self.__controlador_sistema.controlador_animais.update_remoto(animal) #atualiza animal
                self.lista_vacinacoes(animal)
            else:
                self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Vacinação não existe.")

    def lista_vacinacoes(self, animal: Animal):
        dados_vacinacao = []
        indice = 0
        for v in animal.vacinas:
            indice += 1
            dados_vacinacao.append({
                "indice" : indice,
                "tipo_vacinal" : v.tipo.name,
                "data" : v.data
            })
        self.__tela_vacinacao.mostra_vacinacao(dados_vacinacao)

    def listagem(self):
        if not self.__controlador_sistema.controlador_animais.animais:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Não há animais cadastrados.")
        else:
            self.__controlador_sistema.controlador_animais.lista_animais()
            chip = self.__tela_vacinacao.seleciona_animal()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(chip)
            self.lista_vacinacoes(animal)

    def excluir_vacinacao(self):
        if not self.__controlador_sistema.controlador_animais.animais:
            self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: Não há animais cadastrados.")
        else:
            self.__controlador_sistema.controlador_animais.lista_animais()
            chip = self.__tela_vacinacao.seleciona_animal()
            animal = self.__controlador_sistema.controlador_animais.pega_animal_por_chip(chip)
            self.lista_vacinacoes(animal)
            indice = self.__tela_vacinacao.seleciona_vacinacao()
            vacina = animal.vacinas[indice-1]
            if (vacina is not None):
                animal.excluir_vacina(vacina)
                self.atualiza_status(animal)
                self.__controlador_sistema.controlador_animais.update_remoto(animal) #atualiza animal
                self.lista_vacinacoes(animal)
            else:
                self.__tela_vacinacao.mostra_mensagem("ATENÇÃO: esta vacinação não existe.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_vacinacao, 2: self.alterar_cadastro, 3: self.listagem, 4: self.excluir_vacinacao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_vacinacao.tela_opcoes()]()
