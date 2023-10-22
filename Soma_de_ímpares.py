X = int(input("Número: "))
Y = int(input("Número: "))
somaImpares = 0

for i in range(X,Y -1):
    if i % 2 != 0:

        somaImpares += i

print(somaImpares)