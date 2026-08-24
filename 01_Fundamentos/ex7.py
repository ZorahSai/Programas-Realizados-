'''Um microempresário tem por norma retirar mensalmente 40% do lucro de sua
empresa para os seus gastos pessoais se o lucro ultrapassar R$ 3.000,00 e retirar
apenas R$ 1.000,00 se o lucro for menor que isso. Faça um programa que leia do
teclado o faturamento mensal e o total das despesas para calcular o lucro (lucro =
faturamento - despesas) e imprima quanto o microempresário deve retirar neste mês.
Declare com constantes simbólicas o lucro mínimo, a retirada mínima e o limite da
retirada.'''

faturamento_m = float(input("Informe o faturamento do mês: "))
despesas_m = float(input("Informe as despesas do mês: "))

LUCROMAX = 3000
LUCROMIN = 1000
taxa = 0.40
lucro = faturamento_m - despesas_m

if lucro > 3000 :
    print("A retirada será de R$", (lucro*taxa), "reais")
elif lucro <= 0:
    print("Você está no vermelho!!!!")
else :
    print("A retirada será de R$", (LUCROMIN), "reais")