# Trabalho de POO2

Tema: Padrão (ONG de Adoção)

```mermaid

classDiagram
    class Pessoa {
        -str __cpf
        -str __nome
        -str __dataNasc
        -str __endereco
        -str __tipoHab
        -str __tamanhoHab
        -int __numeroAnimais
        + <<create>> __init__(cpf: str, nome: str, dataNasc: date, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int)
        +cpf(): str
        +cpf(str)
        +nome(): str
        +nome(str)
        +dataNasc(): date
        +dataNasc(date)
        +endereco(): str
        +endereco(str)
        +tipoHab(): str
        +tipoHab(str)
        +tamanhoHab(): str
        +tamanhoHab(str)
        +numeroAnimais(): int
        +numeroAnimais(int)
        +idade(data:date): int
    }

    class Animal {
        -int __chip
        -str __nome
        -str __raca
        -str __tamanho
        -list~str~ __historicoVacinas
        + <<create>> __init__(chip: str, nome: str, raca: str, tamanho: str)
        +chip(): str
        +chip(str)
        +nome(): str
        +nome(str)
        +raca(): str
        +raca(str)
        +tamanho(): str
        +tamanho(str)
        +historicoVacinas(): list~str~
        +addVacina(vacina: str, data: date)
        +apto(): bool
    }

    class RegistroD {
        -str __data
        -Animal __animal
        -Pessoa __doador
        -str __motivo
        + <<create>> __init__(data: str, animal: Animal, doador: Pessoa, motivo: str)
        +data(): str
        +data(str)
        +animal(): Animal
        +animal(Animal)
        +doador(): Pessoa
        +doador(Pessoa)
        +motivo(): str
        +motivo(str)
    }

    class RegistroA {
        -str __data
        -Animal __animal
        -Pessoa __adotante
        -bool __termo
        + <<create>> __init__(data: str, animal: Animal, adotante: Pessoa, termo: bool)
        +data(): str
        +data(str)
        +animal(): Animal
        +animal(Animal)
        +adotante(): Pessoa
        +adotante(Pessoa)
        +termo(): bool
        +termo(bool)
    }

    class Sistema {
        -list~Animal~ __animais
        -list~Pessoa~ __pessoas
        -list~RegistroD~ __doacoes
        -list~RegistroA~ __adocoes
        + <<create>> __init__()
        +animais: list~Animal~
        +pessoas: list~Pessoa~
        +doacoes: list~RegistroD~
        +adocoes: list~RegistroA~
        +cadastrarPessoa(cpf: str, nome: str, dataNasc: str, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int)
        +cadastrarAdotante(cpf: str, nome: str, dataNasc: str, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int)
        +excluirPessoa(pessoa: Pessoa)
        +cadastrarAnimal(chip: str, nome: str, raca: str, tamanho: str)
        +excluirAnimal(animal: Animal)
        +cadastrarDoacao(data: date, animal: Animal, doador: Pessoa, motivo: str)
        +cadastrarAdocao(data: date, animal: Animal, adotante: Pessoa)
        +relatorioDoacoes(comeco: date, fim: date): list~RegistroD~
        +relatorioAdocoes(comeco: date, fim: date): list~RegistroA~
        +disponiveisParaAdocao(): list~Animal~
    }

    RegistroD "1" o-- "1" Animal : animal
    RegistroD "1" o-- "1" Pessoa : doador
    RegistroA "1" o-- "1" Animal : animal
    RegistroA "1" o-- "1" Pessoa : adotante
    Sistema "1" --> "many" Pessoa : pessoa
    Sistema "1" --> "many" Animal : animal
    Sistema "1" --> "many" RegistroD : doação
    Sistema "1" --> "many" RegistroA : adoção