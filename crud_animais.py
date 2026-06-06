import os
import arquivos


# ════════════════════════════════════════════════════════
# FUNÇÕES AUXILIARES
# ════════════════════════════════════════════════════════

def _limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def _campo_vazio(valor):
    """Retorna True se o campo estiver vazio."""
    return str(valor).strip() == ""


def _idade_valida(idade):
    """Retorna True se a idade for um número inteiro não negativo."""
    try:
        return int(idade) >= 0
    except ValueError:
        return False


def _gerar_id(animais):
    """Gera um ID único que não muda mesmo após exclusões."""
    if not animais:
        return 1
    try:
        return max(int(a.get("id", 0)) for a in animais) + 1
    except (ValueError, TypeError):
        return len(animais) + 1


def _buscar_por_id(animais, id_animal):
    """Retorna o animal com o ID informado ou None."""
    for animal in animais:
        try:
            if int(animal.get("id", -1)) == id_animal:
                return animal
        except (ValueError, TypeError):
            continue
    return None


def _animal_duplicado(animais, nome, especie, id_ignorar=None):
    """Retorna True se já existir animal com mesmo nome e espécie."""
    for animal in animais:
        try:
            if id_ignorar is not None and int(animal.get("id", -1)) == id_ignorar:
                continue
        except (ValueError, TypeError):
            pass
        if (
            animal["nome"].lower() == nome.lower()
            and animal["especie"].lower() == especie.lower()
        ):
            return True
    return False


def _exibir_animal(animal):
    """Exibe os dados de um animal formatados no terminal."""
    print("\n-------------------------")
    print("ID          :", animal.get("id"))
    print("Nome        :", animal.get("nome"))
    print("Espécie     :", animal.get("especie"))
    print("Raça        :", animal.get("raca"))
    print("Idade       :", animal.get("idade"))
    print("Saúde       :", animal.get("saude"))
    print("Data chegada:", animal.get("data_chegada"))
    print("Comportamento:", animal.get("comportamento"))


# ════════════════════════════════════════════════════════
# FUNÇÕES DO CRUD
# ════════════════════════════════════════════════════════

def cadastrar_animal():
    try:
        _limpar_tela()
        animais = arquivos.carregar_animais()

        print("\n--- Cadastro de Animal ---")

        nome          = input("Nome: ").strip()
        especie       = input("Espécie: ").strip()
        raca          = input("Raça: ").strip()
        idade         = input("Idade: ").strip()
        saude         = input("Estado de saúde: ").strip()
        data_chegada  = input("Data de chegada (DD/MM/AAAA): ").strip()
        comportamento = input("Comportamento: ").strip()

        # Valida campos vazios
        campos = [nome, especie, raca, idade, saude, data_chegada, comportamento]
        if any(_campo_vazio(c) for c in campos):
            print("Erro: todos os campos são obrigatórios.")
            return

        # Valida idade
        if not _idade_valida(idade):
            print("Erro: idade inválida. Digite um número inteiro maior ou igual a zero.")
            return

        # Valida duplicata
        if _animal_duplicado(animais, nome, especie):
            print("Erro: já existe um(a)", especie, "com o nome", nome, "cadastrado(a).")
            return

        animal = {
            "id"           : _gerar_id(animais),
            "nome"         : nome,
            "especie"      : especie,
            "raca"         : raca,
            "idade"        : idade,
            "saude"        : saude,
            "data_chegada" : data_chegada,
            "comportamento": comportamento,
        }
        
        
        animais.append(animal)
        arquivos.salvar_animais(animais)
        print("Animal cadastrado com sucesso! ID:", animal["id"])

    except Exception as erro:
        print("Erro ao cadastrar animal:", erro)


def listar_animais():
    try:
        _limpar_tela()
        animais = arquivos.carregar_animais()

        if not animais:
            print("Nenhum animal cadastrado.")
            return

        print("\n--- Lista de Animais ---")
        for animal in animais:
            _exibir_animal(animal)

    except Exception as erro:
        print("Erro ao listar animais:", erro)


def editar_animal():
    try:
        _limpar_tela()
        animais = arquivos.carregar_animais()

        if not animais:
            print("Nenhum animal cadastrado.")
            return

        listar_animais()

        id_busca = input("\nDigite o ID do animal que deseja editar: ").strip()
        if not id_busca.isdigit():
            print("Erro: digite um ID válido.")
            return

        animal = _buscar_por_id(animais, int(id_busca))
        if not animal:
            print("Animal não encontrado.")
            return

        print("\nDigite os novos dados (ENTER para manter o valor atual):")

        novo_nome = input(f"Nome [{animal['nome']}]: ").strip() or animal["nome"]
        nova_especie = input(f"Espécie [{animal['especie']}]: ").strip() or animal["especie"]

        # Valida duplicata na edição (ignora o próprio animal)
        if _animal_duplicado(animais, novo_nome, nova_especie, id_ignorar=int(animal["id"])):
            print("Erro: já existe um(a)", nova_especie, "com o nome", novo_nome, "cadastrado(a).")
            return

        nova_raca          = input(f"Raça [{animal['raca']}]: ").strip() or animal["raca"]
        nova_idade         = input(f"Idade [{animal['idade']}]: ").strip() or animal["idade"]
        nova_saude         = input(f"Saúde [{animal['saude']}]: ").strip() or animal["saude"]
        nova_data          = input(f"Data chegada [{animal['data_chegada']}]: ").strip() or animal["data_chegada"]
        novo_comportamento = input(f"Comportamento [{animal['comportamento']}]: ").strip() or animal["comportamento"]

        # Valida campos vazios nos novos dados
        campos = [novo_nome, nova_especie, nova_raca, nova_idade, nova_saude, nova_data, novo_comportamento]
        if any(_campo_vazio(c) for c in campos):
            print("Erro: nenhum campo pode ficar vazio.")
            return

        # Valida idade
        if not _idade_valida(nova_idade):
            print("Erro: idade inválida.")
            return

        animal["nome"]          = novo_nome
        animal["especie"]       = nova_especie
        animal["raca"]          = nova_raca
        animal["idade"]         = nova_idade
        animal["saude"]         = nova_saude
        animal["data_chegada"]  = nova_data
        animal["comportamento"] = novo_comportamento

        arquivos.salvar_animais(animais)
        print("Animal atualizado com sucesso!")

    except Exception as erro:
        print("Erro ao editar animal:", erro)


def excluir_animal():
    try:
        _limpar_tela()
        animais = arquivos.carregar_animais()

        if not animais:
            print("Nenhum animal cadastrado.")
            return

        listar_animais()

        id_busca = input("\nDigite o ID do animal que deseja excluir: ").strip()
        if not id_busca.isdigit():
            print("Erro: digite um ID válido.")
            return

        animal = _buscar_por_id(animais, int(id_busca))
        if not animal:
            print("Animal não encontrado.")
            return

        confirmar = input(f"Tem certeza que deseja excluir '{animal['nome']}'? (s/n): ").strip().lower()
        if confirmar != "s":
            print("Exclusão cancelada.")
            return

        animais.remove(animal)
        arquivos.salvar_animais(animais)
        print("Animal removido com sucesso!")

    except Exception as erro:
        print("Erro ao excluir animal:", erro)

if __name__ == "__main__":
    cadastrar_animal()
    
    