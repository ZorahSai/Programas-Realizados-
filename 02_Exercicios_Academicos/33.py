#função para calcular PI
def calcular(precisao):
    pi_aprox=0
    for i in range(precisao):
        termo=(-1)**i/(2*i+1)
        pi_aprox +=termo
    pi_aprox *= 4
    return pi_aprox
#test
numero_de_termos=10000
pi=calcular(numero_de_termos)
print("O VALOR APROXIMADO DE π:", pi)