vazio = False
counter = 0
numeros_int = []
soma_maiores = 0

while not vazio:
    numeros = input().split()

    if numeros == []:
      
        print("linha vazia")
        vazio = True
    else:
        for i in range(len(numeros)):
            numeros_int.append(int(numeros[i]))

        maior = numeros_int[0]
        for j in range(1, len(numeros_int)):
            if maior < numeros_int[j]:
                maior = numeros_int[j]
        soma_maiores += maior
        print("Maior: ", maior)
        counter +=1

media_maiores = soma_maiores / counter
print("Média %.1f " %media_maiores)
