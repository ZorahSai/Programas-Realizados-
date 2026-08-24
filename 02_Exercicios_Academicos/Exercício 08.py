'''8. Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno 
precisa  ter  média  do  período  (mp)  igual  ou  superior  a  7  pontos.  Caso  contrário,  o 
aluno  será  submetido  a  exame  final,  sendo  a  sua  média  final  (mf)  calculada  pela 
seguinte  fórmula:  mf =  0.6mp +  0.4ne,  onde ne  é  a  nota  do  exame.  Essa  média  final 
deverá  então  ser  igual  ou  superior  a  5  pontos  para  que  o  aluno  seja  aprovado.  Por 
outro lado, a média do período é calculada através da média das notas dos créditos, 
cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o 
número  de  créditos  da  disciplina,  as  notas  dos  créditos,  e  se  necessário  calcule  a 
nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar 
todos  os  créditos  o  aluno  já  estiver  aprovado,  avise  isso  a  ele  e  encerre  a leitura  de 
notas (utilize aqui um comando break).'''

#Função calcular média do período
def calcular_media_periodo(notas, creditos):
    soma_pesos = sum(nota * credito for nota, credito in zip(notas, creditos))
    soma_creditos = sum(creditos)
    return soma_pesos / soma_creditos

#Função determina se o aluno passa ou vai d exame
def verificar_aprovacao(media_periodo):
    if media_periodo >= 7:
        return True
    else:
        return False

#Função calcular nota exame final
def calcular_nota_exame_final(media_periodo):
    nota_exame_final = (5 - 0.6 * media_periodo) / 0.4
    return max(0, nota_exame_final)  


num_disciplinas = int(input('Digite o número de disciplinas: '))


notas = []
creditos = []


for i in range(num_disciplinas):
    nota = float(input(f'   Digite a nota da disciplina {i + 1}: '))
    credito = int(input(f'\tDigite o número de créditos da disciplina {i + 1}: '))

    notas.append(nota)
    creditos.append(credito)

media_periodo = calcular_media_periodo(notas, creditos)

if verificar_aprovacao(media_periodo):
    print(f'\nParabéns! Você passou direto com média {media_periodo:.2f}/10')
else:
    nota_exame_final = calcular_nota_exame_final(media_periodo)
    print(f'\nVocê precisa tirar pelo menos {nota_exame_final:.2f} no exame final para ser aprovado.')
