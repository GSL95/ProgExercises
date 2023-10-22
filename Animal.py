# O programa lê três palavras do usuário e define o animal descrito a partir das características

palavra1 = input("Digite a primeira característica: vertebrado ou invertebrado")
palavra2 = input("Digite a segunda característica: classe")
palavra3 = input("Digite a terceira característica: alimentação")

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("águia")
        elif palavra3 == "onivoro":
            print("pomba")
    elif palavra2 == "mamifero":
        if palavra3 == "onivoro":
            print("homem")
        elif palavra3 == "herbivoro":
            print("vaca")
    else:
        print("animal inválido")

elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            print("pulga")
        elif palavra3 == "herbivoro":
            print("lagarta")
    if palavra2 == "anelideo":
        if palavra3 == "hematofago":
            print("sanguessuga")
        elif palavra3 == "onivoro":
            print("minhoca")
    else:
        print("animal inválido")

