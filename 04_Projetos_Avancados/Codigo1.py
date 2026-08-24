#Sistema de Login

senha = []
login = []
usuario = input("insira o nome do usuario: ")
senha = input("Insira uma senha: ")
senha2 = input("Insira a mesma senha: ")
while senha2 not in senha:
    print("Repita a senha digitada anteriormente!!")
    senha2 = input("Insira a mesma senha: ")

with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"{usuario},{senha}\n")
print("Usuário cadastrado com sucesso!")



usuario_input = input("Usuario: ")
senha_input = input("Senha: ")
try:
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario_salvo, senha_salvo = linha.strip().split(",")
            if usuario_input == usuario_salvo and senha_input == senha_salvo:
                print("Login efetuado com sucesso!!!")
            else: 
                print("Usuario ou senha invalidos!! ")
                break
except FileNotFoundError:
    print("Saindo")