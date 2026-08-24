'''Escreva  uma  função  (FparaC)  que  receba  uma  temperatura  em  graus  F  e  retorne  a 
temperatura em graus C, sendo: )32(9
5 −= FC. A seguir, faça um programa que, em 
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente, 
utilizando a função FparaC.'''
#Fahrenheit para Celsius
def FpraC(fahrenheit):
    celsius =  5 / 9 *(fahrenheit - 32)
    return celsius

while True:
    try:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit (ou 'sair' para encerrar): "))
        if fahrenheit == "sair":
            break   
        celsius = FpraC(fahrenheit)
        print(f"A temperatura em Celsius é: {celsius:.2f}°C")
    except ValueError:
        print("Por favor, digite um número ou 'sair' para encerrar.")
