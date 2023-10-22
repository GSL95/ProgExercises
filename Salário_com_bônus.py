# Lê o nome de um vendedor, seu salário e o total que ele vendeu no mês. Calcula um bônus de 15%
# sobre o vendido e calcula o salário com o bônus

nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário do vendedor: "))
totalVendas = float(input("Digite o total vendido em dinheiro: "))

salarioAtualizado = salario + 15 / 100 * totalVendas

print("O funcionário", nome, "receberá este mês: R$ %.2f" % salarioAtualizado)
