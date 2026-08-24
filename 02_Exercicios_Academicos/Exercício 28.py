'''Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem, 
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação 
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo: 
 
Tipo Quantidade vendida Comissões 
8 K-10 ou mais - R$ 550 por TV vendida 
    -Menos que 10 R$  350 por TV vendida 
4 K-10 ou mais -R$ 420 por TV vendida 
               -Menos que 10 R$ 250 por TV vendida 
 
Sabe-se  ainda,  que  ele  tem  um  desconto  de  8%  do  salário  total  para  pagamento  do 
INSS  e  se  o  seu  salário  total for  superior  a R$  950,00  ele  ainda  tem  um  desconto  de 
5% do salário para fins de imposto de renda. Faça um programa que leia os dados de 
vários  funcionários  e,  para  cada  funcionário,  calcule  e  imprima  o  salário  líquido  (já 
com os descontos). Além disso, no final, o programa deve: 
12 
 
a. Imprimir o número de funcionários. 
b. Imprimir o total de salários pagos. 
c. Imprimir a média das comissões. 
d. Imprimir o valor da maior e da menor comissão paga pelo departamento. '''


# Função para calcular a comissão com base no tipo e quantidade de TVs vendidas
def calcular_comissao(tipo, quantidade):
    if tipo == "8K":
        if quantidade >= 10:
            return 550 * quantidade
        else:
            return 350 * quantidade
    elif tipo == "4K":
        if quantidade >= 10:
            return 420 * quantidade
        else:
            return 250 * quantidade
    else:
        return 0

# Função para calcular o salário líquido com descontos
def calcular_salario_liquido(salario_bruto):
    inss = salario_bruto * 0.08
    salario_liquido = salario_bruto - inss
    if salario_liquido > 950:
        imposto_renda = salario_liquido * 0.05
        salario_liquido -= imposto_renda
    return salario_liquido

# Variáveis para armazenar estatísticas
total_salarios = 0
total_comissoes = 0
numero_funcionarios = 0
maior_comissao = float('-inf')
menor_comissao = float('inf')

while True:
    tipo = input("Digite o tipo de TV vendida (8K/4K) ou digite 'sair' para encerrar: ").upper()
    if tipo == "SAIR":
        break
    quantidade = int(input("Digite a quantidade de TVs vendidas: "))
    salario_fixo = float(input("Digite o salário fixo do funcionário: "))
    
    # Calcular comissão e salário líquido
    comissao = calcular_comissao(tipo, quantidade)
    salario_total = salario_fixo + comissao
    salario_liquido = calcular_salario_liquido(salario_total)
    
    # Atualizar estatísticas
    total_salarios += salario_liquido
    total_comissoes += comissao
    numero_funcionarios += 1
    if comissao > maior_comissao:
        maior_comissao = comissao
    if comissao < menor_comissao:
        menor_comissao = comissao

    print(f"Salário líquido do funcionário: R$ {salario_liquido:.2f}")

# Imprimir estatísticas finais
print(f"Número de funcionários: {numero_funcionarios}")
print(f"Total de salários pagos: R$ {total_salarios:.2f}")
print(f"Média das comissões: R$ {total_comissoes / numero_funcionarios:.2f}")
print(f"Maior comissão paga: R$ {maior_comissao:.2f}")
print(f"Menor comissão paga: R$ {menor_comissao:.2f}")
