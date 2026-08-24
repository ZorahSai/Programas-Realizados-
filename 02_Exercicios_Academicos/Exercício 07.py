#7. Para fazer o balanço mensal de um armazém, faça um programa que que leia para um 
#número  qualquer  de  mercadorias  diferentes  o  preço  de  custo,  o  preço  de  venda  e  a 
#quantidade  vendida.  A  partir  desses  dados  imprima:  o  número  total  de  mercadorias 
#diferentes lidas, o faturamento total e o lucro total do armazém. 

mercadorias = []

while True:
    número_Mercadoria = int(input('Digite o número de identificação da mercadoria: '))

    if número_Mercadoria <= 0:
        break

    custo_Mercadoria = float(input('\tDigite o Custo da mercadoria R$: '))
    preço_venda_Mercadoria = float(input('\tDigite o preço de venda da mercadoria R$: '))
    qtd_Mercadoria = float(input('\tDigite a quantidade vendida da mercadoria: '))

    mercadorias.append([número_Mercadoria, custo_Mercadoria, preço_venda_Mercadoria, qtd_Mercadoria])

if mercadorias:
    total_vendas = sum(mercadoria[2] * mercadoria[3] for mercadoria in mercadorias)
    lucro_total = sum((mercadoria[2] - mercadoria[1]) * mercadoria[3] for mercadoria in mercadorias)

    print(f'Número de mercadorias: {len(mercadorias)}')
    print(f'Total de vendas R$: {total_vendas}')
    print(f'Lucro total R$: {lucro_total}')

else:
    print('Você não inseriu nenhuma mercadoria!\n\tPor favor, reinicie o programa.')
