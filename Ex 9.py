#Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
#se for o caso.

X = int(input("Digite o valor de X: "))

for i in range(0,X+1) :
    if i%2 != 0:
        print(i)