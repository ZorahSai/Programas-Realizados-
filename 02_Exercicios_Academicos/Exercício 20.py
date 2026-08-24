'''Elabore  um  outro  programa  didático  nos  mesmos  moldes  do  anterior  para  treino  da 
divisão.  Neste  programa  deve  ser  perguntado  à  criança  o  resultado  da  divisão  e  o 
resto. '''

import random

def treinar_divisao():
    # Dicionário para armazenar o número de perguntas respondidas, acertos e erros
    estatisticas = {'perguntas': 0, 'acertos': 0, 'erros': 0}
    
    while True:
        continuar = True
        while continuar:
            divisor = random.randint(1, 10)
            # Garante que o dividendo será múltiplo do divisor para evitar divisões com resto
            dividendo = random.randint(divisor, 10) * divisor
        
            # Calcula a resposta correta
            resultado_correto = dividendo // divisor
            resto_correto = dividendo % divisor
            
            # Pedepara responder
            try:
                resultado_usuario = int(input(f"Quanto é {dividendo} dividido por {divisor}? "))
                resto_usuario = int(input(f"E qual é o resto da divisão de {dividendo} por {divisor}? "))
            except ValueError:
                print("Por favor, insira apenas números inteiros.")
                continue
            
            estatisticas['perguntas'] += 1
            
            if resultado_usuario == resultado_correto and resto_usuario == resto_correto:
                print("Resposta correta!")
                estatisticas['acertos'] += 1
            else:
                print(f"Resposta incorreta. O resultado correto é {resultado_correto} com resto {resto_correto}.")
                estatisticas['erros'] += 1
            
            # Pergunta se deseja continuar
            opcao = input("Deseja continuar treinando? (s/n): ").lower()
            if opcao != 's':
                continuar = False
        
        # Imprime estatísticas
        print("\nEstatísticas:")
        print(f"Número de perguntas respondidas: {estatisticas['perguntas']}")
        print(f"Número de acertos: {estatisticas['acertos']}")
        print(f"Número de erros: {estatisticas['erros']}")
        
        # Pergunta se deseja reiniciar o programa
        reiniciar = input("Deseja treinar novamente? (s/n): ").lower()
        if reiniciar != 's':
            break

# Inicia o programa
treinar_divisao()

