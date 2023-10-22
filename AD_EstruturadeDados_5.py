# Questão 5 da AD-1 da disciplina de Estrutura de Dados implementada em Python

# Dadas v1 e v2 duas listas ordenadas, encontrar v3 tal que v3 = v1 - v2

# Função de busca binária para tirar de v3 os elementos de v2:
def busca_binaria(lista, x):
    n = len(lista)
    inicio = 0
    fim = n - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2

        if x == lista[meio]:  # achou x
            return True
        elif x < lista[meio]:  # x pode estar na primeira metade da sequência
            fim = meio - 1
        else:
            inicio = meio + 1  # x pode estar na segunda metade da sequência

    return False

def main():
    # Inicialização das listas:
    v1 = []
    v2 = []
    v3 = []

    # Declarando 'm' como o tamanho de v1 e 'n' como o tamanho de v2:
    m = len(v1)
    n = len(v2)

    # Colocando os elementos de v1 em v3:
    for i in range(m):
        v3.append(v1[i])
    
    # Retirando de v3 os elementos que existem em v2:
    for j in range(n):
        if busca_binaria(v3, v2[j]):
            v3.remove(v2[j])

    print("v3 = ", v3)

main()

# O número de passos do algoritmo é (m + n), logo sua complexidade é O(m+n).

    