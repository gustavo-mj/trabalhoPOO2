from datetime import date
from datetime import datetime
from abstract.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaDoacao(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):

        '''
        print("-------- DOAÇÕES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar doação")
        print("2 - Alterar cadastro")
        print("3 - Listar doações")
        print("4 - Listar doações num período")
        print("5 - Excluir doação")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    raise ValueError
                break
            except ValueError as e:
                print("Entrada inválida. Tente novamente.")
        '''

        layout = [
            [sg.Text('-------- DOAÇÕES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Alterar', "RD1", key='2')],
            [sg.Radio('Listar doações', "RD1", key='3')],
            [sg.Radio('Listar doações num período', "RD1", key='4')],
            [sg.Radio('Excluir', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
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

    def pega_dados_doacao(self):
        '''
        print("-------- DADOS DA DOAÇÃO --------")
        while True:
            try:
                cpf = int(input("CPF do doador: "))
                chip = int(input("Chip do animal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                motivo = input("Motivo: ")
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")
        '''
        layout = [
            [sg.Text('-------- DADOS DOAÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('CHIP:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.CalendarButton('Data da doação', target='data', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='data')],
            [sg.Text('MOTIVO:', size=(15, 1)), sg.InputText('', key='motivo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        chip = int(values['chip'])
        cpf = int(values['cpf'])
        motivo = values['motivo']
        data = datetime.strptime(values['data'], '%d/%m/%Y').date()
        self.__window.Close()

        return {"cpf" : cpf, "chip" : chip, "data" : data, "motivo" : motivo}

    def mostra_doacao(self, dados_doacao):
        string_todos_doacoes = ""
        for dado in dados_doacao:
            string_todos_doacoes = string_todos_doacoes + "CÓDIGO: " + str(dado['codigo']) + '\n'
            string_todos_doacoes = string_todos_doacoes + "NOME DO ANIMAL: " + dado['nome_animal'] + '\n'
            string_todos_doacoes = string_todos_doacoes + "CHIP DO ANIMAL: " + str(dado['chip_animal']) + '\n'
            string_todos_doacoes = string_todos_doacoes + "NOME DO DOADOR: " + dado['nome_doador'] + '\n'
            string_todos_doacoes = string_todos_doacoes + "CPF DO DOADOR: " + str(dado['cpf_doador']) + '\n'
            string_todos_doacoes = string_todos_doacoes + "DATA: " + dado['data'].strftime('%d/%m/%Y') + '\n\n'
        sg.Popup('-------- LISTA DE DOAÇÕES ----------', string_todos_doacoes)
        '''
        print("CODIGO DA DOACAO: ", dados_doacao["codigo"])
        print("NOME DO ANIMAL" , dados_doacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("NOME DO DOADOR" , dados_doacao["nome_doador"])
        print("CPF DO DOADOR" , dados_doacao["cpf_doador"])
        print("DATA", dados_doacao["data"])
        print("\n")
        '''

    def seleciona_doacao(self):
        '''
        codigo = int(input("Código da doação que deseja selecionar: "))
        return codigo
        '''
        layout = [
            [sg.Text('-------- SELECIONAR DOAÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da doação que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Seleciona doação').Layout(layout)
        button, values = self.__window.Read()
        codigo = int(values['codigo'])
        self.__window.Close()
        return codigo

    def seleciona_periodo(self):
        '''
        while True:
            try:
                inicio = datetime.strptime(input("Início: "), "%d/%m/%Y").date()
                fim = datetime.strptime(input("Fim: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")
        '''
        layout = [
            [sg.Text('-------- SELEÇÃO DE PERÍODO ----------', font=("Helvica", 25))],
            [sg.CalendarButton('INÍCIO', target='inicio', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='inicio')],
            [sg.CalendarButton('FIM', target='fim', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='fim')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        inicio = datetime.strptime(values['inicio'], '%d/%m/%Y').date()
        fim = datetime.strptime(values['fim'], '%d/%m/%Y').date()
        self.__window.Close()
                
        return {"inicio" : inicio, "fim" : fim}

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

class TelaAdocao(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        '''
        print("-------- ADOÇÕES --------")
        print("Escolha a opção:")
        print("1 - Mostrar disponíveis")
        print("2 - Cadastrar adoção")
        print("3 - Alterar cadastro")
        print("4 - Listar adoções")
        print("5 - Listar adoções num período")
        print("6 - Excluir adoção")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1, 2, 3, 4, 5, 6]:
                    raise ValueError
                break
            except ValueError as e:
                print("Entrada inválida. Tente novamente.")

        return opcao
        '''
        layout = [
            [sg.Text('-------- ADOÇÕES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar disponíveis', "RD1", key='1')],
            [sg.Radio('Cadastrar', "RD1", key='2')],
            [sg.Radio('Alterar', "RD1", key='3')],
            [sg.Radio('Listar adoções', "RD1", key='4')],
            [sg.Radio('Listar adoções num período', "RD1", key='5')],
            [sg.Radio('Excluir', "RD1", key='6')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
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
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()

        return opcao

    def pega_dados_adocao(self):
        '''
        print("-------- DADOS DA ADOÇÃO --------")
        while True:
            try:
                cpf = int(input("CPF do Adotante: "))
                chip = int(input("Chip do animal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {"cpf" : cpf, "chip" : chip, "data" : data}
        '''
        layout = [
            [sg.Text('-------- DADOS ADOÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('CHIP:', size=(15, 1)), sg.InputText('', key='chip')],
            [sg.CalendarButton('Data da adoção', target='data', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        chip = int(values['chip'])
        cpf = int(values['cpf'])
        data = datetime.strptime(values['data'], '%d/%m/%Y').date()
        self.__window.Close()

        return {"cpf" : cpf, "chip" : chip, "data" : data}

    def mostra_adocao(self, dados_adocao):
        '''
        print("CODIGO DA DOACAO: ", dados_adocao["codigo"])
        print("NOME DO ANIMAL" , dados_adocao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_adocao["chip_animal"])
        print("NOME DO ADOTANTE" , dados_adocao["nome_adotante"])
        print("CPF DO ADOTANTE" , dados_adocao["cpf_adotante"])
        print("DATA", dados_adocao["data"])
        print("\n")
        '''
        string_todos_adocoes = ""
        for dado in dados_adocao:
            string_todos_adocoes = string_todos_adocoes + "CÓDIGO: " + str(dado['codigo']) + '\n'
            string_todos_adocoes = string_todos_adocoes + "NOME DO ANIMAL: " + dado['nome_animal'] + '\n'
            string_todos_adocoes = string_todos_adocoes + "CHIP DO ANIMAL: " + str(dado['chip_animal']) + '\n'
            string_todos_adocoes = string_todos_adocoes + "NOME DO ADOTANTE: " + dado['nome_adotante'] + '\n'
            string_todos_adocoes = string_todos_adocoes + "CPF DO ADOTANTE: " + str(dado['cpf_adotante']) + '\n'
            string_todos_adocoes = string_todos_adocoes + "DATA: " + dado['data'].strftime('%d/%m/%Y') + '\n\n'
        sg.Popup('-------- LISTA DE ADOÇÕES ----------', string_todos_adocoes)

    def seleciona_adocao(self):
        '''
        codigo = int(input("Código da adoção que deseja selecionar: "))
        return codigo
        '''
        layout = [
            [sg.Text('-------- SELECIONAR ADOÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da adoção que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Seleciona adoção').Layout(layout)
        button, values = self.__window.Read()
        codigo = int(values['codigo'])
        self.__window.Close()
        return codigo
    
    def seleciona_periodo(self):
        '''
        while True:
            try:
                inicio = datetime.strptime(input("Início: "), "%d/%m/%Y").date()
                fim = datetime.strptime(input("Fim: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")
        return {"inicio" : inicio, "fim" : fim}
        '''
        layout = [
            [sg.Text('-------- SELEÇÃO DE PERÍODO ----------', font=("Helvica", 25))],
            [sg.CalendarButton('INÍCIO', target='inicio', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='inicio')],
            [sg.CalendarButton('FIM', target='fim', format='%d/%m/%Y', close_when_date_chosen=True), sg.Input(key='fim')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        inicio = datetime.strptime(values['inicio'], '%d/%m/%Y').date()
        fim = datetime.strptime(values['fim'], '%d/%m/%Y').date()
        self.__window.Close()
                
        return {"inicio" : inicio, "fim" : fim}

    def mostra_mensagem(self, msg):
        sg.popup("", msg)