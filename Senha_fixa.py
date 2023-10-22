# Testa uma senha até que seja digitada corretamente

senha = input("Digite sua senha: ")

while senha != "2002":
    print("Senha inválida")
    senha = input("Digite sua senha: ")

print("Acesso permitido")
