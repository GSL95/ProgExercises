def main():  # Função principal do programa

    vazio = False  # variável auxiliar;
    numeros = []  # lista vazia

    while not vazio:  # laço que pega números enquanto a linha não é vazia;

        numero = (input("Digite um valor: "))

        if numero == "":  # condição de linha vazia
            vazio = True

        else:
            numeros.append(int(numero))  # adiciona o número na lista convertido pra inteiro;

    pares = 0  # Inicialização das variáveis
    impares = 0
    soma_pares = 0
    soma_impares = 0

    for j in range(len(numeros)):  # Laço para ver se os números da lista são pares ou ímpares.

        if numeros[j] % 2 == 0:  # Condição se o número é par ou ímpar.
            pares += 1
            soma_pares += numeros[j]
        else:
            impares += 1
            soma_impares += numeros[j]

    media_pares = 0
    media_impares = 0

    if pares > 0:  # Condição para evitar divisão por 0.
         media_pares = soma_pares / pares
    if impares > 0:  # Condição para evitar divisão por 0.
        media_impares = soma_impares / impares

    print("Menor:", min(numeros))  # Mostra na tela o menor número da lista.
    print("Maior:", max(numeros))  # Mostra na tela o maior número da lista.
    print("Média dos Pares: %.2f" % media_pares) #  Mostra na tela a média dos números pares;
    print("Média dos Ímpares: %.1f" % media_impares) # Mostra na tela a média dos números ímpares.

main()  # Chamada da função principal.