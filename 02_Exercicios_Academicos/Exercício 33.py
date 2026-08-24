'''
O valor aproximado de π pode ser calculado a partir da série:

π=4(41−43+45−47+…)π=4(14​−34​+54​−74​+…)

Escreva uma função que calcule o valor de π, com a precisão fornecida como parâmetro."
faça um codigo'''
def calcular_pi(precisao):
    pi_aproximado = 0
    denominador = 1
    sinal = 1
    termo = sinal * 4 / denominador
    while abs(termo) >= precisao:
        pi_aproximado += termo
        sinal *= -1
        denominador += 2
        termo = sinal * 4 / denominador
    return pi_aproximado

# Teste da função para calcular pi com uma precisão de 0.0001
precisao = 0.000000000001
pi_calculado = calcular_pi(precisao)
print("Valor aproximado de π:", pi_calculado)
