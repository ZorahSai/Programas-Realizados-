#15. Construa  um  programa  que  receba  três  valores  quaisquer  e  imprima-os  em  ordem 
#crescente. Como seu programa reage  a valores de entrada iguais como no exercício 
#anterior?

n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
n3 = int(input("Insira o terceiro numero: "))

if n1 > n2 > n3:
    print(n3)
    print(n2)
    print(n1)
elif n1 > n3 > n2:
    print(n2)
    print(n3)
    print(n1)
elif n2 > n1 > n3:
    print(n3)
    print(n1)
    print(n2)
elif n2 > n3 > n1:
    print(n1)
    print(n3)
    print(n2)
elif n3 > n1 > n2:
    print(n2)
    print(n1)
    print(n3)
elif n3 > n2 > n1:
    print(n1)
    print(n2)
    print(n3)
elif n1 > n2 == n3:
    print(n3)
    print(n1)
elif n2 > n1 == n3:
    print(n3)
    print(n2)
else:
    print(n2)
    print(n3)
