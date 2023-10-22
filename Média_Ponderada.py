nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 >= 0 and nota1 <= 10 and nota2 >=0 and nota2 <= 10:
    media = ((nota1 * 3.5) + (nota2 * 7.5)) / 11
    print("%.5f" %media)
else:
    print("Notas fora do intervalo 0 a 10")