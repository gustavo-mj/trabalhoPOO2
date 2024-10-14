# Trabalho de POO2

Tema: Padrão (ONG de Adoção)

```mermaid

classDiagram
    class Pessoa {
        -int __cpf
        -str __nome
        -str __dataNasc
        -str __endereco
        -str __tipoHab
        -str __tamanhoHab
        -int __numeroAnimais
        + <<create>> __init__(cpf: int, nome: str, dataNasc: date, endereco: str, tipoHab: str, tamanhoHab: str, numeroAnimais: int)
        +cpf(): int
        +cpf(int)
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
    }

    class Animal {
        -int __chip
        -str __nome
        -str __raca
        -str __tamanho
        + <<create>> __init__(chip: int, nome: str, raca: str, tamanho: str)
        +chip(): int
        +chip(int)
        +nome(): str
        +nome(str)
        +raca(): str
        +raca(str)
        +tamanho(): str
        +tamanho(str)
    }

    class Doacao {
        -str __data
        -Animal __animal
        -Pessoa __doador
        -str __motivo
        + <<create>> __init__(data: date, animal: Animal, doador: Pessoa, motivo: str)
        +data(): date
        +data(date)
        +animal(): Animal
        +animal(Animal)
        +doador(): Pessoa
        +doador(Pessoa)
        +motivo(): str
        +motivo(str)
    }

    class Adocao {
        -str __data
        -Animal __animal
        -Pessoa __adotante
        -bool __termo
        + <<create>> __init__(data: date, animal: Animal, adotante: Pessoa, termo: bool)
        +data(): date
        +data(date)
        +animal(): Animal
        +animal(Animal)
        +adotante(): Pessoa
        +adotante(Pessoa)
        +termo(): bool
        +termo(bool)
    }

    class Vacina {
        -int __codigo
        -Animal __animal
        -str __tipo
        -date __data
        + <<create>> __init__(codigo: int, animal: Animal, tipo: str, data: date)
        +codigo(): int
        +codigo(int)
        +animal(): Animal
        +animal(Animal)
        +tipo(): str
        +tipo(str)
    }

    class ControladorPessoa {
        -list~Pessoa~ __pessoas
        -ControladorSistema __controlador_sistema
        -TelaPessoa __tela_pessoa
        + <<create>> __init__(controlador_sistema: ControladorSistema)
        +pega_pessoa_por_cpf(cpf: int): Pessoa
        +cadastrar_pessoa()
        +alterar_cadastro()
        +lista_pessoa()
        +excluir_pessoa()
        +retornar()
        +abre_tela()
    }

    class ControladorAnimal {
        -list~Animal~ __animais
        -ControladorSistema __controlador_sistema
        -TelaAnimal __tela_animal
        + <<create>> __init__(controlador_sistema: ControladorSistema)
        +pega_animal_por_chip(chip: int): Animal
        +cadastrar_animal()
        +alterar_cadastro()
        +lista_animal()
        +excluir_animal()
        +retornar()
        +abre_tela()
    }

    class ControladorVacina {
        -ControladorSistema __controlador_sistema
        -list~Vacina~ __vacinacoes
        -TelaVacina __tela_vacinacao
        + <<create>> __init__(controlador_sistema: ControladorSistema)
        +pega_vacina_por_codigo(codigo: int): Vacina
        +cadastrar_vacinacao()
        +lista_vacinacoes()
        +lista_vacinas_por_animal(chip: int): list~str~
        +excluir_vacinacao()
        +retornar()
        +abre_tela()
    }

    class ControladorDoacoes {
        -ControladorSistema __controlador_sistema
        -list~Doacao~ __doacoes
        -TelaDoacao __tela_doacao
        + <<create>> __init__(controlador_sistema: ControladorSistema)
        +pega_doacao_por_codigo(codigo: int): Doacao
        +cadastrar_doacao()
        +lista_doacao()
        +excluir_doacao()
        +retornar()
        +abre_tela()
    }

    class ControladorAdocoes {
        -ControladorSistema __controlador_sistema
        -list~Adocao~ __adocoes
        -TelaAdocao __tela_adocao
        + <<create>> __init__(controlador_sistema: ControladorSistema)
        +pega_adocao_por_codigo(codigo: int) Adocao
        +cadastrar_adocao()
        +lista_adocao()
        +excluir_adocao()
        +listar_disponveis_para_adocao() list~dict~
        +retornar()
        +abre_tela()
    }

    class ControladorSistema {
        -ControladorAnimal __controlador_animais
        -ControladorPessoa __controlador_pessoas
        -ControladorDoacoes __controlador_doacoes
        -ControladorAdocoes __controlador_adocoes
        -ControladorVacina __controlador_vacinacoes
        -TelaSistema __tela_sistema
        + <<create>> __init__()
        +controlador_animais(): ControladorAnimal
        +controlador_pessoas(): ControladorPessoa
        +controlador_doacoes(): ControladorDoacoes
        +controlador_adocoes(): ControladorAdocoes
        +controlador_vacinacoes(): ControladorVacina
        +inicializa_sistema()
        +cadastra_animal()
        +cadastra_pessoa()
        +cadastra_doacao()
        +cadastra_adocao()
        +cadastra_vacinacao()
        +encerra_sistema()
        +abre_tela()
    }

    class TelaPessoa {
        +tela_opcoes(): int
        +pega_dados_pessoa(): dict
        +mostra_pessoa(dados_pessoa: dict)
        +seleciona_pessoa(): int
        +mostra_mensagem(msg: str)
    }

    class TelaAnimal {
        +tela_opcoes(): int
        +pega_dados_animal(): dict
        +mostra_pessoa(dados_animal: dict)
        +seleciona_animal(): int
        +mostra_mensagem(msg: str)
    }

    class TelaVacina {
        +tela_opcoes(): int
        +pega_dados_vacina(): dict
        +mostra_vacinacao(dados_vacinacao: dict)
        +seleciona_vacinacao(): int
        +mostra_mensagem(msg: str)
    }

    class TelaDoacao {
        +tela_opcoes(): int
        +pega_dados_doacao(): dict
        +mostra_doacao(dados_doacao: dict)
        +seleciona_doacao(): int
        +pega_dados_listagem(): dict
        +mostra_mensagem(msg: str)
    }

    class TelaAdocao {
        +tela_opcoes(): int
        +pega_dados_adocao(): dict
        +mostra_adocao(dados_adocao: dict)
        +seleciona_adocao(): int
        +pega_dados_listagem(): dict
        +mostra_disponiveis(dados_disponiveis: dict)
        +mostra_mensagem(msg: str)
    }

    class TelaSistema {
        +tela_opcoes(): int
    }

    Pessoa "many" <-- "1" ControladorPessoa
    TelaPessoa "1" <-* "1" ControladorPessoa

    Animal "many" <-- "1" ControladorAnimal
    TelaAnimal "1" <-* "1" ControladorAnimal

    Vacina "many" <-- "1" ControladorVacina
    TelaVacina "1" <-* "1" ControladorVacina
    Vacina "1" --> "1" Animal: animal

    Doacao "many" <-* "1" ControladorDoacoes
    TelaDoacao "1" <-* "1" ControladorDoacoes
    Doacao "1" --> "1" Animal: animal
    Doacao "1" --> "1" Pessoa: doador

    Adocao "many" <-* "1" ControladorAdocoes
    TelaAdocao "1" <-* "1" ControladorAdocoes
    Adocao "1" --> "1" Animal: animal
    Adocao "1" --> "1" Pessoa: adotante

    TelaSistema "1" <-* "1" ControladorSistema

    ControladorPessoa "1" <-* "1" ControladorSistema
    ControladorAnimal "1" <-* "1" ControladorSistema
    ControladorVacina "1" <-* "1" ControladorSistema
    ControladorAdocoes "1" <-* "1" ControladorSistema
    ControladorDoacoes "1" <-* "1" ControladorSistema