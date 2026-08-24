#Função para converter Celsius para Fahrenheit
def CparaF(celsius):
    return(celsius* 9/5) + 32
#Função para converter Celsius para Kelvin
def CparaK(celsius):
    return celsius + 273
#Função para converter Kelvin para Celsius
def KparaC(kelvin):
    return kelvin-273
#Função para converter Kelvin para Fahrenheit
def KparaF(kelvin):
    celsius = KparaC(kelvin)
    return CparaF(celsius)
#Função para converter Fahrenheit para Kelvin
def FparaK(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return CparaK(celsius)
#Função Menu
def menu():
    while True:
        print("\n [ESCOLHA UMA OPÇÃO:]\t")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Kelvin para Celcius")
        print("4. Kelvin para Fahrenheit")
        print("5. Fahrenheit para Kelvin")
        print("6. Finalizar")

        opcao =input("DIGITE O NUMERO QUE DESEJA USAR: ").lower()
        if opcao =="1":
            celsius=float(input("DIGITE A TEMPERATURA: "))
            print(f"{celsius}°C é igual a {CparaF(celsius):.2f}°F")
        elif opcao =="2":
            celsius=float(input("DIGITE A TEMPERATURA: "))
            print(f"{celsius}°C é igual a {CparaK(celsius):.2f}K")
        elif opcao =="3":
            kelvin=float(input("DIGITE A TEMPERATURA: "))
            print(f"{kelvin}K é igual a {KparaC(kelvin):.2f}°C")
        elif opcao =="4":
            kelvin ==float(input("DIGITE A TEMPERATURA: "))
            print(f"{kelvin}K é igual a {KparaF(kelvin):.2f}°F")
        elif opcao =="5":
            fahrenheit=float(input("DIGITE A TEMPERATURA: "))
            print(f"{fahrenheit}°F é igual a {FparaK(fahrenheit):.2f}K")
        elif opcao =="6":
            print("PROGAMA ENCERRADO, OBRIGADO POR USAR!!!")
        else:
            print("OPÇÃO INVALIDA!!!! INSIRA UM DAS OPÇÕES!")
#Chamada
menu()
