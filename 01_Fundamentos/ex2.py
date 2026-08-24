'''Em um determinado país, deve declarar imposto de renda todo cidadão com renda
anual superior à $ 23.750,00. A renda anual é a renda mensal multiplicada por 13 (12
meses mais a o 13º salário). A alíquota para quem paga é de 20%. Faça um programa
que leia do teclado a renda mensal do usuário e imprima se ele está isento ou se ele
deve fazer a declaração de renda e qual o imposto devido. Declare como constantes
simbólicas o limite para imposto: 23750; o fator de multiplicação: 13; e a alíquota:
20%'''

BASE_R = 23750.00
ALIQ = 0.20
MESES = 13

salario = float(input("Insira o valor do seu salário para análise: "))
renda = salario*MESES
imposto = renda*ALIQ
if renda < BASE_R :
    print("Você está isento de impostos")
else : 
    print("Seu imposto a ser pago é igual a R$",imposto, " reais")