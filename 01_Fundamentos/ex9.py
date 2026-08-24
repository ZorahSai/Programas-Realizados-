'''9. O que acontece no programa anterior se a pessoa nasceu há 18 anos, mas ainda não
fez aniversário? Melhore o programa para que, neste caso, o programa pergunte se a
pessoa já fez aniversário ou não antes de imprimir o resultado.'''
nasc = int(input("Digite o ano de nascimento: "))
ANO = 2025
MAIORIDADE = 18
idade = ANO - nasc
if idade > MAIORIDADE:
    print("A pessoa é maior de idade.")
elif idade < MAIORIDADE:
    print("A pessoa é menor de idade.")
else:
    aniver = input("Você já fez aniversário este ano? (s/n): ")
    if aniver == 's':
        print("A pessoa é maior de idade.")
    elif aniver == 'n':
        print("A pessoa é menor de idade.")
    else : 
        print("Informação inválida!!")