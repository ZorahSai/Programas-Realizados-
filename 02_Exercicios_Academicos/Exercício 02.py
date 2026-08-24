#2. Faça  um  programa  que  leia  um  conjunto  de  números  positivos,  sendo  o  conjunto 
#destes números finalizado quando for digitado um número negativo. Ao final, imprima 
#o maior e o menor número lido e a média deles.

numero = -1

while numero <= 0:
 numero = int(input("Digite um número positivo: "))
 if numero <= 0:
    print('\tVocê precisa digitar um número positivo!\n')
menor = numero
maior = numero
while numero > 0:
 numero = int(input("Digite um número positivo: "))

 if numero < menor and numero > 0:
     menor = numero
 if numero > maior and numero > 0:
     maior = numero

média = (maior + menor) / 2
print(f"O maior e o menor número lido, respectivamente, foram: {maior, menor}")
print(f"A média entre os dois foi de: {média}")
