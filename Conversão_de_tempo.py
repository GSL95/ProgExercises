# Transforma um tempo em segundos para horas, minutos e segundos

tempo = int(input("Digite o tempo do processo em segundos: "))
horas = tempo // 3600
minutos = (tempo - horas * 3600) // 60
segundos = (tempo - (horas * 3600) - (minutos * 60))

print(horas, ":", minutos, ":", segundos)
