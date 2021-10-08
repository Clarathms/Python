N = int(input("Qual é a ordem da matriz? "))
mat: [[int]] = [[0 for x in range(N)] for X in range(N)]

for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}] : "))

print("DIAGONAL PRINCIPAL: ",end='')
for i in range(0, N):
    for j in range(0, N):
        if i == j :
            print(f"{mat[i][j]} ",end='')

neg = 0
for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] < 0:
            neg = neg + 1
print()
print(f"QUANTIDADE DE NEGATIVOS: {neg}")
