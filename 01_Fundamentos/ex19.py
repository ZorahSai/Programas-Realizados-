# exercicio 19
'''Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte
forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for
da categoria “Gerente”, receberá 20% de aumento e os demais funcionários
receberão 15% de aumento. Faça um programa utilizando o comando if else aninhado
que leia do teclado o salário e a categoria do funcionário, calcule e imprima o seu
novo salário.'''


salario = float(input("Digite seu salário:"))
cat_funcionario = str(input("Digite em qual categoria de funcionário você está (Técnico/Gerente/Outros):"))

if cat_funcionario == 'Técnico' or cat_funcionario == 'Tecnico' or cat_funcionario == 'técnico' or cat_funcionario == 'tecnico':
    novo_salario = salario + salario*0.30
    print (f"Seu novo salário vai ser de R${novo_salario}")
else:
    if cat_funcionario == 'Gerente' or cat_funcionario == 'gerente':
      novo_salario = salario + salario*0.20
      print(f"Seu novo salário vai ser de R${novo_salario}")
    else:
        if cat_funcionario == 'Outros' or cat_funcionario == 'outros':
         novo_salario = salario + salario*0.15
         print(f"Seu novo salário é de R${novo_salario}")
        else:
         print("Categoria inválida! Digite 'Técnico', 'Gerente' ou 'Outros'")