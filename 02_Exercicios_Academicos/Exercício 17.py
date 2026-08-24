'''O  número  pi  pode  ser  calculado  através  da  série: ...9
pi = 4 - 4/3 + 4/5 + 4 /7 + 4/9  Faça  um 
programa  para  calcular  o  valor  de  pi  com  precisão  de  0,00001  (o  programa  encerra 
quando a parcela da série for menor que a precisão). '''

def calcular_pi(precisao):
    soma = 0
    denominador = 1
    termo = 4 / denominador
    sinal = 1

    while abs(termo) > precisao:
        soma += sinal * termo
        denominador += 2
        termo = 4 / denominador
        sinal *= -1

    return soma

precisao = 0.00001
pi = calcular_pi(precisao)
print("Valor de pi com precisão de {:.5f}(ou 1e-05):".format(precisao), "{:.10f}".format(pi))
