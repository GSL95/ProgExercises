def lerVotos():
    votos = []
    x = 0
    while x != "":
        x = input("Digite o candidato votado: ")
        if x != "":
            votos.append(x)
    return votos

def contagemVotos(votos):
    vetor_quantidade = []
    for i in range(len(votos)):
        quantos_votos = votos.count(votos[i])
        vetor_quantidade.append(quantos_votos)
    return vetor_quantidade

def main():
    votos = lerVotos()
    quantidade = contagemVotos(votos)
    print(votos, quantidade)

main()