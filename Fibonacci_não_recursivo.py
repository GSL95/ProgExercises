fibo = []

fibo.append(1)
fibo.append(1)

n = int(input("digite qual elemento de fibonacci quer saber: "))

for i in range(2,n):
    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[n-1])