from datetime import datetime

class TelaVacina():

    def tela_opcoes(self):
        print("-------- VACINAÇÃO ----------")
        print("Escolha a opção:")
        print("1 - Cadastrar vacinação")
        print("2 - Alterar cadastro")
        print("3 - Listar vacinações")
        print("4 - Excluir vacinação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_vacina(self):
        print("-------- DADOS VACINAÇÃO ----------")
        chip = int(input("Chip do animal: "))
        tipo = int(input("Tipo vacinal: "))
        data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()

        return {"chip" : chip, "tipo_vacinal" : tipo, "data" : data}

    def pega_novos_dados_vacina(self):
        print("-------- DADOS DE ALTERAÇÃO DA VACINAÇÃO ----------")
        tipo = int(input("Tipo vacinal: "))
        data = datetime.strptime(input("Data: "), "%d/%m/%Y").date()

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