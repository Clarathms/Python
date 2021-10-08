soma = 0

print("Digite dois numeros:")
X = int(input("X: "))
Y = int(input("Y: "))

if X < Y:
    t1 = X
    t2 = Y
else:
    t1 = Y
    t2 = X

if t1 % 2 == 0:  # X é par
    for i in range(t1 + 1, t2 - 1, 2):
        soma = soma + i
    print(f"SOMA DOS ÍMPARES: {soma} ")
else:  # X é ímpar
    for i in range(t1 + 2, t2, 2):
        soma = soma + i
    print(f"SOMA DOS ÍMPARES: {soma} ")
