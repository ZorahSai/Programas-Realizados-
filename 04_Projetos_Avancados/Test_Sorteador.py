import random
from collections import Counter as co
lista = []
def sortear():
    print("[SORTEADOR DE NUMEROS]")
    try:
        menor = 1
        maior = int(input("DIGITE O MAIOR NÚMERO PARA SER SORTEADO: "))
        numero_x=int(input("DIGITE QUANTOS SORTEIOS SERAM FEITOS: "))
        if menor >= maior:
           print("O NUMERO TEM QUE SER MAIOR QUE ZERO PARA SER SORTEADO")
           return
        if numero_x <=0:
            print("O NUMERO DE SORTEIOS TEM QUE SER MAIOR QUE ZERO!")
            return
        for _ in range(numero_x):
            numero= random.randint(menor,maior)
            print(f"O NÚMERO SORTEADO É: {numero}")
            lista.append(numero)
    except ValueError:
        print("INSIRA VALORES VALIDO!!!")

def anialisador(lista):
    contagem = co(lista)
    visitados = set()
    for n in lista:
        if n not in visitados:
            contagem[n]
            visitados.add(n)
sortear()
print(lista)
