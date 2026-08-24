'''10. A convenção de graus Fahrenheit para Celsius é obtida pela fórmula 𝑪=𝟓.(𝑭−𝟑𝟐)/𝟗. 
Escreva  um  programa  que  calcule  e  imprima  uma  tabela  de  graus  centígrados  em 
função  de  graus  Fahrenheit  que  variem  de  50  a  150  de  5  em  5.  Utilize  constantes 
simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5).'''

# Constantes simbólicas
INICIO_FAHRENHEIT = 50
FIM_FAHRENHEIT = 150
DIFERENÇA_FAHRENHEIT = 5

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return 5*(fahrenheit - 32) / 9

#loop
print("Fahrenheit\tCelsius")
print("_______________________")
for fahrenheit in range(INICIO_FAHRENHEIT, FIM_FAHRENHEIT + 1, DIFERENÇA_FAHRENHEIT):
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}\t\t{celsius:.2f}")
print("_______________________")