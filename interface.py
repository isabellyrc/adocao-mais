# esse código vai ser sofrido, então eu vou dividir em partes pra eu não ficar maluco da cabeça

from crud_animais import (
    cadastrar_animal,
    listar_animais,
    editar_animal,
    excluir_animal,
    _idade_valida,
    _animal_duplicado,
)
from sugestoes import(
    sugestoes,
)
from tarefas import(
   cadastrar_tarefa,
   listar_tarefa,
   editar_tarefas,
   excluir_tarefa,
   mostrar_alertas,
)
from validação import (
    validar_idade, 
    validar_especie, 
    validar_comportamento)
from datetime import datetime

#precisei colocar o validações aqui para dar adiantamento para o código
#contudo, quem fez as validações foi Maria Carolina, Vulgo Carol, vulgo doida de Olinda
#um Salve pra Carol

def validar_idade(idade):
    try:
        idade = int(idade) 

        if idade <= 0:
            print("idade abaixo de 0")
            return False
        
        elif idade > 30:
            print("idade muito alta")
            return False
        
        else:
            return True
        
    except:
        print("idade invalida")
        return False

    
def validar_especie(especie):
    especies =["cachorro", "gato", "outro"]

    return especie.lower() in especies

def validar_comportamento(comportamento):
    comportamentos = ["calmo", "agitado", "agresivo", "carinhoso", "outro"]

    return comportamento.lower() in comportamentos 

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except:
        return False

def validar_texto(texto):
    return texto.strip() != ""


# PRIMEIRA PARTE (pra limpar e deixar bonitinho)
def limpar():
    print("\n" * 10)

def pausar():
    while True:
        try: #tente, puxar esses ifs e elifs e else lol
            pausa = int(input("Bem vindo a interface do Adoção+! Caso queira continuar, pressione 1, caso contrário, pressione 2: "))
            if pausa == 2:
                print("Saindo... Até logo!")
                exit()
            elif pausa == 1:
                menu_geral()
                break
            else:
                print("Digite apenas UM dos NÚMEROS indicados.\n")
        except ValueError: #caso o usuário BURRO digite alguma LETRA
            print("Por favor, digite um número válido (1 ou 2).\n")

# PARTE DO MENU GERAL
def menu_geral():
    while True:
        limpar()
        print("✹" * 30)
        print("SEJA BEM VINDO AO ADOTE+!!!\n")
        print("Este é o menu principal.\n")
        print("Selecione abaixo o menu que você deseja acessar! ")
        print("✹" * 30)

        print("1 - Acessar o menu de Animais")
        print("2 - Acessar o menu de Matching")
        print("3 - Acessar o menu de Sugestões")
        print("4 - Acessar o menu de Tarefas")
        print("0 - Sair")
        print("✹" * 30)

        try:
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n" * 5)
                print("✹" * 30)
                print("BEM VINDO AO MENU DE ANIMAIS! O QUE VOCÊ DESEJA?")
                print("✹" * 30)
                print("1- Registrar Animal")
                print("2- Verificar a Lista de Animais Registrados")
                print("3- Editar Animais Registrados")
                print("4- Excluir Animal Registrado")
                print("0- Sair do menu")
                print("✹" * 30)

                try:
                    resposta_menu_animais = int(input("Digite sua resposta: "))

                    if resposta_menu_animais == 1:
                        cadastrar_animal()
                        pausar()

                    elif resposta_menu_animais == 2:
                        listar_animais()
                        pausar()

                    elif resposta_menu_animais == 3:
                        editar_animal()
                        pausar()

                    elif resposta_menu_animais == 4:
                        excluir_animal()
                        pausar()

                    elif resposta_menu_animais == 0:
                        print("Saindo do sistema... Até logo!")
                        break

                    else:
                        input("Opção inválida! Pressione Enter para tentar novamente...")

                except ValueError:
                    print("Digite APENAS NÚMEROS")

            if opcao == "2":
                print("\n" * 5)
                print("✹" * 30)
                print("BEM VINDO AO SISTEMA DE MATCHING! O QUE VOCÊ DESEJA?")
                print("✹" * 30)

            if opcao == "3":
                print("\n" * 5)
                print("✹" * 30)
                print("BEM VINDO AO MENU DE SUGESTÕES!")
                print("Abaixo você irá conferir sugestões da nossa equipe obre adoção de pets! \n\n\n")
                print("Porém, para a sugestão funcionar, você precisa saber a espécie, a idade e o comportamento do pet")
                print("Dessa forma, podemos dar uma resposta mais acertiva!!!")
                print(
                    "Você já sabe qual o pet você procura receber a sugestão? "
                    "1- SIM! (Quero digitar e ver as dicas) 2-NÃO!(Quero ver a lista de animais registrados): "
                )
                

                try:
                    resposta_menu_sugestao = int(input("Digite sua resposta"))

                    if resposta_menu_sugestao == 1:
                        print("Bacana! Agora, conta um pouco mais sobre o pet:")
                        while True:
                            especie = input("Espécie (ex:Cach0orro, gato, papagaio, jacaré...)").strip()
                            if validar_especie(especie):
                                break
                        while True:   
                            idade = input("Idade: ").strip()
                            if validar_idade(idade):
                                break
                        while True:
                            comportamento = input("Comportamento(ex: Calmo, agitado, capeta...)").strip()
                            if validar_comportamento(comportamento):
                                break
                        
                        sugestoes(especie, idade, comportamento)
                        input ("Pressione enter para continuar... Só pressione, por favor.")

                    elif resposta_menu_sugestao == 2:
                        listar_animais()
                        input("\n Pressione enter para voltar ao menu anterior.")

                except ValueError:
                    print("Digite um número válido")

            print("✹" * 30)
            #um salve pro meu mano heitor que fez a parte do painel de tarefas, beijão
            if opcao == "4":

                print("\n" * 5)
                print("✹" * 30)
                
                def menus_tarefas():

                    while True:
                        print("\n--- Tarefas ---")
                        print("1 - Cadastrar")
                        print("2 - Listar")
                        print("3 - Editar")
                        print("4 - Excluir")
                        print("5 - Alertas")
                        print("0 - sair")

                        opcao_menu_tarefa = int(input("Escolha uma opcão: ")).strip()

                        if opcao_menu_tarefa == 0:
                            break

                        elif opcao_menu_tarefa == 1:
                            cadastrar_tarefa()

                        elif opcao_menu_tarefa == 2:
                            listar_tarefa()

                        elif opcao_menu_tarefa == 3:
                            editar_tarefas()

                        elif opcao_menu_tarefa ==4:
                            excluir_tarefa()

                        elif opcao_menu_tarefa ==5:
                            mostrar_alertas()

                        else:
                            print("opcão invalida!")
            

        except ValueError:
            print("Digite APENAS NÚMEROS")
            continue

        print("✹" * 30)


    
# Execução do programa
pausar()
