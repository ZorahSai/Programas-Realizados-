#3. Em  um  frigorífico,  cada  boi  é  identificado  por  um  cartão  que  contém  seu  número  e 
#seu peso. Faça um programa que leia os números de identificação e o peso de cada 
#boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi 
#mais magro e o total de peso dos bois do frigorífico.
bois=[]

def obter_peso(boi):
    return boi[1]

while True:
    numero = int(input('Digite o numero de identificação do boi: '))

    if numero <=0:
        break

    peso = float(input('Digite o peso do boi: '))
    bois.append([numero,peso])

if bois:
    boi_mais_magro = min(bois, key=obter_peso)
    boi_mais_gordo = max(bois, key=obter_peso)
    
    total_peso = sum(boi[1] for boi in bois)

    print(f'Boi mais magro e seu peso: {boi_mais_magro}')
    print(f'Boi mais gordo e seu peso: {boi_mais_gordo}')
    print(f'Total de peso dos bois: {total_peso}')

else:
    print('Você não inseriu nenhum boi')