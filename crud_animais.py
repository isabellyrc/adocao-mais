import interface
import arquivos
import validacoes

# Constantes de negócio padronizadas
ESPECIES_VALIDAS       = ["cachorro", "gato", "coelho", "ave", "outro"]
COMPORTAMENTOS_VALIDOS = ["calmo", "agitado", "timido", "brincalhao", "agressivo"]
STATUS_SAUDE_VALIDOS   = ["saudavel", "em tratamento", "recuperacao"]


# ════════════════════════════════════════════════════════
# FUNÇÕES AUXILIARES DE SUPORTE
# ════════════════════════════════════════════════════════

def _gerar_id(animais):
    """Gera um ID único incremental de forma segura."""
    if not animais:
        return 1
    try:
        maior_id = max(int(a.get("id", 0)) for a in animais)
        return maior_id + 1
    except (ValueError, TypeError):
        return len(animais) + 1


def _buscar_por_id(animais, id_animal):
    """Retorna o animal correspondente ao ID informado ou None."""
    for animal in animais:
        try:
            if int(animal.get("id", -1)) == id_animal:
                return animal
        except (ValueError, TypeError):
            continue
    return None


def _animal_duplicado(animais, nome, especie, id_ignorar=None):
    """Evita que dois animais com mesmo nome e espécie coexistam."""
    for a in animais:
        try:
            if id_ignorar is not None and int(a.get("id", -1)) == id_ignorar:
                continue
        except (ValueError, TypeError):
            pass
        if (a.get("nome", "").strip().lower() == nome.strip().lower() and
                a.get("especie", "").strip().lower() == especie.strip().lower()):
            return True
    return False


def _exibir_animal_formatado(animal):
    """Imprime os dados estruturados de um animal no terminal."""
    print("\n" + "─" * 45)
    print(f"  ID           : {animal.get('id', '---')}")
    print(f"  Nome         : {animal.get('nome', '---')}")
    print(f"  Espécie      : {animal.get('especie', '---')}")
    print(f"  Raça         : {animal.get('raca', '---')}")
    print(f"  Idade        : {animal.get('idade', '---')} ano(s)")  # CORRIGIDO: era 'id_animal'
    print(f"  Saúde        : {animal.get('saude', '---')}")
    print(f"  Data Chegada : {animal.get('data_chegada', '---')}")
    print(f"  Comportamento: {animal.get('comportamento', '---')}")
    print("─" * 45)


# ENTRADAS VALIDADAS UTILIZANDO O MÓDULO DA MARIA CAROLINA


def _ler_campo_obrigatorio(prompt, nome_campo, valor_atual=None):
    """Lê um campo de texto não vazio. ENTER mantém valor_atual se fornecido."""
    while True:
        entrada = input(prompt).strip()
        if valor_atual is not None and entrada == "":
            return valor_atual
        if validacoes.validar_campo_vazio(entrada):
            return entrada
        print(f"  ⚠ O campo '{nome_campo}' não pode ficar vazio.")


def _ler_idade_validada(prompt, valor_atual=None):
    """Lê a idade com validação. ENTER mantém valor_atual se fornecido."""
    while True:
        entrada = input(prompt).strip()
        if valor_atual is not None and entrada == "":
            return valor_atual
        if validacoes.validar_idade(entrada):
            return int(entrada)
        print("  ⚠ Idade inválida! Digite um número inteiro maior ou igual a zero.")


def _ler_data_validada(prompt, valor_atual=None):
    """Lê uma data DD/MM/AAAA com validação. ENTER mantém valor_atual se fornecido."""
    while True:
        entrada = input(prompt).strip()
        if valor_atual is not None and entrada == "":
            return valor_atual
        if validacoes.validar_data(entrada):
            return entrada
        print("  ⚠ Data inválida! Use o formato DD/MM/AAAA.")


