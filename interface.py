# esse código vai ser sofrido, então eu vou dividir em partes pra eu não ficar maluco da cabeça

from crud_animais import (
    cadastrar_animal,
    listar_animais,
    editar_animal,
    excluir_animal
)

#PRIMEIRA PARTE (pra limpar e deixar bonitinho)
def limpar():
    print("\n" * 10)
def pausar():
    pausa= int (input("Bem vindo a interface do Adoção+! Caso queira continuar, pressione 1, caso contrário, pressione 2: "))
    if pausa==2:
        exit()
    if pausa==1:
        print (menu_geral)
    else:
        print ("Digite apenas UM dos NÚMEROS indicados.")
#PARTE DO MENU GERAL (Basicamente vai ter as escolhas que o usuário vai fazer, enfim.)

def menu_geral():
    
      while True:
         limpar()
         print ("✹"*30)
         print ("SEJA BEM VINDO AO ADOTE+!!!\n\n\n")   
         print("Selecione abaixo a tarefa que você deseja!")
         print ("✹"*30)
        
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
    
    
    