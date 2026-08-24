#Função Multiplicação
def multiplicacao_rept(numero1,numero2):
    resultado=0
    for _ in range(numero2):
        resultado += numero1
    return resultado
#Função para Tabuada do numero multiplicado
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(0,11):
        resultado = multiplicacao_rept(numero,i)
        print(f"{numero} x {i}={resultado}")
#Principal
try:
    numero=int(input("DIGITE UM NUMERO: "))
    tabuada(numero)
except ValueError:
    print("POR FAVOR, INSIRA UM NUMERO INTEIRO!!!!")