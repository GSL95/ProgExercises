# Lê a idade de uma pessoa em dias e mostra em anos, meses e dias

idade = int(input("DIGITE A SUA IDADE EM DIAS: "))
anos = idade // 365
meses = (idade - anos * 365) // 30
dias = idade - anos * 365 - meses * 30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
