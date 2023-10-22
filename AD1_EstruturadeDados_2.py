# Questão 2 da AD-1 da disciplina de Estrutura de Dados;
# Implementação em Python de algoritmo recursivo para conversão de base decimal para binária

def calcula_binario(numero):

    # se a divisão inteira do número por 2 for diferente de 0 entra no bloco;
    if numero // 2 != 0:

        # variável auxiliar para guardar a divisão inteira do número por 2;
        auxiliar = numero // 2

        # chamada recursiva da função
        calcula_binario(auxiliar)

        # printa o resto da divisão por 2;
        print(numero % 2)
    else:
        print(numero % 2)


def main():
    n = int(input("Digite um número inteiro: "))
    calcula_binario(n)


main()
