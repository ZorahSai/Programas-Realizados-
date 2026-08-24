#12. Uma  empresa  decidiu  dar  um  bônus  de  Natal  aos  seus  funcionários,  cujo  valor  é 
#definido do seguinte modo:  
#a. Funcionários do sexo masculino com tempo de casa superior à 15 anos terão 
#direito à um bônus de 15% do seu salário. 
#b. Funcionárias com tempo de casa superior à 10 anos terão direito a um bônus 
#de 25% do seu salário. 
#c. Demais funcionários receberão um bônus de R$ 500,00 
#Elabore um programa que leia os dados necessários e calcule o bônus à que tem 
#direito o empregado. 


sexo = str(input("Informe seu gênero, sendo M para masculino e F para feminino: "))
tempo = float(input("Informe o tempo que trabalha na empresa: "))
salario = float(input("Informe o salário: R$"))

if sexo == "M"  or sexo == "F":
    if salario == 0 or tempo == 0:
        print("Reinicie o programa e insira valores validos!!! ")
    elif sexo == "M":
        bonus = salario * 0.15
        print(f"Seu bônus sera de R${bonus:.2f}")
    elif tempo > 10:
        bonus = salario * 0.25
        print(f"Seu bônus sera de R${bonus:.2f}")
    elif tempo <= 10:
        bonus = 500
        print(f"Seu bônus sera de R${bonus:.2f}")
    else:
        print("Reinicie o programa e insira valores validos!!! ")
else:
    print("Reinicie o programa e insira valores validos!!! ")