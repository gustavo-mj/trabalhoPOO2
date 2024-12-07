class TelaSistema:

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