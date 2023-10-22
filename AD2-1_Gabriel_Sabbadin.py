# AD2-1 Fundamentos de programação

# métodos
def leituraDeMatriz():
    matriz = []
    linha = (input("Digite uma linha: ").split())

    while linha != []:
        matriz.append(linha)
        linha = (input("Digite uma linha ").split())
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])

    return matriz


def mostraMatriz(texto, matriz):
    print(texto)
    if matriz != []:
        for i in range(len(matriz)):
                print(matriz[i])
    else:
         print("inexistente!")



def somaMatrizes(matrizA, matrizB):
     matrizSoma = []
     if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]):         
        for i in range(len(matrizA)):
               matrizSoma.append([])
               for j in range(len(matrizA[0])):
                    matrizSoma[i].append(matrizA[i][j] + matrizB[i][j])

        return matrizSoma
     else:
        return matrizSoma
     
def multiplicaMatrizes(matrizA, matrizB):
     matrizMultiplicada = []
     if len(matrizA) == len(matrizB[0]):
        for i in range(len(matrizA)):
            matrizMultiplicada.append([]) 
            for j in range(len(matrizB[0])):
                matrizMultiplicada[i].append(0) 
                for k in range(len(matrizA[0])): 
                    matrizMultiplicada[i][j] += matrizA[i][k] * matrizB[k][j]
        return matrizMultiplicada
     else:
         return matrizMultiplicada
        
                         
# Principal
def main():
    valoresA = leituraDeMatriz()
    valoresB = leituraDeMatriz()
    mostraMatriz("Matriz A", valoresA)
    mostraMatriz("Matriz B", valoresB)
    valoresSoma = somaMatrizes(valoresA, valoresB)
    valoresMult = multiplicaMatrizes(valoresA, valoresB)
    mostraMatriz("Matriz Soma de A com B", valoresSoma)
    mostraMatriz("Matriz Multiplicação de A por B", valoresMult)


main()
