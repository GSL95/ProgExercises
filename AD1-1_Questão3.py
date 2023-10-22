def main():  # Função principal do programa

    numeros = input("Digite os números: ").split()
    numeros_lista = []  # lista vazia

    for i in range(len(numeros)):  # laço para pegar os valores da linha, converter pra inteiro e guardar na lista dos números
        numeros_lista.append(int(numeros[i]))

    pares = 0  # Inicialização das variáveis
    impares = 0
    soma_pares = 0
    soma_impares = 0

    for j in range(len(numeros_lista)):  # Laço para ver se os números da lista são pares ou ímpares.

        if numeros_lista[j] % 2 == 0:  # Condição se o número é par ou ímpar.
            pares += 1
            soma_pares += numeros_lista[j]
        else:
            impares += 1
            soma_impares += numeros_lista[j]

    media_pares = 0
    media_impares = 0

    if pares > 0:  # Condição para evitar divisão por 0.
         media_pares = soma_pares / pares
    if impares > 0:  # Condição para evitar divisão por 0.
        media_impares = soma_impares / impares

    print("Menor:", min(numeros_lista))  # Mostra na tela o menor número da lista.
    print("Maior:", max(numeros_lista))  # Mostra na tela o maior número da lista.
    print("Média dos Pares: %.1f" % media_pares)  #  Mostra na tela a média dos números pares;
    print("Média dos Ímpares: %.1f" % media_impares)  # Mostra na tela a média dos números ímpares.

main()  # Chamada da função principal.