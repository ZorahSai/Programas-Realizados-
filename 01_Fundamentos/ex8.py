'''8. Faça um programa que leia o ano de nascimento de uma pessoa e imprima se ela é
maior ou menor de idade. Declare o ano atual e o limite de maioridade como
constantes simbólicas.'''
nasc = int(input("Digite o ano de nascimento: "))
ANO = 2025
MAIORIDADE = 18
idade = ANO - nasc
if idade >= MAIORIDADE:
    print("A pessoa é maior de idade.")
elif idade < MAIORIDADE:
    print("A pessoa é menor de idade.")



