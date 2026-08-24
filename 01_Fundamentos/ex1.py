'''Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
valor até R$100,00 ganha um cupom para concorrer a um carro e se ele comprar
acima de R$100,00 ganha dois cupons e um vale-desconto no total de 10% da
compra. Faça um programa que leia do teclado o total de compras e imprima se o
cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
desconto.'''

LIMITE = 100.0
VALE = 0.10

compra = float(input ("Qual foi o valor de sua compra? "))
desconto = float(VALE*compra)

if compra <= LIMITE :
    print("Você possui um cupom para concorrer a um carro")
else :
    print("Você possui dois cupons onde concorre a um carro, além de ter ganhado um vale de desconto no valor de R$",desconto," reais")