'''
"O seno de um ângulo em radianos, no intervalo de 0 a π/2, pode ser calculado através da série de McLaurin, apresentada a seguir:

sen(x) = x - x³/3! + 3^5/5! + x^7/7! ...

a. Escreva uma função que converta um ângulo em graus para seu valor em radianos (180º = π rad)

b. Escreva uma função que receba como parâmetro um ângulo em graus, a precisão requerida para o cálculo, e retorne o seu seno, utilizando a função de conversão graus-radiano feita anteriormente.

c. Faça um programa que teste a sua função para cálculo do seno."
'''

import math

# Função para converter graus em radianos
def graus_para_radianos(angulo_graus):
    return angulo_graus * (math.pi / 180)

# Função para calcular o seno de um ângulo em graus com precisão específica
def calcular_seno(angulo_graus, precisao):
    angulo_radianos = graus_para_radianos(angulo_graus)
    seno = angulo_radianos  # Primeiro termo da série de McLaurin
    termo = angulo_radianos
    n = 3
    sinal = -1
    while abs(termo) >= precisao:
        termo = (angulo_radianos ** n) / math.factorial(n) * sinal
        seno += termo
        n += 2
        sinal *= -1
    return seno

# Função para testar a função calcular_seno
def teste_calcular_seno():
    angulo_graus = float(input("Digite o ângulo em graus: "))
    precisao = float(input("Digite a precisão desejada para o cálculo: "))
    seno_calculado = calcular_seno(angulo_graus, precisao)
    print(f"O seno de {angulo_graus} graus é aproximadamente: {seno_calculado:.4f}")

# Teste da função de calcular seno
teste_calcular_seno()
