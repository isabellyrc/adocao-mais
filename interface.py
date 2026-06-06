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
   menus_tarefas,

)

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

                    elif resposta_menu_animais == "2":
                        listar_animais()
                        pausar()

                    elif resposta_menu_animais == "3":
                        editar_animal()
                        pausar()

                    elif resposta_menu_animais == "4":
                        excluir_animal()
                        pausar()

                    elif resposta_menu_animais == "0":
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
                        especie = input("Espécie (ex:Cach0orro, gato, papagaio, jacaré...)").strip()
                        idade = input("Idade: ").strip()
                        comportamento = input("Comportamento(ex: Calmo, agitado, capeta...)").strip()

                        sugestoes(especie, idade, comportamento)

                    elif resposta_menu_sugestao == 2:
                        listar_animais()
                        input("\n Pressione enter para voltar ao menu anterior.")

                except ValueError:
                    print("Digite um número válido")

            print("✹" * 30)

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

                        opcao_menu_tarefa = input("Escolha uma opcão: ").strip()

                        if opcao_menu_tarefa == "0":
                            break

                        elif opcao_menu_tarefa == "1":
                            cadastrar_tarefa()

                        elif opcao_menu_tarefa == "2":
                            listar_tarefa()

                        elif opcao_menu_tarefa == "3":
                            editar_tarefas()

                        elif opcao_menu_tarefa == "4":
                            excluir_tarefa()

                        elif opcao_menu_tarefa == "5":
                            mostrar_alertas()

                        else:
                            print("opcão invalida!")

        except ValueError:
            print("Digite APENAS NÚMEROS")
            continue

        print("✹" * 30)


    

# Execução do programa
pausar()
        
# Execução do programa
pausar()

#             if resposta==0:
#                 break
#         elif resposta==1:
#             cadastro_animal()
#         elif resposta==2:
#             print ("Acesso para tarefas")
#         elif resposta==3:
#             print ("Acesso a sugestões")
#         elif resposta==4:
#             print ("Acesso a Matching")
#         else: 
#             print ("Opção invalida, digite uma opção correta.")


# def cadastro_animal():
#     nome=input ("Digite o nome do animal: ")
#     idade=int(input("Digite a idade do animal: "))
#     raça=input("Digite a raça do animal: ")
#     (nome, idade, raça)

# print ("="*30)
# print ("Bom dia! Qual ação você deseja executar?")
# print ("="*30)
# while  True:
#     resposta= int(input("1 - Animais\n2 - Tarefas\n3 - Sugestões\n4 - Matching\n0 - Sair\n" ))
    
    
    