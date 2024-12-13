from datetime import datetime
from abstract.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaVacina(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- VACINAÇÕES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Alterar', "RD1", key='2')],
            [sg.Radio('Listar', "RD1", key='3')],
            [sg.Radio('Excluir', "RD1", key='4')],
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
            print('cancelou!')
        self.__window.Close()
        return opcao
        '''
        print("-------- VACINAÇÃO ----------")
        print("Escolha a opção:")
        print("1 - Cadastrar vacinação")
        print("2 - Alterar cadastro")
        print("3 - Listar vacinações")
        print("4 - Excluir vacinação")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3, 4]:
                    raise ValueError
                break
            except ValueError as e:
                print("Entrada inválida. Tente novamente.")

        return opcao
        '''

    def pega_dados_vacina(self):
        layout = [
            [sg.Text('-------- DADOS VACINAÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Chip:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.Frame(layout=[
                [sg.Radio('Raiva', "TIPO", key='raiva', default=True, size=(10,1)), sg.Radio('Leptospirose', "TIPO", key='leptospirose'), sg.Radio('Hepatite', "TIPO", key='hepatite')]],
                title='Tipo vacinal',
                title_color='red',
                relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags')],
            [sg.CalendarButton('Data de vacinação:', target='data', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        chip = int(values['chip'])
        if values['raiva']:
            tipo_vacinal = 1
        elif values['leptospirose']:
            tipo_vacinal = 2
        elif values['hepatite']:
            tipo_vacinal = 3
        else:
            tipo_vacinal = None
        data = datetime.strptime(values['data'], '%d/%m/%Y').date()
        self.__window.Close()

        '''
        print("-------- DADOS VACINAÇÃO ----------")
        while True:
            try:
                chip = int(input("Chip do animal: "))
                tipo = int(input("Tipo vacinal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")
        '''

        return {"chip" : chip, "tipo_vacinal" : tipo_vacinal, "data" : data}

    def pega_novos_dados_vacina(self):
        layout = [
            [sg.Text('-------- DADOS VACINAÇÃO ----------', font=("Helvica", 25))],
            [sg.Frame(layout=[
                [sg.Radio('Raiva', "TIPO", key='raiva', default=True, size=(10,1)), sg.Radio('Leptospirose', "TIPO", key='leptospirose'), sg.Radio('Hepatite', "TIPO", key='hepatite')]],
                title='Tipo vacinal',
                title_color='red',
                relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags')],
            [sg.CalendarButton('Data de vacinação:', target='data', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        if values['raiva']:
            tipo_vacinal = 1
        elif values['leptospirose']:
            tipo_vacinal = 2
        elif values['hepatite']:
            tipo_vacinal = 3
        else:
            tipo_vacinal = None
        data = datetime.strptime(values['data'], '%d/%m/%Y').date()
        self.__window.Close()
        '''
        print("-------- DADOS DE ALTERAÇÃO DA VACINAÇÃO ----------")
        while True:
            try:
                tipo = int(input("Tipo vacinal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")
        '''
        return {"tipo_vacinal" : tipo_vacinal, "data" : data}

    def mostra_vacinacao(self, dados_vacinacao):
        string_todas_vacinacoes = ""
        for dado in dados_vacinacao:
            string_todas_vacinacoes = string_todas_vacinacoes + "ÍNDICE: " + str(dado["indice"]) + '\n'
            string_todas_vacinacoes = string_todas_vacinacoes + "TIPO VACINAL: " + dado["tipo_vacinal"] + '\n'
            string_todas_vacinacoes = string_todas_vacinacoes + "DATA: " + dado["data"].strftime('%d/%m/%Y') + '\n\n'
        sg.popup('-------- LISTA DE VACINAÇÕES ----------', string_todas_vacinacoes)
        '''
        print("ÍNDICE", dados_vacinacao["indice"])
        print("TIPO VACINAL" , dados_vacinacao["tipo_vacinal"])
        print("DATA: ", dados_vacinacao["data"])
        print("\n")
        '''

    def seleciona_vacinacao(self):
        layout = [
        [sg.Text('-------- SELECIONAR VACINAÇÃO ----------', font=("Helvica", 25))],
        [sg.Text('Digite o índice da vacinação que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('Índice:', size=(15, 1)), sg.InputText('', key='indice')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar vacinação').Layout(layout)
        button, values = self.__window.Read()
        indice = int(values['indice'])
        self.__window.Close()
        return indice
        '''
        codigo = int(input("Índice da vacina que deseja selecionar:"))
        return codigo
        '''

    def seleciona_animal(self):
        layout = [
            [sg.Text('-------- SELECIONAR ANIMAL ----------', font=("Helvica", 25))],
            [sg.Text('Digite o chip do animal que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Chip:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Selecionar animal').Layout(layout)

        button, values = self.__window.Read()
        chip = int(values['chip'])
        self.__window.Close()
        return chip
        ''''
        chip = int(input("Digite o chip do animal que deseja selecionar:"))
        return chip
        '''

    def mostra_mensagem(self, msg):
        sg.popup("", msg)