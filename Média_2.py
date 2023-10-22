# Recebe três valores, calcula a média e exibe com precisao de uma casa.

A = float(input("Forneça a primeira nota: "))
B = float(input("Forneça a segunda nota: "))
C = float(input("Forneça a terceira nota: "))
MEDIA = (A * 2 + B * 3 + C * 5) / 10

if A > 10 or B > 10 or C > 10:
    print("Notas inválidas, nota máxima é 10")
else:
    print("Sua média é: %.1f" % MEDIA)
