# Lê o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse
# funcionário

numeroFuncionario = int(input("Digite o número do funcionário: "))
numeroHoras = int(input("Digite o número de horas trabalhadas: "))
valorHora = float(input("Digite o valor por hora: "))

salario = numeroHoras * valorHora

print("O funcionário de numero ", numeroFuncionario)
print("Recebeu: R$ %.2f" % salario)
