from datetime import datetime
from entidade.adotante import *
from abstract.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaDoador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- DOADORES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir', "RD1", key='1')],
            [sg.Radio('Alterar', "RD1", key='2')],
            [sg.Radio('Listar', "RD1", key='3')],
            [sg.Radio('Excluir', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema ONG de pets').Layout(layout)
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
        self.__window.Close()
        return opcao

    def pega_dados_doador(self):
        layout = [
        [sg.Text('-------- DADOS DOADOR ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.CalendarButton('Data de Nascimento', target='data', format='%d/%m/%Y', close_when_date_chosen=True),
        sg.Input(key='data')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        data_de_nascimento = datetime.strptime(values['data'], '%d/%m/%Y').date()
        cpf = int(values['cpf'])
        endereco = values['endereco']
        self.__window.Close()
        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : data_de_nascimento,
            "endereco" : endereco}

    def mostra_doador(self, dados_doador):
        string_todos_doadores = ""
        for dado in dados_doador:
            string_todos_doadores = string_todos_doadores + "NOME DO DOADOR: " + dado["nome"] + '\n'
            string_todos_doadores = string_todos_doadores + "CPF DO DOADOR: " + str(dado["cpf"]) + '\n'
            string_todos_doadores = string_todos_doadores + "ENDEREÇO: " + dado["endereco"] + '\n'
            string_todos_doadores = string_todos_doadores + "DATA: " + dado["data_de_nascimento"].strftime('%d/%m/%Y') + '\n\n'
        sg.Popup('-------- LISTA DE DOADORES ----------', string_todos_doadores)

    def seleciona_doador(self):
        layout = [
        [sg.Text('-------- SELECIONAR DOADOR ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do doador que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona doador').Layout(layout)
        button, values = self.__window.Read()
        cpf = int(values['cpf'])
        self.__window.Close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

class TelaAdotante(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- ADOTANTES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir', "RD1", key='1')],
            [sg.Radio('Alterar', "RD1", key='2')],
            [sg.Radio('Listar', "RD1", key='3')],
            [sg.Radio('Excluir', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema ONG de pets').Layout(layout)
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
        self.__window.Close()
        return opcao

    def pega_dados_adotante(self):
        layout = [
        [sg.Text('-------- DADOS DOADOR ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Input(key='data'),
        sg.CalendarButton('Data de Nascimento', target='data', format='%d/%m/%Y', close_when_date_chosen=True)],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
        [sg.Frame(layout=[
            [sg.Radio('Casa ', "TIPO", key='casa', default=True, size=(10,1)), sg.Radio('Apartamento', "TIPO", key='apartamento')]],
            title='Tipo de Habitação',
            title_color='red',
            relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        [sg.Frame(layout=[
            [sg.Radio('Pequena', "TAMANHO", key='pequena', default=True, size=(10,1)), sg.Radio('Média', "TAMANHO", key='média'), sg.Radio('Grande', "TAMANHO", key='grande')]],
            title='Tamanho da Habitação',
            title_color='red',
            relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        [sg.Text('Número de animais:', size=(15, 1)), sg.InputText('', key='numero_de_animais')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        data_de_nascimento = datetime.strptime(values['data'], '%d/%m/%Y').date()
        cpf = int(values['cpf'])
        endereco = values['endereco']

        if values['casa']:
            tipo_de_habitacao = TipoHabitacao.casa
        elif values['apartamento']:
            tipo_de_habitacao = TipoHabitacao.apartamento
        else:
            tipo_de_habitacao = None

        if values['pequena']:
            tamanho_da_habitacao = TamanhoHabitacao.pequeno
        elif values['média']:
            tamanho_da_habitacao = TamanhoHabitacao.medio
        elif values['grande']:
            tamanho_da_habitacao = TamanhoHabitacao.grande
        else:
            tamanho_da_habitacao = None

        numero_de_animais = int(values['numero_de_animais'])

        self.__window.Close()

        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : data_de_nascimento,
            "endereco" : endereco,
            "tipo_de_habitacao" : tipo_de_habitacao,
            "tamanho_da_habitacao" : tamanho_da_habitacao,
            "numero_de_animais" : numero_de_animais}

    def mostra_adotante(self, dados_adotante):
        string_todos_adotantes = ""
        for dado in dados_adotante:
            string_todos_adotantes = string_todos_adotantes + "NOME: " + dado['nome'] + '\n'
            string_todos_adotantes = string_todos_adotantes + "CPF: " + str(dado['cpf']) + '\n'
            string_todos_adotantes = string_todos_adotantes + "NASCIMENTO: " + dado['data_de_nascimento'].strftime('%d/%m/%Y') + '\n'
            string_todos_adotantes = string_todos_adotantes + "ENDEREÇO: " + dado['endereco'] + '\n'
            string_todos_adotantes = string_todos_adotantes + "TIPO DE HABITAÇÃO: " + dado['tipo_de_habitacao'] + '\n'
            string_todos_adotantes = string_todos_adotantes + "TAMANHO DA HABITACÃO: " +  dado['tamanho_da_habitacao'] + '\n'
            string_todos_adotantes = string_todos_adotantes + "NÚMERO DE ANIMAIS: " + str(dado['numero_de_animais']) + '\n'
        sg.Popup('-------- LISTA DE ADOTANTES ----------', string_todos_adotantes)

    def seleciona_adotante(self):
        layout = [
        [sg.Text('-------- SELECIONAR ADOTANTE ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do adotante que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona adotante').Layout(layout)
        button, values = self.__window.Read()
        cpf = int(values['cpf'])
        self.__window.Close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)