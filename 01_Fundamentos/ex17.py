# exercicio 17
'''Escreva um programa que leia os três lados de um triângulo e imprima se o triângulo
é equilátero, isósceles ou escaleno, ou ainda, se estes lados não podem constituir um
triângulo.
Lembre-se que:
• O comprimento de cada lado de um triângulo é sempre menor do que a soma
dos comprimentos dos outros dois lados.
• Triângulo equilátero: três lados iguais.
• Triângulo isósceles: dois lados iguais.
• Triângulo escaleno: três lados diferentes.'''

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print("Não é um triângulo")
elif l1 == l2 == l3:
    print("É um triângulo equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("É um triângulo isóceles")
else:
    print("É um triângulo escaleno")