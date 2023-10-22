N = int(input("Digite o número de números que serão lidos: "))
numeros = []

for i in range(N):
    x = int(input("Digite um valor: "))
    numeros.append(x)

for j in range(len(numeros)):
    if numeros[j] % 2 == 0:
        print("EVEN")
        if numeros[j] > 0:
            print("POSITIVE")
        elif numeros[j] < 0:
            print("NEGATIVE")
        else:
            print("NULL")
    else:
        print("ODD")
        if numeros[j] > 0:
            print("POSITIVE")
        elif numeros[j] < 0:
            print("NEGATIVE")
        else:
            print("NULL")

