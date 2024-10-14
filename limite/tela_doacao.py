class TelaDoacao:

    def tela_opcoes(self):
        print("-------- DOAÇÕES ----------")
        print("Escolha a opcao")
        print("1 - Fazer doação")
        print("2 - Listar doações")
        print("3 - Excluir doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DOAÇÃO ----------")
        cpf = int(input("CPF do doador: "))
        chip = int(input("Chip do animal: "))
        data = input("Data: ")
        motivo = input("Motivo: ")

        return {"cpf" : cpf, "chip" : chip, "data" : data, "motivo" : motivo}

    def mostra_doacao(self, dados_doacao):
        print("CODIGO DA DOACAO: ", dados_doacao["codigo"])
        print("NOME DO ANIMAL" , dados_doacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("NOME DO DOADOR" , dados_doacao["nome_doador"])
        print("CPF DO DOADOR" , dados_doacao["cpf_doador"])
        print("\n")

    def seleciona_doacao(self):
        codigo = int(input("Código da doação que deseja selecionar:"))
        return codigo
    
    def pega_dados_listagem(self):
        print("-------- DADOS LISTAGEM ----------")
        inicio = input("Início: ")
        fim = input("Fim: ")

        return {"início" : inicio, "fim" : fim}

    def mostra_mensagem(self, msg):
        print(msg)
