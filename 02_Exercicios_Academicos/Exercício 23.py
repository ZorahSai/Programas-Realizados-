'''Em  um  cinema  que  possui  capacidade  de  50  lugares foi  distribuído  um  questionário 
aos  expectadores,  no  qual  constava  a  idade  e  a  sua  opinião  em  relação  ao  filme, 
segundo:  ótimo,  bom,  regular,  ruim  ou  péssimo.  Elabore  um  programa  que,  lendo 
estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule 
e imprima: 
a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo. 
b. A percentagem de ótimo, bom, regular, ruim e péssimo. 
c. A idade do mais velho entrevistado. 
d. A idade do mais novo entrevistado. '''

# Lista para armazenar as idades dos espectadores
idades = []

# Dicionário para armazenar as contagens de opiniões
contagem_opinioes = {"ótimo": 0, "bom": 0, "regular": 0, "ruim": 0, "péssimo": 0}

# Capacidade máxima do cinema
capacidade_cinema = 3

# Loop para ler os dados dos espectadores
for i in range(capacidade_cinema):
    print(f"Informações do espectador {i+1}:")
    idade = int(input("Idade do espectador: "))
    opiniao = input("Opinião do espectador (ótimo, bom, regular, ruim, péssimo): ").lower()

    # Armazena a idade do espectador
    idades.append(idade)

    # Atualiza a contagem de opiniões
    contagem_opinioes[opiniao] += 1

# Calcula as estatísticas
quantidade_total = len(idades)
idade_mais_velho = max(idades)
idade_mais_novo = min(idades)

# Calcula as percentagens
percentagens_opinioes = {opiniao: (contagem / quantidade_total * 100) if quantidade_total > 0 else 0 
                        for opiniao, contagem in contagem_opinioes.items()}

# Impressão dos resultados
print("\n--- Resultados ---")
print("Quantidade de respostas:")
for opiniao, contagem in contagem_opinioes.items():
    print(f"{opiniao.capitalize()}: {contagem}")

print("\nPercentagem de respostas:")
for opiniao, percentagem in percentagens_opinioes.items():
    print(f"{opiniao.capitalize()}: {percentagem:.2f}%")

print("\nIdade do mais velho entrevistado:", idade_mais_velho)
print("Idade do mais novo entrevistado:", idade_mais_novo)

