''' Foi  realizada  uma  pesquisa  de  algumas  características  físicas  da  população  de  uma 
certa região,  a  qual foram  coletados  os  seguintes  dados referentes a  cada  habitante 
para serem analisados: 
• Sexo. 
• Cor dos olhos (azuis, verdes, castanhos). 
• Cor dos cabelos (louros, castanhos, pretos). 
• Idade. 
Faça um programa que determine e escreva: 
a. O total de entrevistados 
b. O total de homens e o total de mulheres entrevistados 
c. A maior e a menor idade do conjunto de habitantes; 
d. A média de idade do conjunto de habitantes; 
e. A  percentagem  de  indivíduos  de  sexo  feminino  cuja  idade  está  entre  18  e  35 
anos inclusive e que tenham olhos verdes e cabelos louros. 
O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.'''

# Variáveis para armazenar as contagens e estatísticas
total_entrevistados = 0
total_homens = 0
total_mulheres = 0
maior_idade = float('-inf')
menor_idade = float('inf')
soma_idades = 0
mulheres_18_35_olhos_verdes_cabelos_louros = 0

# Loop para coletar os dados dos habitantes
while True:
    sexo = input("Sexo (M/F, ou -1 para sair): ").upper()
    if sexo == '-1':
        break

    cor_olhos = input("Cor dos olhos (azuis, verdes, castanhos): ").lower()
    cor_cabelos = input("Cor dos cabelos (louros, castanhos, pretos): ").lower()
    idade = int(input("Idade: "))

    # Contagem total de entrevistados
    total_entrevistados += 1

    # Contagem de homens e mulheres
    if sexo == 'M':
        total_homens += 1
    elif sexo == 'F':
        total_mulheres += 1

    # Atualização da maior e menor idade
    maior_idade = max(maior_idade, idade)
    menor_idade = min(menor_idade, idade)

    # Soma das idades para cálculo da média
    soma_idades += idade

    # Contagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros
    if sexo == 'F' and 18 <= idade <= 35 and cor_olhos == 'verdes' and cor_cabelos == 'louros':
        mulheres_18_35_olhos_verdes_cabelos_louros += 1

# Calcular média de idade
media_idade = soma_idades / total_entrevistados if total_entrevistados > 0 else 0

# Calcular a porcentagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros
porcentagem_mulheres_18_35_olhos_verdes_cabelos_louros = (mulheres_18_35_olhos_verdes_cabelos_louros / total_mulheres) * 100 if total_mulheres > 0 else 0

# Impressão dos resultados
print("\n--- Resultados ---")
print("Total de entrevistados:", total_entrevistados)
print("Total de homens entrevistados:", total_homens)
print("Total de mulheres entrevistadas:", total_mulheres)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)
print("Média de idade:", media_idade)
print("Porcentagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros: {:.2f}%".format(porcentagem_mulheres_18_35_olhos_verdes_cabelos_louros))
