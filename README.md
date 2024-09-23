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
        + <<create>> __init__(cpf: str, nome: str, dataNasc: str, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int)
        +cpf(): str
        +cpf(str)
        +nome(): str
        +nome(str)
        +dataNasc(): str
        +dataNasc(str)
        +endereco(): str
        +endereco(str)
        +tipoHab(): str
        +tipoHab(str)
        +tamanhoHab(): str
        +tamanhoHab(str)
        +numeroAnimais(): int
        +numeroAnimais(int)
    }

    class Animal {
        -int __chip
        -str __nome
        -str __raca
        -str __tamanho
        + <<create>> __init__(chip: str, nome: str, raca: str, tamanho: str)
        +chip(): str
        +chip(str)
        +nome(): str
        +nome(str)
        +raca(): str
        +raca(str)
        +tamanho(): str
        +tamanho(str)
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
        +cadastrarPessoa(pessoa: Pessoa)
        +excluirPessoa(pessoa: Pessoa)
        +cadastrarAnimal(animal: Animal)
        +excluirAnimal(animal: Animal)
        +animais: list~Animal~
        +pessoas: list~Pessoa~
        +doacoes: list~RegistroD~
        +adocoes: list~RegistroA~
    }

    Pessoa "1" --> "many" Animal : owns
    RegistroD "1" --> "1" Animal : refers to
    RegistroD "1" --> "1" Pessoa : doador
    RegistroA "1" --> "1" Animal : refers to
    RegistroA "1" --> "1" Pessoa : adotante
    Sistema "1" --> "many" Pessoa : manages
    Sistema "1" --> "many" Animal : manages
    Sistema "1" --> "many" RegistroD : records
    Sistema "1" --> "many" RegistroA : records