def _ler_opcao_lista(prompt, lista_validacao, valor_atual=None):
    """Lê uma opção dentro de uma lista válida. ENTER mantém valor_atual se fornecido."""
    while True:
        entrada = input(prompt).strip().lower()
        if valor_atual is not None and entrada == "":
            return valor_atual
        if validacoes.validar_opcao(entrada, lista_validacao):
            return entrada
        print(f"  ⚠ Opção inválida! Escolha entre: {', '.join(lista_validacao)}")


# ════════════════════════════════════════════════════════
# FUNÇÕES DO CRUD (CHAMADAS PELO MAIN)
# ════════════════════════════════════════════════════════

def cadastrar_animal():
    """Coleta, valida e registra um novo animal no sistema."""
    interface.limpar_tela()
    interface.exibir_cabecalho("CADASTRAR NOVO ANIMAL")

    try:
        animais = arquivos.carregar_animais()
    except Exception as e:
        interface.exibir_mensagem_erro(f"Erro ao acessar banco de dados: {e}")
        return

    nome = _ler_campo_obrigatorio("Nome do animal: ", "Nome")

    print(f"Espécies aceitas: {', '.join(ESPECIES_VALIDAS)}")
    especie = _ler_opcao_lista("Espécie: ", ESPECIES_VALIDAS)

    if _animal_duplicado(animais, nome, especie):
        interface.exibir_mensagem_erro(f"Já existe um(a) {especie} com o nome '{nome}' cadastrado(a)!")
        return

    raca         = _ler_campo_obrigatorio("Raça (ou SRD): ", "Raça")
    idade        = _ler_idade_validada("Idade em anos: ")  # CORRIGIDO: linha duplicada removida

    print(f"Status clínicos: {', '.join(STATUS_SAUDE_VALIDOS)}")
    saude        = _ler_opcao_lista("Estado de saúde: ", STATUS_SAUDE_VALIDOS)

    data_chegada = _ler_data_validada("Data de chegada (DD/MM/AAAA): ")

    print(f"Comportamentos: {', '.join(COMPORTAMENTOS_VALIDOS)}")
    comportamento = _ler_opcao_lista("Comportamento do animal: ", COMPORTAMENTOS_VALIDOS)

    novo_animal = {
        "id"           : _gerar_id(animais),
        "nome"         : nome,
        "especie"      : especie,
        "raca"         : raca,
        "idade"        : idade,
        "saude"        : saude,
        "data_chegada" : data_chegada,
        "comportamento": comportamento,
    }

    try:
        animais.append(novo_animal)
        arquivos.salvar_animal(animais)
        interface.exibir_mensagem_sucesso(f"'{nome}' cadastrado com sucesso! ID gerado: {novo_animal['id']}")
    except Exception as e:
        interface.exibir_mensagem_erro(f"Erro ao salvar registro: {e}")


def listar_animais():
    """Exibe todos os animais cadastrados com filtro opcional por espécie."""
    interface.limpar_tela()
    interface.exibir_cabecalho("LISTAGEM GERAL DE PETS")

    try:
        animais = arquivos.carregar_animais()
    except Exception as e:
        interface.exibir_mensagem_erro(f"Erro ao carregar dados: {e}")
        return

    if not animais:  # CORRIGIDO: era "if not) animais:"
        print("\n  Nenhum animal registrado no sistema até o momento.")
        input("\nPressione [Enter] para voltar...")
        return

    print(f"Filtrar listagem por espécie? ({', '.join(ESPECIES_VALIDAS)})")
    filtro = input("Digite a espécie ou pressione ENTER para exibir todos: ").strip().lower()

    exibidos = animais
    if filtro in ESPECIES_VALIDAS:
        exibidos = [a for a in animais if a.get("especie", "").lower() == filtro]

    print(f"\n  Registros encontrados: {len(exibidos)}")
    for animal in exibidos:
        _exibir_animal_formatado(animal)

    input("\nPressione [Enter] para continuar...")


