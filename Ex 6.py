soma = 0
N = int(input("Quantos números você vai digitar? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

print()
print(f"VALORES: ",end='')
for i in range(0, N):
    print(f"{vet[i]} ",end='')

print()
for i in range(0, N):
    soma = soma + vet[i]
print(f"SOMA: {soma:.2f}")

media = soma / N
print(f"MEDIA: {media:.2f} ")
