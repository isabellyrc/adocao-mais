from CRUD import (inserir_animal)

def cadastro_animal():
    nome=input ("Digite o nome do animal: ")
    idade=int(input("Digite a idade do animal: "))
    raça=input("Digite a raça do animal: ")
    inserir_animal(nome, idade, raça)

print ("="*30)
print ("Bom dia! Qual ação você deseja executar?")
print ("="*30)
while  True:
    resposta= int(input("1 - Animais\n2 - Tarefas\n3 - Sugestões\n4 - Matching\n0 - Sair\n" ))
    
    if resposta==0:
        break
    elif resposta==1:
        cadastro_animal()
    elif resposta==2:
        print ("Acesso para tarefas")
    elif resposta==3:
        print ("Acesso a sugestões")
    elif resposta==4:
        print ("Acesso a Matching")
    else: 
        print ("Opção invalida, digite uma opção correta.")

    