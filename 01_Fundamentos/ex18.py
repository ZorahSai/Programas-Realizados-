# exercicio 18
'''Desejamos calcular, a partir do sexo e da altura, o peso ideal de uma pessoa. Para
isto, devemos saber que existem duas fórmulas para o peso ideal, que são:
• Homens: (72,7 * altura) - 58
• Mulheres: (62,1 * altura) - 44,7
Para que uma pessoa seja considerada obesa, a diferença entre o seu peso e o peso
ideal deve ser superior à 40 Kg. Elabore um programa que leia o sexo, o peso e a
altura de uma pessoa, imprima o peso ideal e informe se a pessoa está abaixo do
peso ideal, acima do peso ideal ou obesa.'''

sexo = input("digite seu sexo (M para masculino/F para feminino:")
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

if (sexo == "M"):
    homem = (72.7 * altura) - 58
    if altura == 0:
        print("Reinicie o programa e insira um valor para a altura!!!!")
    elif (homem + 40) < peso:
        print(f"Voçê está Obeso, estando {peso - homem:.2f}Kg acima do peso ideal que seria {homem:.2f}kg ")
    elif homem < peso:
        print(f"Voçê esta acima do peso, estando {peso - homem:.2f}Kg acima do peso ideal que seria {homem:.2f}kg ")
    elif peso == 0:
        print("Reinicie o programa e insira um valor de peso valido!!!")
    else:
        print(f"Voçê está abaixo do peso, estando {homem - peso:.2f}Kg abaixo do peso ideal que seria {homem:.2f}Kg")
elif (sexo == "F"):
    mulher = (62.1 * altura) - 44.7
    if altura == 0:
        print("Reinicie o programa e insira um valor para a altura!!!")
    elif (mulher + 40) < peso:
        print(f"Voçê está Obeso, estando {peso - mulher:.2f}Kg acima do peso ideal que seria {mulher:.2f}kg ")
    elif mulher < peso:
        print(f"Voçê esta acima do peso, estando {peso - mulher:.2f}Kg acima do peso ideal que seria {mulher:.2f}kg ")
    elif peso == 0:
        print("Reinicie o programa e insira um valor de peso valido!!!")
    else:
        print(f"Voçê está abaixo do peso, estando {mulher - peso:.2f}Kg abaixo do peso ideal que seria {mulher:.2f}Kg")
else:
    print("Reinicie o programa e insira as M para masculino e F para feminino para que o programa funciona corretamente!!!")
