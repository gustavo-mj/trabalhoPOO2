class ListaVaziaException(Exception):
    def __init__(self):
        super().__init__("Não há cadastros disponíveis para consumo.")