# Calcula quantos litros de combustível são necessários para fazer uma viagem a partir da
# tempo gasto e velocida média

autonomia = 12
tempoGasto = int(input("Entre com o tempo da vaigem em horas: "))
velocidade = int(input("Entre com a velocidade média da viagem em km/h: "))

litrosGastos = tempoGasto * velocidade / 12
print("Para esta viagem são necessário: %.3f" % litrosGastos, "litros de combustível")
