'''Escreva um programa que, dadas duas datas, determine qual delas ocorreu
cronologicamente primeiro. Para cada uma das duas datas, leia três números
referentes ao dia, mês e ano, respectivamente.'''

d1 = int(input("Digite o dia da primeira data: "))
m1 = int(input("Digite o mês da primeira data: "))
a1 = int(input("Digite o ano da primeira data: "))
d2 = int(input("Digite o dia da segunda data: "))
m2 = int(input("Digite o mês da segunda data: "))
a2 = int(input("Digite o ano da segunda data: "))

if a1 < 0 or a2 < 0:
    print("Esse ano não existe")
else :
    if m1 > 12 or m2 > 12:
        print("Esse mês não existe")
    else:
        if (m1 == 2 or m2 == 2) and (d1>28 or d2>28):
                print("Esse dia não existe")
        else:
             if (m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11) or (m2 == 4 or m2 == 6 or m2 == 9 or m2 == 11) and (d1>30 or d2>30):
                  print("Esse dia não existe")
             elif (d1 > 31 or d2 > 31):
                  print("Esse dia não existe")
             else :
                    if a1 < a2 :
                       print("A primeira data aconteceu antes")
                    elif a1 > a2 :
                       print("A segunda data aconteceu antes")
                    else:
                       if m1 < m2 :
                            print("A primeira data aconteceu antes")
                       elif m1 > m2 :
                            print("A segunda data aconteceu antes")
                       else:
                            if d1 < d2 :
                                 print("A primeira data aconteceu antes")     
                            elif d1 > d2:
                                 print("A segunda data aconteceu antes")   
                            else:
                                 print("As datas são iguais")   
                

