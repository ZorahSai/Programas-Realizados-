'''11. O volume de uma esfera pode ser calculado pela fórmula (4/3) *pi * (raio**3) onde r é o raio da 
esfera.  Faça  um  programa  que  imprima  uma  tabela  de  volumes  para  esferas  que 
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.  '''
import math
def calcular_volume_esfera(raio):
    return (4/3) * math.pi * (raio**3)

print("Raio (cm)\tVolume da Esfera (cm³)")
print("---------------------------------")
#loop
raio_atual = 0
while raio_atual <= 15:
    volume = calcular_volume_esfera(raio_atual)
    print(f"{raio_atual:.1f}\t\t{volume:.2f}")
    raio_atual += 0.5

print("---------------------------------")
