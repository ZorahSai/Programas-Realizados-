#  13. Elabore um programa que receba três valores quaisquer e imprima o menor valor dos 
#três lidos. O que acontece se o seu programa tiver lido dois ou mais números iguais 
#(Ex.: 1, 1, 3)? 

n1 = float(input('Digite o primeiro número:' ))
n2 = float(input('Digite o segundo número:'  ))
n3 = float(input('Digite o terceiro número:' ))

menor = n1 

if menor > n2 or menor == n2:
    menor = n2
    if menor > n3 or menor == n3:
        menor = n3
    else: 
        print("Insira valores corretos!!!! ")

print(f"O Menor valor dentre ({ n1}, {n2}, {n3} ) é {menor}!")



