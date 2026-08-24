'''A multiplicação entre dois números inteiros pode ser definida como uma repetição da 
adição de um deles. Exemplo: 3x4 = 4 + 4 + 4 
Escreva uma função que multiplique dois números inteiros utilizando esse método. A 
seguir,  escreva  um  programa  que  peça  ao  usuário  um  número  inteiro  e  imprima  a 
tabuada para aquele número (de 1 à 10) utilizando a função construída. '''

# Função para multiplicar dois números inteiros utilizando o método de repetição de adição
def multiplicacao_repetida(numero1, numero2):
    resultado = 0
    for _ in range(numero2):
        resultado += numero1
    return resultado

# Função para imprimir a tabuada de um número utilizando a função de multiplicação repetida
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(0, 11):
        resultado = multiplicacao_repetida(numero, i)
        print(f"{numero} x {i} = {resultado}")

# Programa principal
try:
    numero = int(input("Digite um número inteiro: "))
    tabuada(numero)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
