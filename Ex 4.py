print("Digite dois numeros:")
n1 = int(input())
n2 = int(input())

while n1 != n2 :
    if n1 < n2 :
        print("CRESCENTE!")
    else:
        print("DECRESCENTE!")

    print("Digite outros dois numeros:")
    n1 = int(input())
    n2 = int(input())