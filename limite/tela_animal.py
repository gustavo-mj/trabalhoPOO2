class TelaAnimal():

    def tela_opcoes(self):
        print("-------- ANIMAIS --------")
        print("Escolha a opção:")
        print("1 - Cadastrar cachorro")
        print("2 - Cadastrar gato")
        print("3 - Alterar cadastro")
        print("4 - Listar cadastrados")
        print("5 - Excluir cadastro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_cahorro(self):
        print("-------- DADOS DO CACHORRO --------")
        chip = int(input("Chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")
        tamanho = int(input("Tamanho(1 - pequeno; 2 - médio; 3 - grande): "))

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca,
            "tamanho" : tamanho
        }

    def pega_dados_gato(self):
        print("-------- DADOS DO GATO --------")
        chip = int(input("Chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        return {
            "chip": chip,
            "nome": nome,
            "raca" : raca
        }

    def mostra_animal(self, dados_animal):
        print("ESPÉCIE: ", dados_animal["especie"])
        print("STATUS", dados_animal["status"])
        print("CHIP: ", dados_animal["chip"])
        print("NOME: ", dados_animal["nome"])
        print("RAÇA: ", dados_animal["raca"])
        try:
            print("TAMANHO: ", dados_animal["tamanho"])
        except Exception as e:
            pass
        print("\n")

    def seleciona_animal(self):
        chip = int(input("Código do chip do animal que deseja selecionar: "))
        return chip

    def mostra_mensagem(self, msg):
        print(msg)