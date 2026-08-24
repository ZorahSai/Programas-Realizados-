'''Uma  equação  do  segundo  grau  é  escrita ax² + bx +c = 0  e  a  sua  solução  é  dada  em 
função  dos  valores  de  a,  b  e  c.  Podendo  ter  duas  raízes,  uma  ou  nenhuma.  Escreva 
uma função que resolva a equação do segundo grau, retornando o número de raízes 
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.'''

import math

def resolver_equacao_segundo_grau(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return 2, raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return 1, raiz
    else:
        return 0

# Solicitar os valores de a, b e c ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Resolver a equação do segundo grau
num_raizes, *raizes = resolver_equacao_segundo_grau(a, b, c)

# Exibir o resultado
if num_raizes == 2:
    raiz1, raiz2 = raizes
    print(f"A equação tem duas raízes reais distintas: {raiz1} e {raiz2}.")
elif num_raizes == 1:
    raiz = raizes[0]
    print(f"A equação tem uma raiz real: {raiz}.")
elif num_raizes == 0:
    print("A equação não tem raízes reais.")
else:
    print("Erro: Discriminante negativo. A equação não tem raízes reais.")
