#5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser 
#colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros 
#seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha 
#o cuidado de testar se ele não sofre um overflow.

total_graos = 0
graos_no_quadrado = 1

for quadrado in range(1,65):
    total_graos += graos_no_quadrado
    graos_no_quadrado *= 2

print(f'O número total de graos de milho no tabuleiro é de: {total_graos:,.2f}')

#vai dar 18 quintilhões ; 446 quadrilhões ; 744 trilhões ; 73 bilhões ; 709 milhões ; 551 mil e 615