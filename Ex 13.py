M = int(input("Qual a qtd de linhas da matriz (até 10) ? "))
N = int(input("Qual a qtd de colunas da matriz (até 10) ? "))

mat: [[float]] = [[0 for x in range(N)] for y in range(M)]
vet: [float] = [0 for y in range(M)]

for i in range(0, M):
    print(f"Digite os elementos da {i + 1}ª linha:")
    for j in range(0, N):
        mat[i][j] = float(input())
        vet[i] = vet[i]+mat[i][j]

print("VETOR GERADO:")
for i in range(0, M):
    print(f"{vet[i]:.1f}")