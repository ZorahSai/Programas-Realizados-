#6. Um  dado  material  radioativo  perde  metade  de  sua  massa  a  cada  50s.  Dada  a  massa 
#inicial  em  gramas,  fazer  um  algoritmo  que  determine  o  tempo  necessário  para  que 
#essa massa seja menor que 0,5g.

#import math
#meia_vida = 50
#massa_inicial = float(input('Digite a massa inicial do material radioativo(em gramas): '))
#massa_final = 0.5
#tempo = abs(meia_vida * math.log(massa_final/massa_inicial, 1/2))
#print(f'O tempo necessáiro para a massa de {massa_inicial}g atingir 0.5g é de: {tempo}s')

massa = float(input('Digite a quantidade inicial de gramas do material radioativo: '))
massa_inicial = massa
tempo = 0
while massa > 0.5:

    massa /=2
    tempo += 50

print(f'A massa inicial: {massa_inicial}g\nTempo decorrido: {tempo}s\n')
