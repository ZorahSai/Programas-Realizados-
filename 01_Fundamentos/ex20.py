# exercicio 20
'''Utilizando-se do comando if else aninhado, elabore um programa que:
• Mostre um menu de opções de conversão entre moedas (1 - dólar americano,
2 - euro, 3 - libra esterlina e 4 - yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.

Moeda Valor (R$)
Dólar americano 3,258
Euro 4,095
Libra esterlina 4,529
Yuan 0,515'''

moeda_escolhida = int(input(
'''1- dólar americano
2- euro
3- libra esterlina
4- yuan
Digite para qual moeda você deseja realizar a conversão:'''))

valor_reais = float(input("Digite o valor em reais que você deseja converter:"))
if moeda_escolhida == 1:
    valor_convertido = valor_reais/3.258
    print(f"Valor convertido em dólar americano: ${valor_convertido:.2f}")
else:
    if moeda_escolhida == 2:
        valor_convertido = valor_reais/4.095
        print(f"Valor convertido em euro:  €{valor_convertido:.2f}")
    else:
        if moeda_escolhida == 3:
            valor_convertido = valor_reais/4.529
            print(f"Valor convertido em libra esterlina: £{valor_convertido:.2f}")
        else:
            if moeda_escolhida == 4:
                valor_convertido = valor_reais/0.515
                print(f"Valor convertido em yuan: ¥{valor_convertido:.2f}")
            else:
                print("Opção inválida, por favor digite uma opção ente 1 e 4.")