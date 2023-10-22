# Calcula o consumo médio de um automóvel a partir da distância percorrida e o combustível gasto

distancia = int(input("Digite a distância percorrida: "))
combustivelGasto = float(input("Digite quantos litros de combustível foi gasto: "))

consumoMedio = distancia / combustivelGasto

print("O consumo médio foi: %.3f" % consumoMedio, "km/l")
