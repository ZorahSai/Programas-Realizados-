import math
#Função graus para radiano
def graus_for_rad(angulo_graus):
    return angulo_graus * (math.pi/100)
#Função Calcular seno
def calcular_sin(angulo_graus, precisao):
    angulo_rad=graus_for_rad(angulo_graus)
    sin=angulo_rad
    termo=angulo_rad
    n=3
    sinal=-1
    while abs(termo) >= precisao:
        termo=(angulo_rad**n)/math.factorial(n)*sinal
        sin+=termo
        n+=2
        sinal*=-1
    return sin
#Função test
def test():
    angulo_graus=float(input("DIGITE UM ÂNGULO: "))
    precisao = float(input("DIGITE A PRECISÃO: "))
    sin_calculado=calcular_sin(angulo_graus, precisao)
    print(f"O seno de {angulo_graus} graus é aproximadamente: {sin_calculado:.4f}")
#test
test()