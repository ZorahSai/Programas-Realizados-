'''Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que 
os  dados  de  cada  contribuinte  (número  do  CPF,  número  de  dependentes  e  renda 
mensal)  são  valores  fornecidos  pelo  usuário.  Para  cada  contribuinte  será  feito  um 
desconto  no  imposto  de  5%  do  salário  mínimo  (R$136,00)  para  cada  dependente  (o 
salário mínimo e o desconto são designados por constantes simbólicas). Os valores 
da alíquota para cálculo do imposto são: 
Renda Líquida (R$) - Alíquota 
até 900,00 - isento 
900,01 até 1500,00 - 5% 
1500,01 até 1900,00 - 10% 
1900,01 até 2200,00 - 15% 
acima de 2200,01 - 20%

O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final, 
devem ser impressos: 
a. Para cada contribuinte, o total a pagar. 
b. O número de contribuintes. 
c. O total de contribuintes isentos e não isentos. 
d. O total de impostos que serão arrecadados desse grupo de contribuintes. 
e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar 
o maior imposto. 
'''
# Constantes simbólicas
SALARIO_MINIMO = 136.00
DESCONTO_POR_DEPENDENTE = 136.00  # Alteração aqui para subtrair 136 por dependente

# Função para calcular o imposto de renda
def calcular_imposto_renda(renda, dependentes):
    renda_liquida = renda - (dependentes * DESCONTO_POR_DEPENDENTE)
    if renda_liquida <= 900.00:
        imposto = 0
    elif 900.01 <= renda_liquida <= 1500.00:
        imposto = renda_liquida * 0.05
    elif 1500.01 <= renda_liquida <= 1900.00:
        imposto = renda_liquida * 0.10
    elif 1900.01 <= renda_liquida <= 2200.00:
        imposto = renda_liquida * 0.15
    else:
        imposto = renda_liquida * 0.20
    return max(0, imposto)  # Imposto não pode ser negativo

# Variáveis para guardar informações
total_a_pagar = 0
num_contribuintes = 0
num_isentos = 0
total_impostos_arrecadados = 0
maior_imposto = 0
cpf_maior_imposto = None

# Loop para entrada de contribuintes
while True:
    cpf = input("Informe o número do CPF (ou digite 0 para finalizar): ")
    if cpf == '0':
        break
    dependentes = int(input("Informe o número de dependentes: "))
    renda = float(input("Informe a renda mensal: "))

    if cpf != '0':
        num_contribuintes += 1
        imposto = calcular_imposto_renda(renda, dependentes)
        total_impostos_arrecadados += imposto
        if imposto == 0:
            num_isentos += 1
        else:
            if imposto > maior_imposto:
                maior_imposto = imposto
                cpf_maior_imposto = cpf
        total_a_pagar += imposto

# Subtraindo R$ 136,00 para cada dependente
total_a_pagar -= (num_contribuintes * DESCONTO_POR_DEPENDENTE)

# Garantindo que o total a pagar não seja negativo
total_a_pagar = max(0, total_a_pagar)

# Resultados
print("\n--- Resultados ---")
print("Total a pagar pelos contribuintes:", total_a_pagar)
print("Número de contribuintes:", num_contribuintes)
print("Número de contribuintes isentos:", num_isentos)
print("Número de contribuintes não isentos:", num_contribuintes - num_isentos)
print("Total de impostos arrecadados:", total_impostos_arrecadados)
if cpf_maior_imposto:
    print("CPF do contribuinte que vai pagar o maior imposto:", cpf_maior_imposto)
    print("Valor do maior imposto a ser pago:", maior_imposto)
else:
    print("Não há contribuintes pagando impostos.")
