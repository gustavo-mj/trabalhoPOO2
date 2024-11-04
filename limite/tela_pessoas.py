from datetime import datetime
from entidade.adotante import *
from abstract.tela_abstrata import TelaAbstrata

class TelaDoador(TelaAbstrata):

    def tela_opcoes(self):
        print("-------- DOADORES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar doador")
        print("2 - Alterar cadastro")
        print("3 - Listar doadores")
        print("4 - Excluir cadastro")
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

    def pega_dados_doador(self):
        print("-------- DADOS DO DOADOR --------")
        while True:
            try:
                cpf = int(input("CPF: "))
                nome = input("Nome completo: ")
                data_de_nascimento = datetime.strptime(input("Data de nascimento(dd/mm/aaaa): "), "%d/%m/%Y").date()
                endereco = input("Endereço: ")
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : data_de_nascimento,
            "endereco" : endereco}

    def mostra_doador(self, dados_doador):
        print("CPF: ", dados_doador["cpf"])
        print("NOME COMPLETO: ", dados_doador["nome"])
        print("DATA DE NASCIMENTO: ", dados_doador["data_de_nascimento"])
        print("ENDEREÇO: ", dados_doador["endereco"])
        print("\n")

    def seleciona_doador(self):
        cpf = int(input("CPF do doador que deseja selecionar: "))
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)

class TelaAdotante(TelaAbstrata):

    def tela_opcoes(self):
        print("-------- ADOTANTES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar adotante")
        print("2 - Alterar cadastro")
        print("3 - Listar adotantes")
        print("4 - Excluir cadastro")
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

    def pega_dados_adotante(self):
        print("-------- DADOS DO ADOTANTE --------")
        while True:
            try:
                cpf = int(input("CPF: "))
                nome = input("Nome completo: ")
                data_de_nascimento = datetime.strptime(input("Data de nascimento(dd/mm/aaaa): "), "%d/%m/%Y").date()
                endereco = input("Endereço: ")
                tipo_de_habitacao = TipoHabitacao(int(input("Tipo de habitação(1 - casa; 2- apartamento): ")))
                tamanho_da_habitacao = TamanhoHabitacao(int(input("Tamanho da habitação(1 - pequeno; 2 - médio; 3 - grande): ")))
                numero_de_animais = int(input("Número de animais: "))
                break
            except ValueError as e:
                print("Você inseriu um valor inválido. Tente novamente.")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : data_de_nascimento,
            "endereco" : endereco,
            "tipo_de_habitacao" : tipo_de_habitacao,
            "tamanho_da_habitacao" : tamanho_da_habitacao,
            "numero_de_animais" : numero_de_animais}

    def mostra_adotante(self, dados_pessoa):
        print("CPF: ", dados_pessoa["cpf"])
        print("NOME COMPLETO: ", dados_pessoa["nome"])
        print("DATA DE NASCIMENTO: ", dados_pessoa["data_de_nascimento"])
        print("ENDEREÇO: ", dados_pessoa["endereco"])
        print("TIPO DE HABITAÇÃO: ", dados_pessoa["tipo_de_habitacao"])
        print("TAMANHO DA HABITAÇÃO: ", dados_pessoa["tamanho_da_habitacao"])
        print("NÚMERO DE ANIMAIS: ", dados_pessoa["numero_de_animais"])
        print("\n")

    def seleciona_adotante(self):
        cpf = int(input("CPF do adotante que deseja selecionar: "))
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)