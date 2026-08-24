#15. Elabore um programa que calcule e mostre a 
#soma dos 10 primeiros termos da série: (100/0!)+(99/1!)+(98/2!)+(97/3!)...
import math

def calcula_sequencia(n):
    resultado = 0
    for i in range(n):
        termo = (100 - i) / math.factorial(i)
        resultado += termo
    return resultado

resultado_final = calcula_sequencia(10)
print(resultado_final)
