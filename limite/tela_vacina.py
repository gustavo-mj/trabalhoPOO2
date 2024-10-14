from datetime import datetime

class TelaVacina():

    def tela_opcoes(self):
        print("-------- VACINAÇÃO ----------")
        print("Escolha a opcao")
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

    def mostra_vacinacao(self, dados_vacinacao):
        print("CODIGO DA VACINAÇÃO: ", dados_vacinacao["codigo"])
        print("NOME DO ANIMAL", dados_vacinacao["nome_animal"])
        print("CHIP DO ANIMAL" , dados_doacao["chip_animal"])
        print("TIPO VACINAL" , dados_doacao["tipo_vacinal"])
        print("\n")

    def seleciona_vacinacao(self):
        codigo = int(input("Código da vacinação que deseja selecionar:"))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)