X = int(input("Digite um valor: "))
Y = int(input("Digite um valor: "))

for i in range(X,Y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)