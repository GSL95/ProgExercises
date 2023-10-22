# Calcula o volume de uma esfera a partir do seu raio, mostra na tela a saída com três casas decimais

pi = 3.14159
print("vamos calcular o volume de uma esfera!")
raio = float(input("Digite o raio da esfera: "))

volume = 4.0/3 * pi * raio ** 3
print("O volume da esfera é %.3f" % volume)
