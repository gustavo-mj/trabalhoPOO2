class CadastroInexistenteException(Exception):
    def __init__(self):
        super().__init__("Erro: cadastro inexistente.")