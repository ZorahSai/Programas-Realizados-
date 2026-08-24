''' Faça um programa didático para estudo de tabuadas de 1 até 10, onde: 
a. A criança escolhe a tabuada a ser estudada. 
b. O programa gera um número aleatório e pergunta à criança qual o valor dele 
multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta 
novamente, se acertar o programa pergunta à criança se ela deseja continuar 
respondendo. 
c. Ao final, o programa deve imprimir o número de perguntas respondidas, o número de 
acertos e o número de erros cometidos pela criança.'''

import random

def estudar_tabuada():
    # Dicionário para armazenar o número de perguntas respondidas, acertos e erros
    estatisticas = {'perguntas': 0, 'acertos': 0, 'erros': 0}
    
    while True:
        tabuada = int(input("Escolha a tabuada que deseja estudar (1 a 10): "))
        if tabuada < 1 or tabuada > 10:
            print("Por favor, escolha um número entre 1 e 10.")
            continue
        
        continuar = True
        while continuar:
            # Gera um número aleatório entre 1 e 10
            numero_aleatorio = random.randint(1, 10)
            # Calcula a resposta correta
            resposta_correta = numero_aleatorio * tabuada
            # Pede à criança para responder
            resposta_usuario = int(input(f"Quanto é {numero_aleatorio} vezes {tabuada}? "))
            estatisticas['perguntas'] += 1
            
            if resposta_usuario == resposta_correta:
                print("Resposta correta!")
                estatisticas['acertos'] += 1
            else:
                print(f"Resposta incorreta. O resultado correto é {resposta_correta}.")
                estatisticas['erros'] += 1
            
            # Pergunta se deseja continuar
            opcao = input("Deseja continuar estudando? (s/n): ").lower()
            if opcao != 's':
                continuar = False
    
        # Imprime estatísticas
        print("\nEstatísticas:")
        print(f"Número de perguntas respondidas: {estatisticas['perguntas']}")
        print(f"Número de acertos: {estatisticas['acertos']}")
        print(f"Número de erros: {estatisticas['erros']}")
        
        # Pergunta se deseja reiniciar o programa
        reiniciar = input("Deseja estudar outra tabuada? (s/n): ").lower()
        if reiniciar != 's':
            break

# Inicia o programa
estudar_tabuada()
