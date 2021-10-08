#Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
#Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
#se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
#apenas NULO.

N = int(input("Quantos números serão digitados? "))

for i in range (0,N):
    x = int(input("Digite um número: "))

    if x % 2 != 0 :
        print("ÍMPAR ",end='')
    elif x == 0:
        print("")
    else:
        print("PAR ",end='')

    if x > 0 :
        print("POSITIVO")
    elif x == 0:
        print("NULO")
    else:
        print("NEGATIVO")
