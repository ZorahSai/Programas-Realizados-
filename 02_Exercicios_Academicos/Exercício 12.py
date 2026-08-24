'''12. Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N 
é fornecido pelo usuário. 
Sabemos que: 
N! = 1 x 2 x 3 x 4 x...x (N - 1) x N; 
0! = 1, por definição.'''

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero_usuario = int(input("Digite um número para calcular o fatorial: "))

if numero_usuario < 0:
    print("Por favor, reinicie o programa e digite um número positivo")
else:
    fatorial_resultado = calcular_fatorial(numero_usuario)
    print(f"O fatorial de {numero_usuario} é: {fatorial_resultado}")
