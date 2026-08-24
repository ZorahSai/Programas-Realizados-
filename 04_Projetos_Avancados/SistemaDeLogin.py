import bcrypt
import getpass
import tkinter as tk

class SistemaDeLogin:

    def gerar_hash_seguro(self, senha_puro_texto):
        senha_bytes = senha_puro_texto.encode('utf-8')
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_bytes, salt)
        return senha_hash

    def verificar_senha(self, senha_digitada, hash_armazenado):
        senha_bytes = senha_digitada.encode('utf-8')
        if isinstance(hash_armazenado, str):
            hash_armazenado = hash_armazenado.encode('utf-8')
        return bcrypt.checkpw(senha_bytes, hash_armazenado)

    def cadastro(self):
        print("\n--- CADASTRO DE NOVO USUÁRIO ---")
        usuario = input("Insira o nome do usuario: ").strip()
        if not usuario:
            print("O nome de usuário não pode estar vazio.")
            return

        senha = input("Insira uma senha: ")
        senha2 = input("Insira a mesma senha novamente: ")
        
        while senha2 != senha:
            print("As senhas não coincidem. Repita a senha digitada anteriormente!!")
            senha2 = input("Insira a mesma senha: ")

        senha_hash = self.gerar_hash_seguro(senha)
        
        with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{usuario},{senha_hash.decode('utf-8')}\n")
            
        print("Usuário cadastrado com sucesso!")

    def login(self):
        print("\n--- TELA DE LOGIN ---")
        usuario_input = input("Usuario: ").strip()
        senha_input = getpass.getpass("Senha: ")
        
        login_sucesso = False
        
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    usuario_salvo, hash_salvo = linha.strip().split(",", 1)
                    
                    if usuario_input == usuario_salvo:
                        if self.verificar_senha(senha_input, hash_salvo):
                            login_sucesso = True
                        break
                        
            if login_sucesso:
                print("Login efetuado com sucesso!!! Seja bem-vindo(a).")
            else:
                print("Usuário ou senha inválidos!!")
                
        except FileNotFoundError:
            print("Nenhum usuário cadastrado ainda. Faça um cadastro primeiro.")

    def menu(self):
        while True:
            print("\n==============================")
            print("      SISTEMA DE LOGIN        ")
            print("==============================")
            print("1. Cadastrar")
            print("2. Fazer Login")
            print("3. Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastro()
            elif opcao == "2":
                self.login()
            elif opcao == "3":
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    sistema = SistemaDeLogin()
    sistema.menu()