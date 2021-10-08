# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
# seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada.
soma = 0

N = int(input("Qual é a ordem da matriz? "))
mat: [[float]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

# SOMA POSITIVOS
for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print()
print(f"SOMA DOS POSITIVOS: {soma:.1f}")

# LINHA
print()
print()
L = int(input("Escolha uma linha: "))
print("LINHA ESCOLHIDA: ", end='')
for j in range(0, N):
    for i in range(0, N):
        print(f"{mat[L][j]:.1f} ", end='')
        break

# COLUNA
print()
print()
C = int(input("Escolha uma coluna: "))
print("COLUNA ESCOLHIDA: ", end='')

for i in range(0, N):
    for j in range(0, N):
        print(f"{mat[i][C]:.1f} ", end='')
        break

# DIAG PRINCIPAL
print()
print()
print(f"DIAGONAL PRINCIPAL: ", end='')
for i in range(0, N):
    for j in range(0, N):
        print(f"{mat[i][i]:.1f} ", end='')
        break

# MATRIZ ALTERADA
print()
print()
print("MATRIZ ALTERADA:")
for i in range(0, N):
    print()
    for j in range(0, N):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] ** 2

        print(f"{mat[i][j]:.1f} ", end='')
