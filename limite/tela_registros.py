class TelaDoacao:

    def tela_opcoes(self):
        print("-------- DOAÇÕES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar doação")
        print("2 - Alterar cadastro")
        print("3 - Listar doações")
        print("4 - Excluir doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DA DOAÇÃO --------")
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
        codigo = int(input("Código da doação que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)

class TelaAdocao():

    def tela_opcoes(self):
        print("-------- ADOÇÕES --------")
        print("Escolha a opção:")
        print("1 - Mostrar disponíveis")
        print("2 - Cadastrar adoção")
        print("3 - Alterar cadastro")
        print("3 - Listar adoções")
        print("4 - Excluir adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS DA ADOÇÃO --------")
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
        codigo = int(input("Código da adoção que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)