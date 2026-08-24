'''9. Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a 
exercícios  sobre  o  mesmo  assunto  até  que  ele  alcance  a  nota  máxima  (100  pontos), 
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo 
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior. 
Caso  contrário, ele permanece  no  mesmo nível, zerando  novamente os pontos 
acumulados.  Faça  um  programa  que  compute  o  progresso  do  aluno,  através  da 
leitura  de  suas  notas  até  que  ele  termine  o  10º  nível.  Utilize  o  comando  break  (por 
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota 
máxima). '''

pontos_Acumulados = 0
nivel_Inicial = 1

while nivel_Inicial <= 10:
    tentativas = 0

    while tentativas < 5:
        notas_Exercícios = int(input(f'Digite a nota do aluno de nivel ({nivel_Inicial}): ')) 

        if (notas_Exercícios == 100):
            print(f'Parabens, você atingiu a nota máxima do seu nivel, avançará para o proximo. {nivel_Inicial}->{max(10,nivel_Inicial+1)}')
            nivel_Inicial += 1
            pontos_Acumulados = 0
            break

        elif(notas_Exercícios > 100 or notas_Exercícios < 0):
            print('\tPor favor, coloque uma nota válida!')
            
        else:
            pontos_Acumulados +=notas_Exercícios
            tentativas +=1

            if pontos_Acumulados < 300 and tentativas == 5:
                print(f'\tVocê não bateu os 300 pontos acumulados, irá retornar um nível {nivel_Inicial} -> {max(1, nivel_Inicial - 1)}')
                nivel_Inicial = max(1, nivel_Inicial - 1)  # O max protege o nível para não se tornar igual ou menor a zero
                pontos_Acumulados = 0
                tentativas = 5
                break
            else:
                print(f'\tPontos acumulados: {pontos_Acumulados}. \n\tTente novamente no mesmo nível')
                if pontos_Acumulados >= 300:
                    print(f'\tAtingiu 300 pontos acumulados, resetando os pontos')
                    pontos_Acumulados = 0
print('##Parabens, vc completou os 10 niveis##')