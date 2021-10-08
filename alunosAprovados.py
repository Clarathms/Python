# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis).

N = int(input("Quantos alunos serão digitados? "))
nome: [str] = [0 for x in range(N)]
n1: [float] = [0 for x in range(N)]
n2: [float] = [0 for x in range(N)]
media: [float] = [0 for x in range(N)]

for i in range(0, N):
    print(f"Digite nome, primeira e segunda nota do {i + 1}° aluno:")
    nome[i] = input()
    n1[i] = float(input())
    n2[i] = float(input())

print("Alunos aprovados:")
for i in range(0, N):
    media[i] = (n1[i] + n2[i]) / 2
    if media[i] >= 6:
        print(nome[i])
