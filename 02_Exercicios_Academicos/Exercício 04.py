#4)Desejando obter a média aritmética das idades dos alunos do curso de Odontologia, 
#do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a 
# média aritmética das idades. O programa é encerrado quando for lida uma idade igual 
#a zero e deve rejeitar idades negativas, pedindo que o usuário redigite.
lista_idades = []
idade = -1
while idade <= 0:
    idade = int(input("Digite a idade de um aluno do curso de Odontologia: "))
    if idade <= 0:
        print('\tPor favor, digite uma idade válida: \n')

lista_idades.append(idade)

while idade != 0:
    idade = int(input("Digite outra idade de um aluno: "))
    if idade > 0:
        lista_idades.append(idade)
    elif idade < 0:
        print('\tPor favor, digite uma idade válida.\n')
    
media = sum(lista_idades) / len(lista_idades)
print(f"A Média das idades dos alunos de Odontologia é: {media}, de {len(lista_idades)} alunos!")
