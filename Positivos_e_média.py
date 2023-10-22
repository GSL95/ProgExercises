# Lê seis valores, diz quantos são positivos e calcula a média entre eles

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite um valor: "))
num3 = float(input("Digite um valor: "))
num4 = float(input("Digite um valor: "))
num5 = float(input("Digite um valor: "))
num6 = float(input("Digite um valor: "))

lista = [num1, num2, num3, num4, num5, num6]
contador = 0
soma = 0

for i in lista:
    if i > 0:
        contador += 1
        soma += i
media = soma / contador

print(contador, "valores positivos")
print("%.1f" % media)
