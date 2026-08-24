import math

def menu():
    print("Menu:")
    print("1. Converter um ângulo em graus para radiano")
    print("2. Calcular o seno de um ângulo")
    print("3. Calcular o valor de pi")
    print("4. Resolver uma equação do segundo grau")
    print("0. Sair")

def graus_para_radiano():
    graus = float(input("Digite o valor do ângulo em graus: "))
    radiano = math.radians(graus)
    print(f"{graus} graus é equivalente a {radiano} radianos.")

def calcular_seno():
    angulo = float(input("Digite o valor do ângulo em graus: "))
    seno = math.sin(math.radians(angulo))
    print(f"O seno de {angulo} graus é {seno}.")

def calcular_pi():
    print(f"O valor de pi é {math.pi}.")

def resolver_equacao_segundo_grau():
    a = float(input("Digite o coeficiente 'a' da equação: "))
    b = float(input("Digite o coeficiente 'b' da equação: "))
    c = float(input("Digite o coeficiente 'c' da equação: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A única raiz da equação é {raiz}.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são {raiz1} e {raiz2}.")

# Programa principal
opcao = None

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        graus_para_radiano()
    elif opcao == 2:
        calcular_seno()
    elif opcao == 3:
        calcular_pi()
    elif opcao == 4:
        resolver_equacao_segundo_grau()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
