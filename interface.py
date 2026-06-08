# esse código vai ser sofrido, então eu vou dividir em partes pra eu não ficar maluco da cabeça

from crud_animais import (
    cadastrar_animal,
    listar_animais,
    editar_animal,
    excluir_animal,

    _buscar_simples_por_id,
    
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
   limpar_terminal
)
from matching import menu_matching


#prec
# PRIMEIRA PARTE (pra limpar e deixar bonitinho)
limpar_terminal()

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
        
        print("✹" * 30)
        print("ＳＥＪＡ　ＢＥＭ　ＶＩＮＤＯ　ＡＯ　ＡＤＯＴＥ＋!!!\n")
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
            opcao = int (input("Escolha uma opção: "))
            if opcao==1 or opcao==2 or opcao==4:
                limpar_terminal()
            if opcao == 1:

                limpar_terminal()
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
                        input ("Pressione enter para continuar... Só pressione, por favor.")

                    elif resposta_menu_animais == 2:
                        listar_animais()
                        input ("Pressione enter para continuar... Só pressione, por favor.")
                        limpar_terminal()

                    elif resposta_menu_animais == 3:
                        editar_animal()
                        input ("Pressione enter para continuar... Só pressione, por favor.")
                        limpar_terminal()

                    elif resposta_menu_animais == 4:
                        excluir_animal()
                        input ("Pressione enter para continuar... Só pressione, por favor.")
                        limpar_terminal()

                    elif resposta_menu_animais == 0:
                        print("Saindo do sistema... Até logo!")
                        break

                    else:
                        input("Opção inválida! Pressione Enter para tentar novamente...")

                except ValueError:
                    print("Digite APENAS NÚMEROS")

            elif opcao == 2:
                menu_matching()


            elif opcao == 3:
                while True:
                    limpar_terminal()
                    print("✹" * 30)
                    print("BEM VINDO AO MENU DE SUGESTÕES!")
                    print("Abaixo você irá conferir sugestões da nossa equipe obre adoção de pets! \n")
                    print("Porém, para a sugestão funcionar, você precisa saber a espécie, a idade e o comportamento do pet\n")
                    print("Dessa forma, podemos dar uma resposta mais acertiva!!!\n")
                    print(
                    "Você já sabe qual o pet você procura receber a sugestão?\n ")
                    print("1- SIM! (Quero digitar e ver as dicas) ")
                    print("2-NÃO!(Quero ver a lista de animais registrados):")
                    print("3-Voltar ao menu principal ")

                    try:
                        escolha_sugestao = int(input("Escolha uma opção: "))
        
                        if escolha_sugestao == 3:
                            break
                            
                        elif escolha_sugestao == 2:
                            listar_animais()
                            input("\nPressione Enter para continuar...")
                            
                        elif escolha_sugestao == 1:
                            try:
                                resposta_menu_sugestao = int(input("\nDigite o ID do animal para receber a dica: "))
                                animal_retornado = _buscar_simples_por_id(resposta_menu_sugestao)
                                
                                if animal_retornado is None:
                                    print("\nAnimal não encontrado!")
                                    input("Pressione Enter para tentar novamente...")
                                else:
                                    print("\nO animal em questão é:")
                                    print(f"{animal_retornado['nome']}\n")
                                    
                                    sugestoes(animal_retornado["especie"], int(animal_retornado["idade"]), animal_retornado["comportamento"])
                                    
                                    print("✹" * 30)
                                    input("Pressione Enter para continuar e voltar para o Menu de Sugestões...")
                                
                            except ValueError:
                                input(" Digite APENAS NÚMEROS válidos! Pressione Enter para tentar novamente...")
                                
                        else:
                            input("Opção inválida! Pressione Enter para tentar novamente...")
                            
                    except ValueError:
                        input("Digite APENAS NÚMEROS! Pressione Enter para tentar novamente...")

             
            #um salve pro meu mano heitor que fez a parte do painel de tarefas, beijão
            elif opcao == 4:

                print("\n" * 5)
                print("✹" * 30)
                
               
                while True:
                        print("✹" * 30)
                        print("BEM VINDO AO MENU DE TAREFAS! O QUE VOCÊ DESEJA?")
                        print("✹" * 30)
                        print("1 - Cadastrar Tarefa")
                        print("2 - Listar Tarefas")
                        print("3 - Editar Tarefa")
                        print("4 - Excluir Tarefa")
                        print("5 - Mostrar Alertas")
                        print("0 - Sair do menu de tarefas")
                        print("✹" * 30)
                        try:
                            opcao_menu_tarefa = int(input("Escolha uma opcão: ").strip())
                        except ValueError:
                            print ("Digite apenas Números")
                            continue
                        if opcao_menu_tarefa == 0:
                            limpar_terminal()
                            break

                        elif opcao_menu_tarefa == 1:
                            cadastrar_tarefa()
                            input ("Pressione enter para continuar... Só pressione, por favor.")
                            limpar_terminal()

                        elif opcao_menu_tarefa == 2:
                            listar_tarefa()
                            input ("Pressione enter para continuar... Só pressione, por favor.")
                            limpar_terminal()
                        elif opcao_menu_tarefa == 3:
                            editar_tarefas()
                            input ("Pressione enter para continuar... Só pressione, por favor.")
                            limpar_terminal()

                        elif opcao_menu_tarefa ==4:
                            excluir_tarefa()
                            input ("Pressione enter para continuar... Só pressione, por favor.")
                            limpar_terminal()
                        elif opcao_menu_tarefa ==5:
                            mostrar_alertas()
                            input ("Pressione enter para continuar... Só pressione, por favor.")
                            limpar_terminal()
                        else:
                            print("opcão invalida!")
            
            elif opcao==0:
                break
            else:
                print("Opção inválida")

        except ValueError:
            print("Digite APENAS NÚMEROS")
            continue

        print("✹" * 30)


    
# Execução do programa
pausar()
