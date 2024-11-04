from datetime import datetime
from abstract.tela_abstrata import TelaAbstrata

class TelaVacina(TelaAbstrata):

    def tela_opcoes(self):
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

    def pega_dados_vacina(self):
        print("-------- DADOS VACINAÇÃO ----------")
        while True:
            try:
                chip = int(input("Chip do animal: "))
                tipo = int(input("Tipo vacinal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {"chip" : chip, "tipo_vacinal" : tipo, "data" : data}

    def pega_novos_dados_vacina(self):
        print("-------- DADOS DE ALTERAÇÃO DA VACINAÇÃO ----------")
        while True:
            try:
                tipo = int(input("Tipo vacinal: "))
                data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {"tipo_vacinal" : tipo, "data" : data}

    def mostra_vacinacao(self, dados_vacinacao):
        print("ÍNDICE", dados_vacinacao["indice"])
        print("TIPO VACINAL" , dados_vacinacao["tipo_vacinal"])
        print("DATA: ", dados_vacinacao["data"])
        print("\n")

    def seleciona_vacinacao(self):
        codigo = int(input("Índice da vacina que deseja selecionar:"))
        return codigo

    def seleciona_animal(self):
        chip = int(input("Digite o chip do animal que deseja selecionar:"))
        return chip

    def mostra_mensagem(self, msg):
        print(msg)