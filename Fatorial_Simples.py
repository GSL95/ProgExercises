N = int(input("Qual número calculará o fatorial: "))
fatorial = 1

while N > 0:
    fatorial = fatorial * N
    N -= 1


print(fatorial)