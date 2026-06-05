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
        
    animal_selecionado = None
    for animal_atual in animais:

        if animal_selecionado in (animal_atual.get["id"]) == int(id_animal): #comparando ID do animal
            animal_selecionado = animal_atual
            break

    if animal_selecionado is None:
        print("Animal não encontrado")
        return
        
    print(f"Animal selecionado: {animal_selecionado['nome']}" )

    
    print(f"Tipos disponiveis: {','.join(TIPOS_VALIDOS)}")

    tipo = input("Tipo da tarefa: ").strip().lower()

    if tipo not in TIPOS_VALIDOS:
        print("Erro: tipo inválido")
        return
    
    data = input("Data prevista (DD/MM/AAAA): ").strip()
    try:
        data_prevista = datetime.strptime(data,"%d/%m/%Y" ).date()
    except ValueError: #esse ValueErro acontece pois o strptime converte em uma data real
        print("Erro: data inválida. Use DD/MM/AAAA.")
        return
    
    tarefas = arquivos.carregar_tarefas()
    tarefa_id = len(tarefas) + 1
    
    tarefa = {
        "id": tarefa_id,
        "id_animal": animal_selecionado["id"],
        "animal": animal_selecionado["nome"],
        "tipo": tipo,
        "data": data,
        "concluida": "nao"
    }

    tarefas.append(tarefa)
    arquivos.salvar_tarefas(tarefas)
    print(f"Tarefa '{tipo}' para {animal_selecionado['nome']} cadastrada com sucesso! ")

def listar_tarefa():
    limpar_terminal()

    tarefas = arquivos.carregar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("--- Lista de Tarefas --- ")

    for tarefas_atual in tarefas:

        data_prevista = datetime.strptime(tarefas_atual["data"], "%d/%m/%Y").date()
        dias = (data_prevista - date.today()).days

        if tarefas_atual["concluida"] == "sim":
            status = "Concluída"

        else:
            status = "Pendente"

        print(f"\nID: {tarefas_atual['id']} | Animal{tarefas_atual['animal']} | Tipo: {tarefas_atual['tipo']}")
        print(f"Data: {tarefas_atual['data']} | Dias restantes: {dias} | Status {status} ")

def editar_tarefas():
    limpar_terminal()
    listar_tarefa()

    tarefa_id = input("\n ID da tarefa pra editar: ").strip()
    tarefas = arquivos.carregar_tarefas()

    tarefa = None
    for tarefa_atual in tarefas:
        if tarefa_atual["id"] == tarefa_id:
            tarefa = tarefa_atual
            break

    if tarefa is None:
        print("Tarefa não encontrada")
        return
        
    nova_data = input(f"Nova data [{tarefa['data']}]: ").strip()

    if nova_data:
        try:
            datetime.strptime(nova_data, "%d/%m/%Y")
            tarefa["data"] = nova_data
        except ValueError:
            print("Data inválida. Nada foi Alterado")
            return
        
    print(f"Tipos disponiveis: {','.join(TIPOS_VALIDOS)}")
    novo_tipo = input(f"Novo tipo [{tarefa['tipo']}]: ").strip().lower()

    if novo_tipo in TIPOS_VALIDOS:
        tarefa["tipo"] = novo_tipo
    elif novo_tipo:
        print("tipo inválido. Mantemos o anterior")

    concluida = input(f"Concluida? sim/nao [{tarefa['concluida']}]: ").strip().lower()

    if concluida in ["sim", "nao"]: 
        tarefa["concluida"] = concluida 

    arquivos.salvar_tarefas(tarefas)
    print("Tarefa atualizada!")
            
def excluir_tarefa():
    limpar_terminal()
    listar_tarefa()

    tarefa_id = 

def mostrar_alertas():
    pass

def testar_datas():
    pass
