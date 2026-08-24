#1. Elabore um programa que: 
#• Mostre um menu de opções de conversão entre moedas (1  – dólar americano, 
#2 – euro, 3 – libra esterlina e 4 – yuan;  
#• Leia a escolha do usuário;  
#• Leia o custo em R$ (reais) da operação; 
#• Imprima  o  valor  da  transação  na  moeda  escolhida,  de  acordo  com  os  fatores 
#de conversão da tabela abaixo. 
#Moeda Valor (R$) 
#Dólar americano 3,258 
#Euro 4,095 
#Libra esterlina 4,529 
#Yuan 0,515

DOLAR = 3.258
EURO = 4.095
LIBRA = 4.529
YUAN = 0.515

print('##################################')
print('#      CONVERSOR DE MOEDAS       #')
print('##################################\n')
print('____________________________')
print('|   MOEDA    -   VALOR (R$)|')
print('|(1)Dolar Americano - 3,258|')
print('|(2)Euro            - 4,095|')
print('|(3)Libra Esterlina - 4,529|')
print('|(4)Yuan            - 0,515|')
print('____________________________')

opção = int(input('Digite a opção de moeda desejada para a conversão(1-4): '))
while (opção <= 0 or opção > 4): 
    opção = int(input("Por favor, digite uma opção de 1 à 4: ")) 

valor_Reais = float(input(f'Digite o valor em Reais para a conversão R$: '))

if opção == 1:
    print(f'O valor convertido de Real para Dólar Americano é de:\n R$:{valor_Reais:,.2f} -> $:{valor_Reais/DOLAR:,.2f}')

elif opção == 2:
    print(f'O valor convertido de Real para Euro é de:\n R$:{valor_Reais:,.2f} -> €:{valor_Reais/EURO:,.2f}')

elif opção == 3:
    print(f'O valor convertido de Real para Libra Esterlina é de:\n R$:{valor_Reais:,.2f} -> £:{valor_Reais/LIBRA:,.2f}')

else:  # (opcao == 4)
    print(f'O valor convertido de Real para Yuan é de:\n R$:{valor_Reais:,.2f} -> ¥:{valor_Reais/YUAN:,.2f}')
