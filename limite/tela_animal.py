from entidade.cachorro import TamanhoAnimal
from abstract.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from exception.dados_invalidos_exception import DadosInvalidosException

class TelaAnimal(TelaAbstrata):

    def __init__(self):
        self.__window = None
    
    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- ANIMAIS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir cachorro', "RD1", key='1')],
            [sg.Radio('Incluir gato', "RD1", key='2')],
            [sg.Radio('Alterar', "RD1", key='3')],
            [sg.Radio('Listar', "RD1", key='4')],
            [sg.Radio('Excluir', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao

        '''
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
        '''

    def pega_dados_cahorro(self):
        '''
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
        '''

        layout = [
            [sg.Text('-------- DADOS CACHORRO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Chip:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.Text('Raça:', size=(15, 1)), sg.InputText('', key='raca')],
            [sg.Frame(layout=[
                [sg.Radio('Pequeno', "TAMANHO", key='pequeno', default=True, size=(10,1)), sg.Radio('Médio', "TAMANHO", key='médio'), sg.Radio('Grande', "TAMANHO", key='grande')]],
                title='Tamanho do cachorro',
                title_color='red',
                relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        chip = int(values['chip'])
        raca = values['raca']
        if values['pequeno']:
            tamanho = TamanhoAnimal.pequeno
        elif values['médio']:
            tamanho = TamanhoAnimal.medio
        elif values['grande']:
            tamanho = TamanhoAnimal.grande
        else:
            tamanho = None

        self.__window.Close()

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca,
            "tamanho" : tamanho
        }

    def pega_dados_gato(self):
        layout = [
            [sg.Text('-------- DADOS GATO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Chip:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.Text('Raca:', size=(15, 1)), sg.InputText('', key='raca')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        chip = int(values['chip'])
        raca = values['raca']

        self.__window.Close()

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

        """

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca
        }

    def mostra_animal(self, dados_animal):
        '''
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
        '''
        string_todos_animais = ""
        for dado in dados_animal:
            string_todos_animais = string_todos_animais + "ESPÉCIE: " + dado["especie"] + '\n'
            string_todos_animais = string_todos_animais + "STATUS: " + dado["status"] + '\n'
            string_todos_animais = string_todos_animais + "NOME: " + dado["nome"] + '\n'
            string_todos_animais = string_todos_animais + "CHIP: " + str(dado["chip"]) + '\n'
            try:
                string_todos_animais = string_todos_animais + "TAMANHO: " + dado["tamanho"] + '\n'
            except Exception as e:
                pass
            string_todos_animais = string_todos_animais + "RAÇA: " + dado["raca"] + '\n\n'

        sg.Popup('-------- LISTA DE ANIMAIS ----------', string_todos_animais)

    def seleciona_animal(self):
        layout = [
            [sg.Text('-------- SELECIONAR ANIMAL ----------', font=("Helvica", 25))],
            [sg.Text('Digite o chip do animal que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Chip:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Seleciona animal').Layout(layout)

        button, values = self.__window.Read()
        chip = values['chip']
        self.__window.Close()
        return chip
        '''
        chip = int(input("Código do chip do animal que deseja selecionar: "))
        return chip
        '''

    def mostra_mensagem(self, msg):
        sg.popup("", msg)