from datetime import datetime, date
import os

tarefas = [] #substituir por aquivos.py de heitor

TIPOS_VALIDOS = ["vacinas", "banho", "consulta", "treino"]

def limpar_terminal(): 
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_tarefa():
    
    print(" --- Cadastrar tarefa --- ")

    nome_animal = input("Digite o nome do animal: ").strip()
    if not nome_animal: 
        print("Nome não pode estar vazio! ")
        return
    
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
    
    tarefa = {
        "id": len(tarefas) + 1,
        "animal": nome_animal,
        "tipo": tipo,
        "data": data_prevista,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{tipo}' para {nome_animal} cadastrada com sucesso! ")

def editar_tarefa():
    pass

def excluir_tarefa():
    pass

def calcular_prazo():
    pass

def mostrar_alertas():
    pass

def testar_datas():
    pass
