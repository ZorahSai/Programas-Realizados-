'''Faça  um  programa  didático  para  estudo  das  raízes  quadradas  dos  números,  da 
seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta 
qual  a  raiz  quadrada  desse  valor  para  o  estudante.  O  programa  deve  apresentar  as 
mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma 
semelhante aos anteriores. '''

import random

def treinar_raiz_quadrada():
    estatisticas = {'perguntas': 0, 'acertos': 0, 'erros': 0}
    
    while True:
        # Gera um número aleatório
        numero = random.randint(1, 10)
        
        # Calcula o quadrado do número
        quadrado = numero ** 2
        
        # Pede ao estudante para calcular a raiz quadrada do quadrado
        try:
            resposta = float(input(f"Qual é a raiz quadrada de {quadrado}? "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        estatisticas['perguntas'] += 1
        
        # Verifica se a resposta está correta
        if resposta == numero:
            print("Resposta correta!")
            estatisticas['acertos'] += 1
        else:
            print(f"Resposta incorreta. A raiz quadrada de {quadrado} é {numero}.")
            estatisticas['erros'] += 1
        
        # Pergunta se deseja continuar
        opcao = input("Deseja continuar treinando? (s/n): ").lower()
        if opcao != 's':
            break
    
    # Imprime estatísticas
    print("\nEstatísticas:")
    print(f"Número de perguntas respondidas: {estatisticas['perguntas']}")
    print(f"Número de acertos: {estatisticas['acertos']}")
    print(f"Número de erros: {estatisticas['erros']}")

# Inicia o programa
treinar_raiz_quadrada()
