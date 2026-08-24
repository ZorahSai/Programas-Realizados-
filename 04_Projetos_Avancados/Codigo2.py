#Projeto Criação de um Menu


def menu():
    opcao = 0
    while opcao != 5:
        print("1 - Bem vindo!")
        print("2 - Bom dia!")
        print("3 - Boa Tarde!")
        print("4 - Boa Noite!")
        print("5 - Sair")
        opcao = int(input("Escolha uma das opções: "))
        
        if opcao == 1:
            print("Seja Bem vindo ao nosso programa!!!")
            return menu()
        elif opcao == 2:
            print("Tenha um Otimo Dia!!")
            return menu()
        elif opcao == 3:
            print("Tenha uma Otima Tarde!!!")
            return menu()
        elif opcao == 4:
            print("Tenha uma Otima Noite!!!!")
            return menu()
        elif opcao == 5:
            print("Saindo......")
        else:
            print("opção invalida! Tente Novamente")
            
menu()