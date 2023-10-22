# Lê um numero inteiro que dita quantos valores serão pegos do usuário e teste se o valor está no intervalo
# [10, 20]

n = int(input("Digite quantos números serão avaliados"))
contadorIn = 0
contadorOut = 0
numerosAvaliados = []

if n > 0 and n < 10000:
    for i in range(n):
        x = int(input("Digite um número para ser avaliado"))
        if x > -10000000 and x < 10000000:
            numerosAvaliados.append(x)
        else:
            print("Número grande demais ou pequeno demais")
    for j in numerosAvaliados:
        if j >= 10 and j <= 20:
            contadorIn += 1
        else:
            contadorOut += 1
    print(contadorIn, "in")
    print(contadorOut, "out")

else:
    print("Muitos números para avaliar")