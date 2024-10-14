class TelaVacina():

    def tela_opcoes(self):
        print("-------- VACINAÇÃO ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar vacinação")
        print("2 - Listar vacinações")
        print("3 - Excluir vacinação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_vacina(self):
        print("-------- DADOS VACINAÇÃO ----------")
        chip = input("Chip do animal: ")
        tipo = input("Tipo vacinal: ")
        data = input("Data: ")

        return {"chip" : chip, "tipo" : tipo, "data" : data}

    def mostra_vacinacao(self, dados_vacinacao):
        print("CODIGO DA VACINAÇÃO: ", dados_vacinacao["codigo"])
        print("NOME DO ANIMAL", dados_vacinacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("TIPO VACINAL" , dados_doacao["tipo_vacina"])
        print("\n")

    def seleciona_vacinacao(self):
        codigo = int(input("Código da vacinação que deseja selecionar:"))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)