from datetime import date
from datetime import datetime


class TelaDoacao:

    def tela_opcoes(self):
        print("-------- DOAÇÕES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar doação")
        print("2 - Alterar cadastro")
        print("3 - Listar doações")
        print("4 - Listar doações num período")
        print("5 - Excluir doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DA DOAÇÃO --------")
        cpf = int(input("CPF do doador: "))
        chip = int(input("Chip do animal: "))
        data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
        motivo = input("Motivo: ")

        return {"cpf" : cpf, "chip" : chip, "data" : data, "motivo" : motivo}

    def mostra_doacao(self, dados_doacao):
        print("CODIGO DA DOACAO: ", dados_doacao["codigo"])
        print("NOME DO ANIMAL" , dados_doacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("NOME DO DOADOR" , dados_doacao["nome_doador"])
        print("CPF DO DOADOR" , dados_doacao["cpf_doador"])
        print("DATA", dados_doacao["data"])
        print("\n")

    def seleciona_doacao(self):
        codigo = int(input("Código da doação que deseja selecionar: "))
        return codigo

    def seleciona_periodo(self):
        inicio = datetime.strptime(input("Início: "), "%d/%m/%Y").date()
        fim = datetime.strptime(input("Fim: "), "%d/%m/%Y").date()
        return {"inicio" : inicio, "fim" : fim}

    def mostra_mensagem(self, msg):
        print(msg)

class TelaAdocao():

    def tela_opcoes(self):
        print("-------- ADOÇÕES --------")
        print("Escolha a opção:")
        print("1 - Mostrar disponíveis")
        print("2 - Cadastrar adoção")
        print("3 - Alterar cadastro")
        print("4 - Listar adoções")
        print("5 - Listar adoções num período")
        print("6 - Excluir adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS DA ADOÇÃO --------")
        cpf = int(input("CPF do Adotante: "))
        chip = int(input("Chip do animal: "))
        data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()

        return {"cpf" : cpf, "chip" : chip, "data" : data}

    def mostra_adocao(self, dados_adocao):
        print("CODIGO DA DOACAO: ", dados_adocao["codigo"])
        print("NOME DO ANIMAL" , dados_adocao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_adocao["chip_animal"])
        print("NOME DO ADOTANTE" , dados_adocao["nome_adotante"])
        print("CPF DO ADOTANTE" , dados_adocao["cpf_adotante"])
        print("DATA", dados_adocao["data"])
        print("\n")

    def seleciona_adocao(self):
        codigo = int(input("Código da adoção que deseja selecionar: "))
        return codigo
    
    def seleciona_periodo(self):
        inicio = datetime.strptime(input("Início: "), "%d/%m/%Y").date()
        fim = datetime.strptime(input("Fim: "), "%d/%m/%Y").date()
        return {"inicio" : inicio, "fim" : fim}

    def mostra_mensagem(self, msg):
        print(msg)