#  Dados quatro tamanhos de varetas fornecidos pelo usuário, o programa deve dizer
#  se é possível formar algum triângulo com as quatro varetas

def main():
    tamanho_varetas = input("Entre com o tamanho das varetas: ").split()
    varetas = []

    for i in range(len(tamanho_varetas)):

        varetas.append(int(tamanho_varetas[i]))
        if varetas[i] < 0:
            print("Não existe tamanho negativo")
            varetas[i] = 0

    if len(varetas) > 4:
        print("Varetas demais, máximo de quatro")
    else:
        a = varetas[0]
        b = varetas[1]
        c = varetas[2]
        d = varetas[3]

        if a + b > c and a + c > b and b + c > a:  #  Triângulo a, b, c
            print("S")
        elif a + b > d and a + d > b and b + d > a:  #  Triângulo a, b, d
            print("S")
        elif a + c > d and a + d > c and d + c > a:  #  Triângulo a, c, d
            print("S")
        elif b + c > d and b + d > c and c + d > b:  # Triângulo b, c, d
            print("S")
        else:
            print("N")


main()