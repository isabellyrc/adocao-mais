import os
import validacao
import arquivos

def cadastrar_adotante():
    print("\n--- Cadastro do Adotante ---")

    nome = input("Nome do Adotante: ").strip()
    if not nome:
        print("Erro: o nome é obrigatório.")
        return None

    especie_desejada = input("Espécie desejada (cachorro, gato, outro): ").strip().lower()
    if not validacao.validar_especie(especie_desejada):
        print("Erro: espécie inválida. Opções: cachorro, gato, outro.")
        return None

    energia = input("Nível de energia preferido (alta, baixa): ").strip().lower()
    if energia not in ["alta", "baixa"]:
        print("Erro: energia inválida. Opções: alta, baixa.")
        return None

    criancas = input("Possui crianças em casa? (sim, nao): ").strip().lower()
    if criancas not in ["sim", "nao"]:
        print("Erro: resposta inválida. Opções: sim, nao.")
        return None

    outros_animais = input("Possui outros animais em casa? (sim, nao): ").strip().lower()
    if outros_animais not in ["sim", "nao"]:
        print("Erro: resposta inválida. Opções: sim, nao.")
        return None

    moradia = input("Tipo de moradia (casa, apartamento): ").strip().lower()
    if moradia not in ["casa", "apartamento"]:
        print("Erro: moradia inválida. Opções: casa, apartamento.")
        return None

    # carrega a lista atual e gera um ID sequencial
    adotantes = arquivos.carregar_adotantes()
    id_adotante = len(adotantes) + 1

    novo_adotante = {
        "id": id_adotante,
        "nome": nome,
        "especie_desejada": especie_desejada,
        "porte": "",
        "energia": energia,
        "criancas": criancas,
        "outros_animais": outros_animais,
        "moradia": moradia
    }

    adotantes.append(novo_adotante)
    arquivos.salvar_adotantes(adotantes)
    print(f"\nAdotante '{nome}' cadastrado com sucesso! ID: {id_adotante}")
    return novo_adotante
