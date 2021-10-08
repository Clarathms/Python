print("Dados da primeira pessoa:")
n1 = input("Nome: ")
i1 = int(input("Idade: "))

print("Dados da segunda pessoa:")
n2 = input("Nome: ")
i2 = int(input("Idade: "))

im: float
im = (i1 + i2)/2
print(f"A idade media de {n1} e {n2} é de {im:.1f} anos")