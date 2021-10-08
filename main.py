#Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
#organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
#quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
#laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
#informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
#utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
#valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
#inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
#de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
#cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
#percentual deve ser apresentado com dois dígitos após o ponto.

tGeral = 0
tc = 0
ts = 0
tr = 0

N = int(input("Quantos casos serão digitados? "))

for i in range (0,N):
    qtd = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia (C - coelho, R - rato, s - sapo): ")

    tGeral = tGeral + qtd

    if tipo == "C":
        tc = tc + qtd
    elif tipo == "R":
        tr = tr + qtd
    else:
        ts = ts + qtd

pC = (tc * 100)/tGeral
ps = (ts * 100)/tGeral
pR = (tr * 100)/tGeral

print()
print("RELATÓRIO FINAL:")
print(f"Total: {tGeral} cobaias")
print(f"Total de coelhos: {tc}")
print(f"Total de ratos: {tr}")
print(f"Total de sapos: {ts}")
print(f"Percentual de coelhos: {pC:.2f}")
print(f"Percentual de ratos: {pR:.2f}")
print(f"Percentual de sapos: {ps:.2f}")

