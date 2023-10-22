N = int(input("Digite um valor: "))

if N // 100 > 0:
    notas_cem = N // 100
    N = N - (notas_cem * 100)
else:
    notas_cem = 0

if N // 50 > 0:
    notas_cinquenta = N // 50
    N = N - (notas_cinquenta * 50)
else:
    notas_cinquenta = 0

if N // 20 > 0:
    notas_vinte = N // 20
    N = N - (notas_vinte * 20)
else:
    notas_vinte = 0

if N // 10 > 0:
    notas_dez = N // 10
    N = N - (notas_dez * 10)
else:
    notas_dez = 0

if N // 5 > 0:
    notas_cinco = N // 5
    N = N - (notas_cinco * 5)
else:
    notas_cinco = 0

if N // 2 > 0:
    notas_dois = N // 2
    N = N - (notas_dois * 2)
else:
    notas_dois = 0

if N // 1 > 0:
    notas_um = N // 1
    N = N - (notas_um * 1)
else:
    notas_um = 0

print(notas_cem)
print(notas_cinquenta)
print(notas_vinte)
print(notas_dez)
print(notas_cinco)
print(notas_dois)
print(notas_um)
