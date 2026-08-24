'''Escreva um programa que, dados três números inteiros, imprima os números em
ordem crescente'''

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 < n2 < n3 :
    print(n1,n2,n3)
elif n1 < n3 < n2 :
    print(n1,n3,n2)
elif n2 < n1 < n3 :
    print(n2,n1,n3)
elif n2 < n3 < n1 :
    print(n2,n3,n1)
elif n3 < n1 < n2 :
    print(n3,n1,n2)
elif n3 < n2 < n1 :
    print(n3,n2,n1)
elif n1 == n2 < n3 :
    print("Número 1 e 2 são iguais. A ordem crescente é:", n1,n3)
elif n1 == n2 > n3 :
    print("Número 1 e 2 são iguais. A ordem crescente é:",n3,n1)
elif n2 == n3 < n1:
    print("Número 2 e 3 são iguais. A ordem crescente é:",n2,n1)
elif n2 == n3 > n1 :
    print("Número 2 e 3 são iguais. A ordem crescente é:",n1,n2)
elif n3 == n1 < n2:
    print("Número 1 e 3 são iguais. A ordem crescente é:",n3,n2)
elif n3 == n1 > n2:
    print("Número 1 e 3 são iguais. A ordem crescente é:",n2,n3)
else :
    print("Todos os números são iguais")