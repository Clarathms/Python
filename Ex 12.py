#Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
#teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
#que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
#que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
#pela soma dos pesos.

N = int(input("Quantos casos serão digitados? "))

for i in range (0,N):
    print("Digite três números:")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    media = (2*(n1) + 3*(n2) + 5*(n3)) / 10
    print(f"MEDIA = {media:.1f}")