def editar_animal():
    """Busca um animal pelo ID e permite alterar qualquer campo."""
    interface.limpar_tela()
    interface.exibir_cabecalho("MODIFICAR CADASTRO DE ANIMAL")

    try:
        animais = arquivos.carregar_animais()
    except Exception as e:
        interface.exibir_mensagem_erro(f"Erro de carregamento: {e}")
        return

    id_busca = input("Digite o ID numérico do animal: ").strip()
    if not id_busca.isdigit():
        interface.exibir_mensagem_erro("O ID deve ser exclusivamente numérico.")
        return

    animal = _buscar_por_id(animais, int(id_busca))
    if not animal:
        interface.exibir_mensagem_erro("Nenhum animal localizado com o ID informado.")
        return

    print("\n» Registro Atual:")
    _exibir_animal_formatado(animal)
    print("\n  Pressione [ENTER] sem digitar nada para MANTER o dado original.\n")

    id_atual     = int(animal["id"])
    novo_nome    = _ler_campo_obrigatorio(f"Nome [{animal['nome']}]: ", "Nome", valor_atual=animal["nome"])

    print(f"Espécies aceitas: {', '.join(ESPECIES_VALIDAS)}")
    nova_especie = _ler_opcao_lista(f"Espécie [{animal['especie']}]: ", ESPECIES_VALIDAS, valor_atual=animal["especie"])

    if _animal_duplicado(animais, novo_nome, nova_especie, id_ignorar=id_atual):
        interface.exibir_mensagem_erro("Mudança negada! Conflito de duplicidade com outro animal cadastrado.")
        return

    animal["nome"]          = novo_nome
    animal["especie"]       = nova_especie
    animal["raca"]          = _ler_campo_obrigatorio(f"Raça [{animal['raca']}]: ", "Raça", valor_atual=animal["raca"])
    animal["idade"]         = _ler_idade_validada(f"Idade [{animal['idade']}]: ", valor_atual=animal["idade"])

    print(f"Status clínicos: {', '.join(STATUS_SAUDE_VALIDOS)}")
    animal["saude"]         = _ler_opcao_lista(f"Saúde [{animal['saude']}]: ", STATUS_SAUDE_VALIDOS, valor_atual=animal["saude"])
    animal["data_chegada"]  = _ler_data_validada(f"Chegada [{animal['data_chegada']}]: ", valor_atual=animal["data_chegada"])

    print(f"Comportamentos: {', '.join(COMPORTAMENTOS_VALIDOS)}")
    animal["comportamento"] = _ler_opcao_lista(f"Comportamento [{animal['comportamento']}]: ", COMPORTAMENTOS_VALIDOS, valor_atual=animal["comportamento"])

    try:
        arquivos.salvar_animal(animais)
        interface.exibir_mensagem_sucesso("Registro atualizado com êxito!")
    except Exception as e:
        interface.exibir_mensagem_erro(f"Falha ao salvar alterações: {e}")


def excluir_animal():
    """Remove um animal do sistema mediante confirmação do usuário."""
    interface.limpar_tela()
    interface.exibir_cabecalho("REMOVER ANIMAL DO SISTEMA")

    try:
        animais = arquivos.carregar_animais()
    except Exception as e:
        interface.exibir_mensagem_erro(f"Erro de carregamento: {e}")
        return

    id_busca = input("Digite o ID numérico para exclusão: ").strip()
    if not id_busca.isdigit():
        interface.exibir_mensagem_erro("ID inválido.")
        return

    animal = _buscar_por_id(animais, int(id_busca))
    if not animal:
        interface.exibir_mensagem_erro("Animal não encontrado.")
        return

    _exibir_animal_formatado(animal)
    confirmar = input("\n  Tem certeza que deseja deletar permanentemente este registro? (s/n): ").strip().lower()

    if confirmar == "s":
        animais.remove(animal)
        try:
            arquivos.salvar_animal(animais)
            interface.exibir_mensagem_sucesso("Animal removido com sucesso!")
        except Exception as e:
            interface.exibir_mensagem_erro(f"Erro ao salvar exclusão: {e}")
    else:
        print("\n  Ação cancelada pelo operador.")
        input("\nPressione [Enter] para voltar...")