#Verificação de intens repetidos de uma lista usando PANDAS e Python Puro

import pandas as pd
from collections import Counter

lista_numeros = [1, 2, 3, 1, 2, 1, 4, 3, 2, 1]

porcentagens = pd.Series(lista_numeros).value_counts(normalize=True)*100
print("--- Estatísticas do Sorteio (Pandas) ---")
for numero, porcentagem in porcentagens.items():
    print(f"O número {numero} saiu em {porcentagem:.2f}% dos sorteios.")

total_sorteios = len(lista_numeros)
contador = Counter(lista_numeros)
print("--- Estatística do Sorteio (Puro) ---")
for numero, quantidade in contador.items():
    pcem = (quantidade / total_sorteios)*100
    print(f"Número {numero}: {quantidade} vezes - {porcentagem:.2f}%")

print(contador.items())
print(porcentagens.items())