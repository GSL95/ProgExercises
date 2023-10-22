notas = []

while len(notas) != 2:
    nota = float(input("Digite uma nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida")

media = (notas[0] + notas[1]) / 2
print("média = %.2f" %media)