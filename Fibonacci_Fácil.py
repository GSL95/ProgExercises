N = int(input("Digite os N números do Fibo: "))
fibonacci = [0, 1]

if N < 46 and N > 0:
    for i in range(N-2):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    print(fibonacci)
else:
    print("N fora do intervalo")
