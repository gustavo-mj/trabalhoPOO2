class TelaAdocao():

    def tela_opcoes(self):
        print("-------- ADOÇÕES ----------")
        print("Escolha a opcao")
        print("1 - Fazer adoção")
        print("2 - Listar adoções")
        print("3 - Excluir adoção")
        print("4 - Listar disponíveis para adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS ADOÇÃO ----------")
        cpf = input("CPF do Adotante: ")
        chip = input("Chip do animal: ")
        data = input("Data: ")

        return {"cpf" : cpf, "chip" : chip, "data" : data}

    def mostra_adocao(self, dados_doacao):
        print("CODIGO DA DOACAO: ", dados_doacao["codigo"])
        print("NOME DO ANIMAL" , dados_doacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("NOME DO ADOTANTE" , dados_doacao["nome_adotante"])
        print("CPF DO ADOTANTE" , dados_doacao["cpf_adotante"])
        print("\n")

    def seleciona_adocao(self):
        codigo = int(input("Código da adoção que deseja selecionar:"))
        return codigo

    def pega_dados_listagem(self):
        print("-------- DADOS LISTAGEM ----------")
        inicio = input("Início: ")
        fim = input("Fim: ")

        return {"início" : inicio, "fim" : fim}

    def mostra_disponiveis(self, dados_disponiveis):
        print("NOME" , dados_disponiveis["nome_animal"])
        print("CHIP" , dados_disponiveis["chip_animal"])
        print("TAMANHO", dados_disponiveis["tamanho_animal"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)