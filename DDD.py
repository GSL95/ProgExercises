# Lê um numero que representa um DDD e informa ao usuário a cidade a qual o DDD se refere, considerando a tabela

ddd = int(input("Digite o DDD da cidade: "))

if ddd == 61:
    print("Brasília")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("São Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitória")
elif ddd == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")
