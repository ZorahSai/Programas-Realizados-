'''10. Faça um programa que lê um caracter do teclado e imprima se o caracter é uma letra.
Se for, deve imprimir se a letra em questão é maiúscula ou minúscula. Dica: use os
códigos ASCII das letras para resolver este problema.'''
char = input("Digite uma tecla do teclado: ")
if len(char) != 1: 
    print("Erro: Digite apenas um único caractere.")
else:
    codigo = ord(char)  
    if 'A' <= char <= 'Z':  
        print(f"O caractere '{char}' é uma letra maiúscula. Seu código ASCII é: {codigo}")
    elif 'a' <= char <= 'z':  
        print(f"O caractere '{char}' é uma letra minúscula. Seu código ASCII é: {codigo}")
    else:
        print(f"O caractere '{char}' não é uma letra. Seu código ASCII é: {codigo}")
