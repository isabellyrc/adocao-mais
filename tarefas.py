from datetime import datetime, date
import arquivos
import os

tarefas = [] #substituir por aquivos.py de heitor

TIPOS_VALIDOS = ["vacinas", "banho", "consulta", "treino"]

def limpar_terminal(): 
    os.system("cls" if os.name == "nt" else "clear")



def cadastrar_tarefa():

    limpar_terminal()
    
    animais = arquivos.carregar_animais()
    if not animais:
        print("Nenhum animal cadastrado!. Cadastre um animal primeiro.")
        return
    

    print("\n --- Cadastrar tarefa --- ")

    print("Animais disponiveis: ")
    for animal_atual in animais:
        print(f" ID {animal_atual['id']} - {animal_atual['nome']} ({animal_atual['especie']})")

    id_animal = input("\n ID do animal: ").strip()
        
    if not id_animal:
        print("Erro: ID inválido")
        return
        
    animal_selecionado = None
    for animal_atual in animais:

        if animal_selecionado in (animal_atual.get("id", -1)) == int(id_animal): #comparando ID do animal
            animal_selecionado = animal_atual
            break

    if not animal_selecionado:
        print("Animal não encontrado")
        return
        
    print(f"Animal selecionado: {animal_selecionado['nome']}" )

    
    print(f"Tipos disponiveis: {','.join(TIPOS_VALIDOS)}")

    tipo = input("Tipo da tarefa: ").strip().lower()

    if tipo not in TIPOS_VALIDOS:
        print("Erro: tipo inválido")
        return
    
    data_str = input("Data prevista (DD/MM/AAAA): ").strip()
    try:
        data_prevista = datetime.strptime(data_str,"%d/%m/%y" ).date()
    except ValueError: #esse ValueErro acontece pois o strptime converte em uma data real
        print("Erro: data inválida. Use DD/MM/AAAA.")
        return
    
    tarefas = arquivos.carregar_tarefas()
    
    tarefa = {
        "id": _gerar_id(tarefa),
        "id_animal": animal_selecionado["id"],
        "animal": animal_selecionado["nome"],
        "tipo": tipo,
        "data": data_prevista,
        "concluida": "não" or "sim"
    }

    tarefas.append(tarefa)
    arquivos.salvar_tarefas(tarefas)
    print(f"Tarefa '{tipo}' para {animal_selecionado} cadastrada com sucesso! ")

def listar_tarefa():
    limpar_terminal()

    tarefas = arquivos.carregar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("--- Lista de Tarefas --- ")

    for tarefas_atual in tarefas:
        dias = _calcular_dias_restantes(tarefas_atual['data'])

        if tarefas_atual["concluida"] == "sim":
            status = "Concluída"

        else:
            status = "Pendente"

def excluir_tarefa():
    pass

def calcular_prazo():
    pass

def mostrar_alertas():
    pass

def testar_datas():
    pass
