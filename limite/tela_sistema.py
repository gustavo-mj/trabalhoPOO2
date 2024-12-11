import PySimpleGUI as sg


class TelaSistema:

    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        layout = [
            [sg.Text('Bem vindo ao sistema da ONG de adoção!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Animais',"RD1", key='1')],
            [sg.Radio('Doadores',"RD1", key='2')],
            [sg.Radio('Adotantes',"RD1", key='3')],
            [sg.Radio('Doações',"RD1", key='4')],
            [sg.Radio('Adoções',"RD1", key='5')],
            [sg.Radio('Vacinações',"RD1", key='6')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema da ONG de pets').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
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
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao
    '''
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError #será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def tela_opcoes(self):
        print("-------- SisONGdePets ---------")
        print("Escolha sua opcao")
        print("1 - Animais")
        print("2 - Doadores")
        print("3 - Adotantes")
        print("4 - Doações")
        print("5 - Adoções")
        print("6 - Vacinações")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5,6])
        return opcao

        '''