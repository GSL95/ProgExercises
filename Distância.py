# Calcula quanto tempo leva um carro X a 90km/h se afastar de um carro Y a 60km/h, uma distância
# fornecida pelo usuário

velResultante = 90 - 60
distancia = int(input("Digite a distancia entre os carros: "))

tempo = int(distancia / velResultante * 60)

print("Levará:", tempo, "minutos para os carros estarem a essa distância entre si")
