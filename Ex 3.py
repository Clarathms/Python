
n1 = int(input("Primeiro valor: "))
n2 = int(input("segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 < n2 and n1 < n3:
    nr = n1
elif n2 < n3:
    nr = n2
else:
    nr = n3

print(f"MENOR = {nr}")