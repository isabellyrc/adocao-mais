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

def calcular_compatibilidade(adotante, animal):
    pontuacao = 0

    comportamento = animal.get("comportamento", "").lower()
    especie = animal.get("especie", "").lower()

    # +2 se a espécie desejada bate com a espécie do animal
    if adotante.get("especie_desejada", "").lower() == especie:
        pontuacao += 2

    # +2 se o nível de energia combina com o comportamento do animal
    energia = adotante.get("energia", "").lower()
    if energia == "alta" and comportamento == "agitado":
        pontuacao += 2
    elif energia == "baixa" and comportamento == "calmo":
        pontuacao += 2

    # +2 se o tipo de moradia combina com o animal
    moradia = adotante.get("moradia", "").lower()
    if moradia == "casa":
        pontuacao += 2
    elif moradia == "apartamento":
        if comportamento == "calmo" or especie == "gato":
            pontuacao += 2

    # +2 se tem crianças em casa e o animal é calmo ou carinhoso
    if adotante.get("criancas", "").lower() == "sim":
        if comportamento in ["carinhoso", "calmo"]:
            pontuacao += 2
    else:
        pontuacao += 2  # sem crianças, qualquer animal é compatível

    # +2 se tem outros animais e o pet é sociável
    if adotante.get("outros_animais", "").lower() == "sim":
        if comportamento in ["carinhoso", "calmo"]:
            pontuacao += 2
    else:
        pontuacao += 2  # sem outros animais, qualquer animal é compatível

    return pontuacao

def sugerir_animais(adotante):
    animais = arquivos.carregar_animais()

    if not animais:
        print("Nenhum animal cadastrado no sistema para fazer o matching.")
        return

    # calcula pontuação de cada animal e guarda numa lista
    ranking = []
    for animal in animais:
        pontos = calcular_compatibilidade(adotante, animal)
        porcentagem = (pontos / 10) * 100
        ranking.append({"animal": animal, "pontos": pontos, "porcentagem": porcentagem})

    # ordena do mais compatível para o menos compatível
    ranking.sort(key=lambda x: x["porcentagem"], reverse=True)

    print(f"\n{'=' * 50}")
    print(f"  MATCHINGS PARA: {adotante['nome'].upper()}")
    print(f"  Prefere: {adotante['especie_desejada'].capitalize()} | Energia: {adotante['energia']} | Moradia: {adotante['moradia']}")
    print(f"{'=' * 50}")

    for item in ranking:
        pet = item["animal"]
        print(f"\nNome: {pet['nome']} ({pet['especie'].capitalize()} - {pet['raca']})")
        print(f"Comportamento: {pet['comportamento'].capitalize()} | Idade: {pet['idade']} ano(s)")
        print(f"Compatibilidade: {item['porcentagem']:.0f}%  ({item['pontos']}/10 pontos)")
        print("-" * 50)

def menu_matching():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("✹" * 30)
        print("   BEM VINDO AO SISTEMA DE MATCHING!")
        print("✹" * 30)
        print("1 - Cadastrar novo adotante e ver sugestões")
        print("2 - Ver sugestões de adotante já cadastrado")
        print("0 - Voltar ao menu principal")
        print("✹" * 30)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break

        elif opcao == "1":
            os.system("cls" if os.name == "nt" else "clear")
            adotante = cadastrar_adotante()
            if adotante:
                sugerir_animais(adotante)
                input("\nPressione Enter para voltar ao menu...")

        elif opcao == "2":
            os.system("cls" if os.name == "nt" else "clear")
            adotantes = arquivos.carregar_adotantes()
            if not adotantes:
                print("Nenhum adotante cadastrado ainda. Escolha a opção 1.")
                input("\nPressione Enter para continuar...")
                continue

            print("--- Adotantes Cadastrados ---")
            for a in adotantes:
                print(f"ID: {a['id']} - {a['nome']} (Prefere: {a['especie_desejada'].capitalize()})")

            id_escolhido = input("\nDigite o ID do adotante: ").strip()

            adotante_selecionado = None
            for a in adotantes:
                if str(a["id"]) == id_escolhido:
                    adotante_selecionado = a
                    break

            if adotante_selecionado:
                os.system("cls" if os.name == "nt" else "clear")
                sugerir_animais(adotante_selecionado)
            else:
                print("Adotante não encontrado.")

            input("\nPressione Enter para voltar ao menu...")

        else:
            print("Opção inválida!")
            input("\nPressione Enter para continuar...")


