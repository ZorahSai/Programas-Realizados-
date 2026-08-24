'''Para  fazer  uma  pesquisa  sobre  o  consumo  de  energia  elétrica  de  uma  cidade,  são 
fornecidos os seguintes dados:  
• O preço o kWh 
• O número de identificação de cada consumidor 
• A quantidade de kWh consumido no mês por cada um 
• O código do tipo de consumidor (residencial, comercial ou industrial)

A partir desses dados calcule:  
a. Para cada consumidor, o total a pagar;  
b. O maior consumo verificado;  
c. O menor consumo verificado 
d. O total de consumo (em kWh) para cada um dos três tipos de consumidores 
e. A média de consumo (em kWh) para cada um dos três tipos de consumidores 
f. O total arrecadado pela companhia elétrica.'''

# Inputs dos dados da cidade
preco_kwh = float(input("Preço do kWh: "))
numero_consumidores = int(input("Número total de consumidores: "))

# Inicialização de variáveis
maior_consumo = float('-inf')
menor_consumo = float('inf')
total_consumo = [0, 0, 0]  # Índices: 0 - Residencial, 1 - Comercial, 2 - Industrial
total_arrecadado = 0

# Loop para coletar os dados de cada consumidor
for _ in range(numero_consumidores):
    print("\nDados do consumidor:")
    id_consumidor = input("Número de identificação do consumidor: ")
    consumo_kwh = float(input("Quantidade de kWh consumidos no mês: "))
    codigo_tipo_consumidor = int(input("Código do tipo de consumidor (1 - Residencial, 2 - Comercial, 3 - Industrial): ")) - 1
    
    # Atualizar o maior e o menor consumo verificado
    maior_consumo = max(maior_consumo, consumo_kwh)
    menor_consumo = min(menor_consumo, consumo_kwh)
    
    # Atualizar o total de consumo para cada tipo de consumidor
    total_consumo[codigo_tipo_consumidor] += consumo_kwh
    
    # Calcular o total a pagar para este consumidor e adicionar ao total arrecadado
    total_a_pagar = preco_kwh * consumo_kwh
    total_arrecadado += total_a_pagar

# Calcular a média de consumo para cada tipo de consumidor
media_consumo = [total_consumo[i] / max(1, total_consumo.count(i)) for i in range(3)]


# Impressão dos resultados
print("\n--- Resultados ---")
print("Maior consumo verificado:", maior_consumo, "kWh")
print("Menor consumo verificado:", menor_consumo, "kWh")
print("Total de consumo para cada tipo de consumidor:")
print("Residencial:", total_consumo[0], "kWh")
print("Comercial:", total_consumo[1], "kWh")
print("Industrial:", total_consumo[2], "kWh")
print("Média de consumo para cada tipo de consumidor:")
print("Residencial:", media_consumo[0], "kWh")
print("Comercial:", media_consumo[1], "kWh")
print("Industrial:", media_consumo[2], "kWh")
print("Total arrecadado pela companhia elétrica: R$", total_arrecadado)
