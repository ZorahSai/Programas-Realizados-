# exercicio 11
'''Elabore um programa que dado o peso de um boxeador, informe à categoria a qual
pertence, seguindo a tabela abaixo.

Categoria Massa (Kg)
Palha < 50
Pluma < 59
Leve < 75
Pesado < 87
Super Pesado >= 87'''

peso_boxeador = float(input("Digite seu peso (kg):"))
if peso_boxeador < 50:
    print("Seu peso está na categoria 'palha'")
elif peso_boxeador < 59:
    print("Seu peso está na categoria 'pluma'")
elif peso_boxeador < 75:
    print("Seu peso está na categoria 'leve'")
elif peso_boxeador < 87:
    print("Seu peso está na categoria 'pesado'")
elif peso_boxeador >= 87:
    print("Seu peso está na categoria 'super pesado'")