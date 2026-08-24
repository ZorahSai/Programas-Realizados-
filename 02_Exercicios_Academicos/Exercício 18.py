'''18. O número 3025 possui a interessante característica:  
30 + 25 = 55 
552 = 3025 
Faça um programa que procure todos os números de 4 algarismos que possuem essa 
característica.'''


def verifica_caracteristica(numero):
    #separa os dois primeiros dígitos
    primeiro_dois_digitos = numero // 100
    #separa os dois últimos dígitos
    ultimos_dois_digitos = numero % 100
    
    #soma dos dois primeiros e eleva ao quadrado
    soma = primeiro_dois_digitos + ultimos_dois_digitos
    quadrado_da_soma = soma ** 2
    
    
    if quadrado_da_soma == numero:
        return True
    else:
        return False

#itera sobre todos os números de 1000 a 9999
for num in range(1000, 10000):
    if verifica_caracteristica(num):
        print(num)
