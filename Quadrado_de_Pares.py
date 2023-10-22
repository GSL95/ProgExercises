N = int(input("Digite o número de números: "))
pares = []

if N > 5 and N < 2000:
    for i in range(1,N+1):
        if i % 2 == 0:
            pares.append(i)

    for j in pares:
        print(j, "^", "2 = ", j**2)

else:
    print("número fora do intervalo")