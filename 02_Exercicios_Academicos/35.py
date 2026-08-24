import math
def menu():
    print(" ________________________________ ")
    print("|[MENU]                          |")
    print("|[1] Converter ângulo em radiano |")
    print("|[2] Calcular o seno de um ângulo|")
    print("|[3] Calcular o valor de pi      |")
    print("|[4] Resolver uma equação de 2°  |")
    print("|[0] Sair                        |")
    print("|________________________________|")
def para_radiano():
    graus=float(input("DIGITE O VALOR DO ÂNGULO: "))
    radiano=math.radians(graus)
    print(f"{graus}° é equivalente a {radiano} radianos.")
def calcular_sin():
    angulo = float(input("DIGITE O VALOR DO ÂNGULO: "))
    sin = math.sin(math.radians(angulo))
    print(f"O seno de {angulo}° é {sin}.")
def pi():
    print(f"O valor de pi é {math.pi}.")
def resolver_eq():
    a = float(input("INSIRA O VALOR DE A: "))
    b = float(input("INSIRA O VALOR DE B: "))
    c = float(input("INSIRA O VALOR DE C: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta ==0:
        raiz = -b/(2*a)
        print(f"A raiz da equação é: {raiz:.2f}.")
    else:
        r1=(-b + math.sqrt(delta)) / (2*a)
        r2=(-b - math.sqrt(delta)) / (2*a)
        print(f"As raizes da equação são: {r1} e {r2}.")
opcao = None
while opcao != 0:
    menu()
    opcao = int(input("ESCOLHA UMA OPÇÃO: "))

    if opcao == 1:
            para_radiano()
    elif opcao == 2:
            calcular_sin()
    elif opcao == 3:
            pi()
    elif opcao == 4:
            resolver_eq()
    elif opcao == 0:
            print("Saindo....... Obrigado por usar o progama!!")
    else:
            print("Opção invalida!!!")

