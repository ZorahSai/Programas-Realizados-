'''Em uma loja de eletroeletrônicos, um vendedor que consiga vender mais de R$
3.000,00 por mês recebe como comissão 5% do valor vendido. Abaixo disso, ele não
recebe nenhuma comissão. Faça um programa que leia do teclado o total de vendas
mensais de um vendedor e imprima se ele tem direito a comissão e, se tiver, de
quanto.'''

BASE = 3000
TAXA = 0.05

vendas = float(input("Insira o valor total das vendas: "))
comissao = float(vendas*TAXA)

if vendas < BASE :
    print("Você não tem direito a comissão")
else : 
    print("Sua comissão é de R$",comissao, " reais")