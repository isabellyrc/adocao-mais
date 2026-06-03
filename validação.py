from datetime import datetime

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

# teste de validaçoes 

# nome = input("nome do animal: ")
# especie = input("especie do animal: ")
# idade = (input("idade do animal: "))
# comportmento = input("comportamneto do animal: ")
# data = input("digita a data (dd/mm/aaaa): ")

# if validar_texto(nome):
#     print(nome)

# else:
#     print("nome invalido")

# if validar_especie(especie):
#     print(especie)

# else:
#     print("especie invalida")

# if validar_idade(idade):
#     print(idade)

# else:
#     print("idade invalida")

# if validar_comportamento(comportmento):
#     print(comportmento)

# else:
#     print("comportamento invalido")

# if validar_data(data):
#     print(data)

# else:
#     print("data invalida")