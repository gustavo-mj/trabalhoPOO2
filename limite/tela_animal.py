from entidade.cachorro import TamanhoAnimal
from abstract.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from exception.dados_invalidos_exception import DadosInvalidosException

class TelaAnimal(TelaAbstrata):

    def __init__(self):
        pass
    
    def tela_opcoes(self):
        print("-------- ANIMAIS --------")
        print("Escolha a opção:")
        print("1 - Cadastrar cachorro")
        print("2 - Cadastrar gato")
        print("3 - Alterar cadastro")
        print("4 - Listar cadastrados")
        print("5 - Excluir cadastro")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise ValueError
                break
            except ValueError as e:
                print("Entrada inválida. Tente novamente.")

        return opcao

    def pega_dados_cahorro(self):
        print("-------- DADOS DO CACHORRO --------")
        while True:
            try:
                chip = int(input("Chip: "))
                nome = input("Nome: ")
                raca = input("Raça: ")
                tamanho = TamanhoAnimal(int(input("Tamanho(1 - pequeno; 2 - médio; 3 - grande): ")))
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca,
            "tamanho" : tamanho
        }

    def pega_dados_gato(self):
        layout = [
        [sg.Text('Insira chip, nome e raça:')],
        [sg.Text('Chip', size=(15, 1)), sg.InputText('chip',
        key='chip')],
        [sg.Text('Nome', size=(15, 1)), sg.InputText('nome',
        key='nome')],
        [sg.Text('Raça', size=(15, 1)), sg.InputText('raca',
        key='raca')],
        [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Dados do Gato').Layout(layout)
        while True:
            button, values = window.Read()
            try:
                values["chip"] = int(values["chip"])
                break
            except ValueError as e:
                print("Dados inválidos.")
        window.close()
        return values

        """"
        print("-------- DADOS DO GATO --------")
        while True:
            try:
                chip = int(input("Chip: "))
                nome = input("Nome: ")
                raca = input("Raça: ")
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca
        }
        """

    def mostra_animal(self, dados_animal):
        print("ESPÉCIE: ", dados_animal["especie"])
        print("STATUS", dados_animal["status"])
        print("CHIP: ", dados_animal["chip"])
        print("NOME: ", dados_animal["nome"])
        print("RAÇA: ", dados_animal["raca"])
        try:
            print("TAMANHO: ", dados_animal["tamanho"])
        except Exception as e:
            pass
        print("\n")

    def seleciona_animal(self):
        chip = int(input("Código do chip do animal que deseja selecionar: "))
        return chip

    def mostra_mensagem(self, msg):
        print(msg)