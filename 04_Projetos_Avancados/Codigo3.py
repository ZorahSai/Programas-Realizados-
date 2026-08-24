#Calculadora 
def obter_numero(texto):
    while True:
        entrada = input(texto)
        entrada = entrada.replace(',','.')

        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números!!!!")

def soma():
    n1 = obter_numero("Insira o valor: ")
    n2 = obter_numero("Insira o valor: ")
    total = n1 + n2
    print(total)
    print("-" * 25)
    print(f"A Soma de {n1} + {n2} = {total}")
    print("-" * 25)

def subtração():
    n1 = obter_numero("Insira o valor: ")
    n2 = obter_numero("Insira o valor: ")
    total = n1 - n2
    print(total)
    print("-" * 25)
    print(f"A Subtração de {n1} - {n2} = {total}")
    print("-" * 25)

def multiplicacao():
    n1 = obter_numero("Insira o valor: ")
    n2 = obter_numero("Insira o valor: ")
    total = n1 * n2
    print(total)
    print("-" * 25)
    print(f"A Multiplicação de {n1} * {n2} = {total}")
    print("-" * 25)

def divisao():
    n1 = obter_numero("Insira o valor: ")
    n2 = obter_numero("Insira o valor: ")
    while n2 == 0:
        print("O divisor não pode ser 0, insira um valor valido!")
        n2 = obter_numero("Insira o valor: ")
    total = n1 / n2
    print(total)
    print("-" * 25)
    print(f"A Divisão de {n1} / {n2} = {total}")
    print("-" * 25)

def calcular_expressao():
    expressao = input("Digite a operação: ").strip()
    operador = None
    for op in ['+', "-", "*", "/"]:
        if op in expressao:
            operador = op
            break
    if not operador:
        print("ERRO: Operador não encontrado ou inválido!!! Use +, -, * ou /.")
    try:
        partes = expressao.split(operador)
        n1 = float(partes[0].replace(',','.'))
        n2 = float(partes[1].replace(',','.'))
        match operador:
            case '+': total = n1 + n2
            case '-': total = n1 - n2
            case '*': total = n1 * n2
            case '/':
                if n2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                total = n1 / n2
        print(f"Resultado da expressão: {total}\n")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números e operadores (Ex: 4+5)")  


def menu():
    while True:
        print("1  + Soma")
        print("2  - Subtração ")
        print("3  * Multiplicação")
        print("4  / Divisão")
        print("5  = Digite uma expressão")
        print("6  Sair")
        opcao = obter_numero("Escolha uma das opções: ")
        print()
        match opcao:
            case 1:
                soma()
            case 2:
                subtração()
            case 3:
                multiplicacao()
            case 4:
                divisao()
            case 5:
                calcular_expressao()    
            case 6:
                print("Saindo......")
                break
            case _:
                print("opção invalida! Tente Novamente")
def iniciar():
    print("I N I C I A N D O......")
    print(". . . . . . . . . . . .")
    print(" ")
    print("Seja Bem Vindo ao Nosso progama!")
    menu()

iniciar()

