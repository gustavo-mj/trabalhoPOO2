from datetime import datetime

class TelaDoador():

    def tela_opcoes(self):
        print("-------- DOADORES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar doador")
        print("2 - Alterar cadastro")
        print("3 - Listar doadores")
        print("4 - Excluir cadastro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_doador(self):
        print("-------- DADOS DO DOADOR --------")
        cpf = int(input("CPF: "))
        nome = input("Nome completo: ")
        dataNasc = datetime.strptime(input("Data de nascimento(dd/mm/aaaa): "), "%d/%m/%Y").date()
        endereco = input("Endereço: ")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : dataNasc,
            "endereco" : endereco}

    def mostra_doador(self, dados_doador):
        print("CPF: ", dados_pessoa["cpf"])
        print("NOME COMPLETO: ", dados_pessoa["nome"])
        print("DATA DE NASCIMENTO: ", dados_pessoa["data_de_nascimento"])
        print("ENDEREÇO: ", dados_pessoa["endereco"])
        print("\n")

    def seleciona_doador(self):
        cpf = int(input("CPF do doador que deseja selecionar: "))
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)

class TelaAdotante():

    def tela_opcoes(self):
        print("-------- ADOTANTES --------")
        print("Escolha a opção:")
        print("1 - Cadastrar adotante")
        print("2 - Alterar cadastro")
        print("3 - Listar adotantes")
        print("4 - Excluir cadastro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_adotante(self):
        print("-------- DADOS DO ADOTANTE --------")
        cpf = int(input("CPF: "))
        nome = input("Nome completo: ")
        dataNasc = datetime.strptime(input("Data de nascimento(dd/mm/aaaa): "), "%d/%m/%Y").date()
        endereco = input("Endereço: ")
        tipoHab = int(input("Tipo de habitação(1 - casa; 2- apartamento): "))
        tamanhoHab = int(input("Tamanho da habitação(1 - pequeno; 2 - médio; 3 - grande): "))
        numeroAnimais = int(input("Número de animais: "))

        return {
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento" : dataNasc,
            "endereco" : endereco,
            "tipo_de_habitacao" : tipoHab,
            "tamanho_da_habitacao" : tamanhoHab,
            "numero_de_animais" : numeroAnimais}

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