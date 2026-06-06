import csv
import os

PASTA_DADOS = "dados"

ARQUIVO_ANIMAIS = os.path.join(PASTA_DADOS, "animais.csv")
ARQUIVO_TAREFAS = os.path.join(PASTA_DADOS, "tarefas.csv")
ARQUIVO_ADOTANTES = os.path.join(PASTA_DADOS, "adotantes.csv")
ARQUIVO_ADOCOES = os.path.join(PASTA_DADOS, "adocoes.csv")


def carregar_animais():
    try:
        animais = []

        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for animal in leitor:
                animais.append(animal)

        return animais

    except FileNotFoundError:
        return []

    except Exception as erro:
        print("Erro ao carregar animais:", erro)
        return []


def salvar_animais(animais):
    try:

        campos = [
            "id",
            "nome",
            "especie",
            "raca",
            "idade",
            "saude",
            "data_chegada",
            "comportamento"
        ]

        with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8", newline="") as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(animais)

    except Exception as erro:
        print("Erro ao salvar animais:", erro)


def carregar_tarefas():
    try:
        tarefas = []

        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for tarefa in leitor:
                tarefas.append(tarefa)

        return tarefas

    except FileNotFoundError:
        return []

    except Exception as erro:
        print("Erro ao carregar tarefas:", erro)
        return []


def salvar_tarefas(tarefas):
    try:

        campos = [
            "id",
            "id_animal",
            "animal",
            "tipo",
            "data",
            "concluida"
        ]

        with open(ARQUIVO_TAREFAS, "w", encoding="utf-8", newline="") as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(tarefas)

    except Exception as erro:
        print("Erro ao salvar tarefas:", erro)


def carregar_adotantes():
    try:
        adotantes = []

        with open(ARQUIVO_ADOTANTES, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for adotante in leitor:
                adotantes.append(adotante)

        return adotantes

    except FileNotFoundError:
        return []

    except Exception as erro:
        print("Erro ao carregar adotantes:", erro)
        return []


def salvar_adotantes(adotantes):
    try:

        campos = [
            "id",
            "nome",
            "especie_desejada",
            "porte",
            "energia",
            "criancas",
            "outros_animais",
            "moradia"
        ]

        with open(ARQUIVO_ADOTANTES, "w", encoding="utf-8", newline="") as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(adotantes)

    except Exception as erro:
        print("Erro ao salvar adotantes:", erro)


def carregar_adocoes():
    try:
        adocoes = []

        with open(ARQUIVO_ADOCOES, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for adocao in leitor:
                adocoes.append(adocao)

        return adocoes

    except FileNotFoundError:
        return []

    except Exception as erro:
        print("Erro ao carregar adoções:", erro)
        return []


def salvar_adocoes(adocoes):
    try:

        campos = [
            "id",
            "id_animal",
            "id_adotante",
            "data_adocao",
            "status"
        ]

        with open(ARQUIVO_ADOCOES, "w", encoding="utf-8", newline="") as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(adocoes)

    except Exception as erro:
        print("Erro ao salvar adoções:", erro)