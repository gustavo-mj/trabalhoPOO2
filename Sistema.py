from Pessoa import Pessoa
from Animal import Animal
from RegistroA import RegistroA
from RegistroD import RegistroD
from datetime import date

class Sistema:
    def __init__(self):
        self.__animais = []
        self.__pessoas = []
        self.__doacoes = []
        self.__adocoes = []
    
    @property
    def animais(self):
        return self.__animais
    
    @property
    def pessoas(self):
        return self.__pessoas

    @property
    def doacoes(self):
        return self.__doacoes

    @property
    def adocoes(self):
        return self.__adocoes

    def cadastrarPessoa(self, cpf: str, nome: str, dataNasc: date, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int):
        if isinstance(cpf, str):
            for cadastrado in self.__pessoas:
                if cadastrado.cpf() == cpf:
                    return None
        pessoa = Pessoa(cpf, nome, dataNasc, endereco, tipoHab, tamanhoHab, numeroAnimais)
        self.__pessoas.append(pessoa)

    def excluirPessoa(self, pessoa: Pessoa):
        if pessoa in self.__pessoas:
            self.__pessoas.remove(pessoa)
    
    def cadastrarAnimal(self, chip: str, nome: str, raca: str, tamanho: str):
        if isinstance(chip, str):
            for cadastrado in self.__animais:
                if cadastrado.chip() == chip:
                    return None
        animal = Animal(chip, nome, raca, tamanho)
        self.__animais.append(animal)

    def excluirAnimal (self, animal: Animal):
        if animal in self.__animais:
            self.__animais.remove(animal)
    
    def cadastrarDoacao(self, data: date, animal: Animal, doador: Pessoa, motivo: str):
        if isinstance(data, date) and isinstance(animal, Animal) and isinstance(doador, Pessoa) and isinstance(motivo, str):
            for doacaoCadastrada in self.__doacoes:
                if ((doacaoCadastrada.data() == data) and (doacaoCadastrada.animal() == animal) and (doacaoCadastrada.doador() == doador) and (doacaoCadastrada.motivo() == motivo)):
                    return None
        doacao = RegistroD(data, animal, doador, motivo)
        self.__doacoes.append(doacao)

    def cadastrarAdocao(self, data: date, animal: Animal, adotante: Pessoa):
        if isinstance(data, date) and isinstance(animal, Animal) and isinstance(doador, Pessoa):
            if (adotante.idade(data) < 18) or not(animal.apto()):
                return None
            elif (animal.tamanho() == 'grande') and (adotante.tipoHab() == 'apartamento') and (adotante.tamanhoHab() == 'pequeno'):
                return None
            for adocaoCadastrada in self.__adocoes:
                if ((adocaoCadastrada.data() == data) and (adocaoCadastrada.animal() == animal) and (adocaoCadastrada.adotante() == adotante)):
                    return None
        adocao = RegistroA(data, animal, adotante, True)
        self.__adocoes.append(adocao)

    def relatorioDoacoes(self, comeco: date, fim: date):
        if not(isinstance(comeco, date) and isinstance(fim, date)):
            return None
        else:
            return [doacao for doacao in self.__doacoes if comeco <= doacao.data() <= fim]

    def relatorioAdocoes(self, comeco: date, fim: date):
        if not(isinstance(comeco, date) and isinstance(fim, date)):
            return None
        else:
            return [adocao for adocao in self.__adocoes if comeco <= adocao.data() <= fim]

    def disponiveisParaAdocao(self):
        disponiveis = []
        for doacao in self.__doacoes:
            flag = False
            for adocao in self.__adocoes:
                if doacao.animal() == adocao.animal():
                    flag = True
                    break
            if not flag:
                disponiveis.append(doacao.animal())
        return disponiveis