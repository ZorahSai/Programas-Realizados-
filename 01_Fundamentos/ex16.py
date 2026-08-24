# exercicio 16
'''Uma equação do segundo grau é descrita genericamente por ax2 + bx + c = 0.
Escrever um programa que leia os valores de a, b e c e resolva a equação do segundo
grau correspondente, imprimindo as raízes reais quando existirem ou avisando que
não existem raízes.'''


a = int(input("Digite a:"))
b = int(input("Digite b:"))
c = int(input("Digite c:"))

if a == 0:
    print("Não é uma equação do segundo grau")
else:
    delta = (b**2) - (4*a*c)
    if delta == 0:
        x = (-b) / (2*a)
        print (f"A raiz é {x}")
    elif delta > 0:
        x1 = ((-b) + delta**0.5) / (2*a)
        x2 = ((-b) - delta**0.5) / (2*a)
        print(f"As raizes são {x1} e {x2}")
    else:
        print("Não existem raizes reais")