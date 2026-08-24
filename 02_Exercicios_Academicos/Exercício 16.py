'''16. Sendo S=1-1/2+1/3-1/4+1/5-1/6... +1/n, construa um programa que leia N, calcule e mostre 
o valor da série S'''

def calcula_serie(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s -= 1 / i
        else:
            s += 1 / i
    return s

n = int(input("Digite o valor de N: "))
resultado = calcula_serie(n)
print("O valor da série S é:", resultado)
