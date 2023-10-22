def fibo(valor):
    if valor == 0:
        return 0
    elif valor == 1:
        return 1
    else:
        return fibo(valor - 1) + fibo(valor - 2)

N = int(input("Quantos números: "))
numeros = []

for i in range(N):
    numeros.append(int(input("Forneça um número: ")))

for j in numeros:
    fibonacci = fibo(j)
    print(fibonacci)
