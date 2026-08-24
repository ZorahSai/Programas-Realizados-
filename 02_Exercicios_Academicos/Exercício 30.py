'''Escreva as seguintes funções:  
a. CparaF – faz a conversão de uma temperatura em graus C para graus F.  
b. CparaK – faz a conversão de uma temperatura em C para Kelvin (C=K-273) 
c. KparaC – faz a conversão de K para C.  
d. KparaF – faz a conversão de K para F (dica: utilize as funções anteriores) 
e. FparaK – faz a conversão de F para K.  
 
A  seguir,  faça  um  programa  que  apresente  continuamente  um  menu  na  tela  com 
todas  as  opções  de  conversão  que  você  implementou.  Uma  vez  feita  a  opção,  o 
programa lê do teclado o valor a ser convertido e imprime o resultado. '''
# Função para converter temperatura de Celsius para Fahrenheit
def CparaF(celsius):
    return (celsius * 9/5) + 32

# Função para converter temperatura de Celsius para Kelvin
def CparaK(celsius):
    return celsius + 273

# Função para converter temperatura de Kelvin para Celsius
def KparaC(kelvin):
    return kelvin - 273

# Função para converter temperatura de Kelvin para Fahrenheit
def KparaF(kelvin):
    celsius = KparaC(kelvin)
    return CparaF(celsius)

# Função para converter temperatura de Fahrenheit para Kelvin
def FparaK(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return CparaK(celsius)

# Função principal para apresentar o menu e realizar as conversões
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Kelvin para Celsius")
        print("4. Kelvin para Fahrenheit")
        print("5. Fahrenheit para Kelvin")
        print("6. Sair")
        
        opcao = input("Digite a letra da opção desejada: ").lower()
        
        if opcao == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C é igual a {CparaF(celsius):.2f}°F")
        elif opcao == "2":
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C é igual a {CparaK(celsius):.2f}K")
        elif opcao == "3":
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K é igual a {KparaC(kelvin):.2f}°C")
        elif opcao == "4":
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K é igual a {KparaF(kelvin):.2f}°F")
        elif opcao == "5":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F é igual a {FparaK(fahrenheit):.2f}K")
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamada da função principal
menu()
