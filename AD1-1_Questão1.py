def main():  # Função principal do programa

    quantidade_numeros_lidos = int(input("Quantos números serão avaliados? "))
    numeros = []  # Inicialização de lista vazia.

    if quantidade_numeros_lidos > 0:  # Condição de entrada no programa.

        for i in range(quantidade_numeros_lidos):  # Laço para capturar valores do usuário e guardar em uma lista.

            numero = int(input("Digite um valor: "))  # Variável auxiliar.
            numeros.append(numero)  # Inclusão do número digitado na lista.

        pares = 0      # Inicialização das variáveis
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

        print("Menor:", min(numeros)) #  Mostra na tela o menor número da lista;
        print("Maior:", max(numeros)) #  Mostra na tela o maior número da lista;
        print("Média dos Pares: %.2f" % media_pares) #  Mostra na tela a média dos números pares;
        print("Média dos Ímpares: %.3f" % media_impares) # Mostra na tela a média dos números ímpares.

    else:
        print("O programa precisa de ao menos um número para avaliar.")

main()  # Chamada da função principal.