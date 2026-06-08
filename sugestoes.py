def sugestoes(especie, idade, compormamento):
    if idade <= 1 :
        print("filhote: necessita de mais atenção")

    elif idade >= 8:
        print("idoso: necessita de consultas frequentes ")

    if compormamento.lower() == "carinhoso":
        print("ideal para familias com crianças")

    elif compormamento.lower() == "calmo":
        print("ideal para morar em apartamento")

    elif compormamento.lower() == "agitado":
        print("ideal para casa com quintal")

    elif compormamento.lower() == "agressivo":
        print("necessita de treinamento comportamental")

    if especie.lower() == "cachorro":
        print("necessita de passeios diarios")

    elif especie.lower() == "gato":
        print("necessita de brinquedos e arranhadores")