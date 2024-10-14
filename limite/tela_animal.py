class TelaAnimal():

    def tela_opcoes(self):
        print("-------- ANIMAIS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar animal")
        print("2 - Alterar cadastro")
        print("3 - Listar cadastrados")
        print("4 - Excluir cadastro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_animal(self):
        print("-------- DADOS ANIMAL ----------")
        chip = int(input("Chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")
        tamanho = input("Tamanho: ")

        return {
            "chip": chip,
            "nome": nome,
            "raça" : raca,
            "tamanho" : tamanho
        }

    def mostra_animal(self, dados_animal):
        print("CHIP: ", dados_animal["chip"])
        print("NOME: ", dados_animal["nome"])
        print("RAÇA: ", dados_animal["raça"])
        print("TAMANHO: ", dados_animal["tamanho"])
        print("\n")

    def seleciona_animal(self):
        chip = int(input("Código do chip do animal que deseja selecionar: "))
        return chip

    def mostra_mensagem(self, msg):
        print(msg)