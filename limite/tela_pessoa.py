class TelaPessoa():

    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar pessoa")
        print("2 - Alterar cadastro")
        print("3 - Listar cadastrados")
        print("4 - Excluir cadastro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ----------")
        cpf = int(input("CPF: "))
        nome = input("Nome completo: ")
        dataNasc = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        tipoHab = input("Tipo de habitação: ")
        tamanhoHab = input("Tamanho da habitação: ")
        numeroAnimais = int(input("Número de animais: "))

        return {
            "CPF": cpf,
            "nome": nome,
            "data de nascimento" : dataNasc,
            "endereço" : endereco,
            "tipo de habitação" : tipoHab,
            "tamanho da habitação" : tamanhoHab,
            "número de animais" : numeroAnimais 
        }

    def mostra_pessoa(self, dados_pessoa):
        print("CPF: ", dados_pessoa["CPF"])
        print("NOME COMPLETO: ", dados_pessoa["nome"])
        print("DATA DE NASCIMENTO: ", dados_pessoa["data de nascimento"])
        print("ENDEREÇO: ", dados_pessoa["endereço"])
        print("TIPO DE HABITAÇÃO: ", dados_pessoa["tipo de habitação"])
        print("TAMANHO DA HABITAÇÃO: ", dados_pessoa["tamanho da habitação"])
        print("NÚMERO DE ANIMAIS: ", dados_pessoa["número de animais"])
        print("\n")

    def seleciona_pessoa(self):
        cpf = int(input("CPF da pessoa que deseja selecionar: "))
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)