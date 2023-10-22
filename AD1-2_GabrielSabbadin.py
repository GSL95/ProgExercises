# AD1-2 da disciplina de Fundamentos da Programação semestre 2023.2
# Aluno: Gabriel Sabbadin

# função que pega a permutação do usuário e armazena em um vetor de inteiros
def lerPermutacao():
    permutacao = input("Digite a permutação: ").split()
    permutacao_int = []
    
    for i in range(len(permutacao)):
        permutacao_int.append(int(permutacao[i]))
    return permutacao_int
        
# função principal do programa (não consegui criar a lógica pra solucionar o problema)
def main():
    permutacao_usuario = lerPermutacao()
    ciclos = []
    ciclo_algebrico = []
    n = len(permutacao_usuario)
    
    while n > 0:
        ciclo_algebrico.append(min(permutacao_usuario))
        
        for j in ciclo_algebrico:
            if ciclo_algebrico[0] != permutacao_usuario[j+1]:
                ciclo_algebrico.append(permutacao_usuario[ciclo_algebrico[j+1]])

                for k in range(len(ciclo_algebrico)):
                    if ciclo_algebrico[k] in permutacao_usuario:
                        permutacao_usuario.remove(ciclo_algebrico[k])
                
            else:
                ciclos.append(ciclo_algebrico)
                
                ciclo_algebrico.clear()
                
        n = len(permutacao_usuario)

    print(ciclos)
    
main()