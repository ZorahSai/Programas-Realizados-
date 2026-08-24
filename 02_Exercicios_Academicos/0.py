idades = []
numero = -1

while numero <= 0:
    numero = int(input("INSIRA A IDADE DO ALUNO: "))
    if numero <= 0:
        print("\tVOÇÊ INSERIU UM NUMERO NEGAIVO OU ZERO!!!!\n")
idades.append(numero)

while numero != 0:
    numero = int(input("DIGITA A IDADE DE OUTRO ALUNO: "))
    if numero > 0:
        idades.append(numero)
    elif numero < 0:
        print("\nERROOOOU, VOÇÊ DIGITOU UMA IDADE ERA BIXOOO!!")
media = sum(idades)/len(idades)
print(f"A MEDIA DE IDADES É: {media:0.0f}, de {len(idades):0.0f}")

 

