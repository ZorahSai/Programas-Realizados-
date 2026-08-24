#Função para calcular o aumento do solario
def aumento_salario(salario):
    if salario <= 1000:
        return salario * 0.15
    elif salario <= 2000:
        return salario * 0.10
    elif salario > 2000:
        return salario *0.05
#Função para informar o numero de funcionarios
q_funcionarios = int(input("INSIRA O NUMERO DE FUNCIONARIOS: "))
#Variáveis
salario_normal=0
salario_futuro_u=0
salario_futuro_total=0
#Coleta de dados e calculo dos resultados
for _ in range(q_funcionarios):
    salario_atual = float(input("INSIRA O SALARIO DO FUNCIONARIO: "))
    salario_normal += salario_atual
    #Novo salario(u)
    novo_u=salario_atual *1.10
    salario_futuro_u +=novo_u
    #Novo salario(p)
    novo_p=salario_atual+aumento_salario(salario_atual)
    salario_futuro_total +=novo_p
    #Print do novo salario
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Novo salário(Uniforme): R$ {novo_u:.2f}")
    print(f"Novo salário(Progressivo): R$ {novo_p:.2f}")
#Media dos salarios de todos os funcionarios
if q_funcionarios != 0:
    media=salario_normal/q_funcionarios
else:
    media = 0
#Prints finais
print(" [RESULTADOS:]")
print(f"NUMERO DE FUNCIONÁRIOS: {q_funcionarios}                   ")
print(f"MÉDIA DE SALARIOS: R$ {media:.2f}                          ")
print(f"FOLHA DE PAGAMENTO ATUAL: R$ {salario_normal:.2f}          ")
print(f"FOLHA DE PAGAMENTO FUTURA(U): R$ {salario_futuro_u:.2f}    ")
print(f"FOLHA DE PAGAMENTO FUTURA(P): R$ {salario_futuro_total:.2f}")

#ECONOMIA PARA A EMPRESA
if salario_futuro_u < salario_futuro_total:
    print("O aumento uniforme é mais econômico!")
elif salario_futuro_u > salario_futuro_total:
    print("O aumento progressivo é mais econômico!")
elif salario_futuro_u == salario_futuro_total:
    print("Ambas as opções tem o mesmo custo!")