'''6. Um programa didático para crianças consiste em pedir dois números inteiros
quaisquer para a criança e depois perguntar a soma desses dois números. Se a
resposta estiver certa, o programa imprime uma mensagem de incentivo. Se não, o
programa imprime o valor correto da soma. Implemente esse programa.'''

n1 = int(input("Digite um número qualquer:"))
n2 = int(input("Digite outro número qualquer:"))
soma = n1 + n2
pergunta = int(input("Qual é a soma dos números? "))
if soma == pergunta : 
    print("Isso mesmo!!! ",n1,"+",n2,"=",soma)
else :
     print("Ahhhhh, não foi dessa vez :/ Tente na próxima!");