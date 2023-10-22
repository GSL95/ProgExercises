def lerPontos():
    vazio = False
    pontos = []
    ponto = input("digite um ponto: ").split()

    if ponto == ['0', '0']:
        print("Não existem pontos")
    else:
        ponto_float = [float(i) for i in ponto]
        pontos.append(ponto_float)

        while not vazio:

            ponto = (input("Digite um ponto: ").split())
            
            if ponto == ['0','0']:
                vazio = True

            else:
                ponto_float = [float(j) for j in ponto]
                pontos.append(ponto_float)
        return pontos

def pontoMedio(matriz):
    somaX = 0
    somaY = 0

    for i in range(len(matriz)):
        somaX += matriz[i][0]
    for j in range(len(matriz)):
        somaY += matriz[j][1]
    mediaX = somaX / len(matriz)
    mediaY = somaY / len(matriz)

    ponto_medio = [mediaX, mediaY]

    return ponto_medio
    

def main():
    pontos = lerPontos()
    medio = pontoMedio(pontos)
    print(medio[0], medio[1])

main()