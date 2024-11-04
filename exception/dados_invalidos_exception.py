class DadosInvalidosException(Exception):
    def __init__(self):
        super().__init__("Erro: dados de entrada inválidos ou ausentes.")